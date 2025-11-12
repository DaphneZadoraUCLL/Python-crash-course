from pathlib import Path

path = Path('Guest.txt')

guest_name = input("Enter your name: ")
path.write_text(guest_name)
