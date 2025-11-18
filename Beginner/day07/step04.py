"""
    added loop
"""

import random

stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
stages.reverse()
lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = "".join(["_" for _ in chosen_word])
game_over = False
correct_letters = []

while not game_over:
    display = ""
    guess: str = input("Guess a letter: ").lower()
    trying = 0
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("you win!")
    print(stages[lives])
