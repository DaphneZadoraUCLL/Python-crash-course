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
              f"- Age: {self.age}\n"
              f"- City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")

    def increment_login_attempts(self, n):
        self.login_attempts += n

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(Users):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, rights_list=[]):
        self.rights_list = rights_list

    def show_privileges(self):
        print("\nAdmin Privileges are:")
        for privilege in self.rights_list:
            print(f"- {privilege}")


# Voorbeeldgebruik
Daphne_admin = Admin('Daphne', 'Zadora', 36, 'Tongeren')
Daphne_admin.privileges.rights_list = [
    'can add post', 'can delete post', 'can ban user']
Daphne_admin.privileges.show_privileges()
