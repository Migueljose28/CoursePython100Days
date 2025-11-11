print("Welcome to Pizza Deliveries!")
size = input("Whats size pizza do you want? S, M or L: ")
wants_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 15 if size == "S" else 20 if size == "M" else 25
bill += 1 if extra_cheese.upper() == "Y" else 0

if wants_pepperoni.upper() == "Y":
    bill += 2 if size == "S" else 3

if size not in ["S", "M", "L"] or any(
        option not in ["Y", "N"]
        for option in [wants_pepperoni, extra_cheese]):
    print("You typed the wrong inputs.")
else:
    print(f"Your final bill in {bill}")

