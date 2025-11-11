class Restaurant:
    """"A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, n):
        """Set the number of customers served to a specific value."""
        self.number_served = n

    def increment_number_served(self, n):
        """Increment the number of customers served by n."""
        self.number_served += n


restaurant = Restaurant('Panda wok', 'Chinese')
restaurant.set_number_served(3)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(4)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Number of customers served: {restaurant.number_served}")
