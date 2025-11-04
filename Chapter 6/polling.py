favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

participants = ['jen', 'sarah', 'edward', 'phil', 'luke', 'anna']

for person in participants:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")
