active = True

while active:
    topping = input(
        "Please enter the topping you would like (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
print("Your pizza is being prepared with the selected toppings.")
