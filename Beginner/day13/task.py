"""
Learn about try and except error.
The program reads user's age and returns whether they are over 18 years old.
"""

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}")
