guests = ["Sam", "Myriam", "Romain", "Cynthia"]
print(f"Hello {guests[0]}, please join dinner")
print(f"Hello {guests[1]}, please join dinner")
print(f"Hello {guests[2]}, please join dinner")
print(f"Hello {guests[3]}, please join dinner")

print(f"It seems {guests[3]} can't make it.")

guests.remove("Cynthia")
guests.insert(3, "Karen")

print(f"Hello {guests[0]}, please join dinner")
print(f"Hello {guests[1]}, please join dinner")
print(f"Hello {guests[2]}, please join dinner")
print(f"Hello {guests[3]}, please join dinner")
