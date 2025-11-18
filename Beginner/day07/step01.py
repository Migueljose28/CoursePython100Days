"""
    Fisrt logic for read and display letter right
"""
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess: str = input("Guess a letter: ").lower()
for letter in chosen_word:
    print("Right" if guess == letter else "Wrong")
