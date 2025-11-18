"""
Show the work empty and complete with chosen letter by user.
"""

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

empty_word = ["_" for _ in chosen_word]
print("".join(empty_word))

guess: str = input("Guess a letter: ").lower()
for idx, letter in enumerate(chosen_word):
    if guess == letter:
        empty_word[idx] = chosen_word[idx]

print("".join(empty_word))
