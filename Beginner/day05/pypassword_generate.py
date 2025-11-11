from secrets import token_urlsafe
import random

# print("welcome to the PyPassword Generator!")
# quantity_letters = input("How many letters would you like in your password?")
# quantity_symbols = input("how many symbols would you like?")
# quantity_numbers = input("How many numbers would you like?")

token = token_urlsafe(10)
print(token)
list_item = list(token)
random.shuffle(list_item)
new_token = ''
for i in list_item:
    new_token += i
print(new_token)
