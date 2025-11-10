def build_sandwich(*toppings):
    print("\nBuilding a sandwich with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')


build_sandwich('lettuce', 'tomato', 'cheese')
build_sandwich('turkey', 'bacon', 'avocado', 'mayo')
build_sandwich('peanut butter', 'jelly')
