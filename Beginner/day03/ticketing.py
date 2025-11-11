height = int(input("Whats your height? "))


def priceToAge(age):
    if age >= 18:
        return 12
    elif age <= 12:
        return 5
    return 7


bill = 0
if height >= 120:
    print("can ride")
    age = int(input("what's your age? "))
    bill = priceToAge(age)

    wants_photo = input("What's photo? (yes or no)")
    if wants_photo == "yes":
        bill += 3
    print(f"the total bill ${bill}")
else:
    print("can don't ride")
