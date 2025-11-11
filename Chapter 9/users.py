class Users:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"User Information:\n{'-' * 20}\n"
              f"- Name: {self.first_name} {self.last_name}\n"
              f"- age: {self.age}\n"
              f"- City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")


user1 = Users('John', 'Doe', 28, 'New York')
user1.describe_user()
user1.greet_user()

user2 = Users('Jane', 'Smith', 34, 'Los Angeles')
user2.describe_user()
user2.greet_user()

user3 = Users('Emily', 'Johnson', 22, 'Chicago')
user3.describe_user()
user3.greet_user()
