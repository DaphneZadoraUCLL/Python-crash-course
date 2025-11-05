pets = {
    'Bailey': {
        'animal': 'cat',
        'owner': 'Aiden',
    },
    'Luna': {
        'animal': 'cat',
        'owner': 'Sam',
    },
    'Mina': {
        'animal': 'cat',
        'owner': 'Daphne',
    }
}
for pet_name, pet_info in pets.items():
    print(f"\nPet name: {pet_name}")
    print(f"\tType: {pet_info['animal']}")
    print(f"\tOwner: {pet_info['owner']}")
