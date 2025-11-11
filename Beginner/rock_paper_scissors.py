import random
rock = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
allowed_gestures = [rock, paper, scissors]
your_choise_number = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 fos Scissors."
))

your_choise = allowed_gestures[your_choise_number]
print(your_choise)

print("Computer choise:")
computer_choise = random.choice(allowed_gestures)
print(computer_choise)

you_win = [
        your_choise == paper and computer_choise == rock,
        your_choise == scissors and computer_choise == paper,
        your_choise == rock and computer_choise == scissors
]
you_lose = [
        your_choise == paper and computer_choise == scissors,
        your_choise == scissors and computer_choise == rock,
        your_choise == rock and computer_choise == paper
]

print("you win"
      if any(you_win)
      else "You lose" if any(you_lose)
      else "It's a draw" if your_choise == computer_choise
      else "you typed an invalid number. You lose!")
