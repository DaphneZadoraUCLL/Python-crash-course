guests = ["Sam", "Myriam", "Romain", "Cynthia"]
print(f"Hello {guests[0]}, please join dinner")
print(f"Hello {guests[1]}, please join dinner")
print(f"Hello {guests[2]}, please join dinner")
print(f"Hello {guests[3]}, please join dinner")

print(f"It seems we found a bigger table so we can invite some more guests")
guests.insert(0, "Aiden")
guests.insert(3, "Karen")
guests.append("Ester")

print(f"Hello {guests[0]}, please join dinner")
print(f"Hello {guests[1]}, please join dinner")
print(f"Hello {guests[2]}, please join dinner")
print(f"Hello {guests[3]}, please join dinner")
print(f"Hello {guests[4]}, please join dinner")
print(f"Hello {guests[5]}, please join dinner")
print(f"Hello {guests[6]}, please join dinner")

print("Our table won't be delivered in time, sadly we can only accept 2 guets")

uninvited = guests.pop()
print(f"I'm so sorry {uninvited}, maybe next time")
uninvited = guests.pop()
print(f"I'm so sorry {uninvited}, maybe next time")
uninvited = guests.pop()
print(f"I'm so sorry {uninvited}, maybe next time")
uninvited = guests.pop()
print(f"I'm so sorry {uninvited}, maybe next time")
uninvited = guests.pop()
print(f"I'm so sorry {uninvited}, maybe next time")


print(f"Hello {guests[0]}, please join dinner")
print(f"Hello {guests[1]}, please join dinner")

del guests[0]
del guests[0]

print(guests)
