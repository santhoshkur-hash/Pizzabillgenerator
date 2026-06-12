print("Welcome to Python Pizza deliveries.")

# The loop starts here
while True:
    pizza_size = input("\nEnter pizza size S, M and L (or type 'quit' to exit): ").upper()

    # Check if user wants to exit
    if pizza_size == "QUIT":
        print("Thank you for using the Pizza Calculator. Goodbye!")
        break  # This exits the loop and stops the program

    pepperoni = input("Do you want pepperoni? Yes or no? ").capitalize()
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

    # 2 & 3. Calculate additions
    if valid_input:
        if pepperoni == "Yes":
            if pizza_size == "S":
                bill += 2
            else:
                bill += 3
        if cheese == "Yes":
            bill += 1
        print(f"Total Bill Amount: {bill} INR")

# The window will now stay open until the user types 'quit'