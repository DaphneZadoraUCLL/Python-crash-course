from Admin import Admin

Daphne = Admin('Daphne', 'Zadora', 30, 'New York')
Daphne.privileges.rights_list = [
    'can add post', 'can delete post', 'can ban user']
Daphne.privileges.show_privileges()
