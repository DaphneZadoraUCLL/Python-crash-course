while True:
    try:
        number_one = input("Please enter a number (Or 'q' to quit): ")
        if number_one.lower() == 'q':
            break

        number_two = input("Please choose a second number (Or 'q' to quit): ")
        if number_two.lower() == 'q':
            break

        result = int(number_one) + int(number_two)
        print(f"The sum is: {result}")
    except ValueError:
        print("Only numbers will work")
