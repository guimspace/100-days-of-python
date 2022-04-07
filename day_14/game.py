import random
from game_data import data


def main():
    score = 0
    random.shuffle(data)

    while True:
        print(f"Score: {score}\n")

        advA = data.pop()
        advB = data.pop()

        print(f'A: {advA["name"]}, a {advA["description"]} from {advA["country"]}')
        print("\t\tvs")
        print(f'B: {advB["name"]}, a {advB["description"]} from {advB["country"]}')

        o = input("Who has more followers? [a,b]: ").lower()
        while o != "a" and o != "b":
            o = input("")

        t = advA["follower_count"] > advB["follower_count"]
        if (t and o == "a") or (not t and o == "b"):
            score += 1
            print("Correct!\n\n")
        else:
            print("Game over!")
            print(f"Score: {score}\n")
            break


if __name__ == "__main__":
    main()
