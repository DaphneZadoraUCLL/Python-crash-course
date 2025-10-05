pizzas = ["Hawai", "Bolognese", "Tonno"]
friends_pizzas = pizzas[:]

pizzas.append("Funghi")
friends_pizzas.append("Peperoni")

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
print()
for pizza in friends_pizzas:
    print(f"My friend's favorite pizzas are: {pizza}")
