print("Welcome to Python Pizza deliveries.")
pizza_size = input("Enter pizza size S, M and L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Yes or no? ").capitalize()
cheese = input("Do you want extra cheese? Yes or no? ").capitalize()

bill = 0
valid_input = True

# 1. Set the base price
if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25
else:
    print("Invalid size selected.")
    valid_input = False

# 2 & 3. Calculate additions ONLY if the size was valid
if valid_input:
    if pepperoni == "Yes":
        if pizza_size == "S":
            bill += 2
        else:
            bill += 3

    if cheese == "Yes":
        bill += 1

    print(f"Total Bill Amount: {bill} INR")