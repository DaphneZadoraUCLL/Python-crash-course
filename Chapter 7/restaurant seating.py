guests = input("How many people are in your dinner group?  ")
guests = int(guests)

if guests > 8:
    print("Please wait until a table is available.")
else:
    print("Your table is ready")
