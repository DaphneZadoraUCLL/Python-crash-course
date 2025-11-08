message = "Welcome, please add your wanted topping (or type quit to finish): "
toppings = []
while True:
    topping = input(message)
    if topping.lower() == "quit":
        toppings_string = ", ".join(toppings) if toppings else "no toppings"
        print(
            f"Preparing your pizza with the following toppings: {toppings_string}")
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)
