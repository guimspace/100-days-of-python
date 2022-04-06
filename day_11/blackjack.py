import random

def init_game(game):
    game["decks"] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * game["num_decks"]
    random.shuffle(game["decks"])

    game["dealer"] = [];
    game["player"] = [];

    hit_deck(game)
    hit_deck(game, "dealer")

    hit_deck(game)
    hit_deck(game, "dealer")

def print_stats(stats):
    print(f"Stats: {' '.join([str(i) for i in stats])}")

def print_hands(game, game_on = True):
    if game_on:
        print(f"Dealer: ? = ? + {' + '.join([str(i) for i in game['dealer'][1::]])}")
    else:
        print(f"Dealer: {sum(game['dealer'])} = {' + '.join([str(i) for i in game['dealer']])}")

    print(f"Player: {sum(game['player'])} = {' + '.join([str(i) for i in game['player']])}")

def end_game(p):
    if p == -1:
        print("Player Win")
    elif p == 1:
        print("Dealer Win")
    else:
        print("Tie")
    input("")

def fix_hand(game, t = "player"):
    while sum(game[t]) > 21 and 11 in game[t]:
        i = game[t].index(11)
        game[t][i] = 1

def hit_deck(game, t = "player"):
    game[t].append(game["decks"].pop())
    fix_hand(game, t)

def main():
    stats = [0, 0, 0]
    game = {
        "num_decks": 4,
        "decks": [],
        "dealer": [],
        "player": []
    }

    while True:
        init_game(game)
        fix_hand(game)

        print_stats(stats)
        print("")
        print_hands(game)

        p = 0
        while sum(game["player"]) < 21:
            c = input("Choose hit or stand [H/s]: ").lower()
            if c != "s":
                hit_deck(game)
            else:
                break

            print("")
            print_hands(game)

        sum_player = sum(game["player"])
        if sum_player > 21:
            p = 1
        elif sum_player == 21:
            p = -1

        if p != 0:
            print("")
            stats[1 + p] += 1
            end_game(p)
            continue

        print("")
        print_hands(game, False)

        sum_dealer = sum(game["dealer"])
        if sum_dealer < 17:
            hit_deck(game, "dealer")
            sum_dealer = sum(game["dealer"])
            print("")
            print_hands(game, False)

        if sum_dealer > 21 or sum_player > sum_dealer:
            p = -1
        elif sum_dealer == 21 or sum_player < sum_dealer:
            p = 1

        print("")
        stats[1 + p] += 1
        end_game(p)

if __name__ == "__main__":
    main()
