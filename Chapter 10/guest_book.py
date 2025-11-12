from pathlib import Path

path = Path('guest_book.txt')
all_names = path.read_text() if path.exists() else ''

while True:
    guest_name = input("Enter your name (or press q to stop): ")
    if guest_name == 'q':
        break
    else:
        all_names += guest_name + '\n'
        path.write_text(all_names)
