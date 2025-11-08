responses = {}
active = True

while active:
    name_prompt = input("What is your name? ")
    location_prompt = input(
        "If you could visit one place in the world, where would you go? ")

    responses[name_prompt] = location_prompt

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        active = False

print("\n--- Poll Results ---")
for name, location in responses.items():
    print(f"{name} would like to visit {location}.")
