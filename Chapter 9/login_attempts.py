class Users:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:\n{'-' * 20}\n"
              f"- Name: {self.first_name} {self.last_name}\n"
              f"- age: {self.age}\n"
              f"- City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")

    def inrcrement_login_attempts(self, n):
        """Increment the number of login attempts by 1."""
        self.login_attempts += n

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0


user1 = Users('John', 'Doe', 28, 'New York')
user1.inrcrement_login_attempts(2)
print(f"Login attempts: {user1.login_attempts}")
user1.inrcrement_login_attempts(3)
print(f"Login attempts: {user1.login_attempts}")
user1.inrcrement_login_attempts(1)
print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
