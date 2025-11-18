"""
    added loop
"""
from hangman_art import stages
from hangman_words import word_list
import random

lives = 6

chosen_word = random.choice(word_list)

placeholder = "".join(["_" for _ in chosen_word])
game_over = False
correct_letters = []

while not game_over:
    print(f"****************{lives}/6 LIVES LEFT******************")
    display = ""
    guess: str = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: ", display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print("****************YOU LOSE******************")

    if "_" not in display:
        game_over = True
        print("****************YOU WIN******************")
    print(stages[lives])
