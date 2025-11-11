import restaurant

Melone = restaurant.IceCreamStand('Melone')
Melone.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Pistache']
Melone.describe_restaurant()
print("Available flavors:")
Melone.display_flavors()

channel_club = restaurant.Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()
