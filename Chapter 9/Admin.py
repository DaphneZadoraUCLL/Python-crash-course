from users import Users


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
