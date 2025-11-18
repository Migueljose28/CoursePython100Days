
"""
    added loop
"""

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = "".join(["_" for _ in chosen_word])
game_over = False
correct_letters = []

while not game_over:
    display = ""
    guess: str = input("Guess a letter: ").lower()

    for idx, letter in enumerate(chosen_word):
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to Guess: \n", display)

    if "_" not in display:
        game_over = True
        print("you win!")
