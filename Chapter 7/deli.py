sandwich_orders = ['kaas', 'ham', 'vegetarisch', 'tonijn', 'kip']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} sandwich is being prepared.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been prepared:")
print(f"{', '.join(finished_sandwiches)}")
