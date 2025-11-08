sandwich_orders = ['kaas', 'pastrami', 'ham',
                   'vegetarisch', 'pastrami', 'tonijn', 'kip', 'pastrami']
finished_sandwiches = []

print("We apologize, but we have run out of pastrami today.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} sandwich is being prepared.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been prepared:")
print(f"{', '.join(finished_sandwiches)}")
