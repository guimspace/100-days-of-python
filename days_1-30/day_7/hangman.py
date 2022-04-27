import random
from wordlist import wordlist

lives = 6
secret_word = random.choice(wordlist)

guess_word = []
for _ in range(len(secret_word)):
    guess_word += "_"

while lives > 0:
    print("Live: " + str(lives))
    print(" ".join(guess_word) + "\n")

    g = input("Guess a letter: ").lower()[0]

    if g not in secret_word:
        lives -= 1
        print("Wrong\n")
    else:
        for p in range(len(secret_word)):
            if g == secret_word[p]:
                guess_word[p] = g

        if "_" not in guess_word:
            break

        print("Right\n")


print("GAME OVER")
print("Lives: " + str(lives))
print("Word: " + secret_word)
print("You:  " + "".join(guess_word) + "\n")
