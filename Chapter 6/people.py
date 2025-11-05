users = []
user_1 = {'name': 'Aiden', 'last_name': 'Stevens',
          'age': '4', 'city': 'Tongeren', }
user_2 = {'name': 'Daphne', 'last_name': 'Zadora',
          'age': '36', 'city': 'Tongeren', }
user_3 = {'name': 'Sam', 'last_name': 'Stevens',
          'age': '34', 'city': 'Tongeren', }

users.append(user_1)
users.append(user_2)
users.append(user_3)

for user in users:
    print(f"\nName: {user['name']} {user['last_name']}")
    print(f"\tAge: {user['age']}")
    print(f"\tCity: {user['city']}")
