active = True

while active:
    age = input(
        "How old are you so I can tell you the price of your movie ticket? (Or type quit to exit): ")
    if age.lower() == "quit":
        active = False
        print("Thank you, have a nice day!")

    else:
        age = int(age)

        if age < 3:
            print("Your movie ticket is free!")
        elif age > 12:
            print("Your movie ticket will cost $15.")
        else:
            print("Your movie ticket will cost $10.")
