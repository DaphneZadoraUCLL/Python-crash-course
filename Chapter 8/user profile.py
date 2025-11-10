def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'daphne', 'zadora', age='36', location='Belgium', field='ICT student')

print(user_profile)
