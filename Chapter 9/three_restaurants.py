class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


my_restaurant = Restaurant('Panda wok', 'Chinese')
my_restaurant.describe_restaurant()

restaurant2 = Restaurant('Olive Garden', 'Italian')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Taco Bell', 'Mexican')
restaurant3.describe_restaurant()
