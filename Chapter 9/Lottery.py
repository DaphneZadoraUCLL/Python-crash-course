from random import choice


def get_winning_ticket(winning_numbers_letters):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_number = choice(winning_numbers_letters)
        if pulled_number not in winning_ticket:
            winning_ticket.append(pulled_number)
    return winning_ticket


def check_ticket(user_ticket, winning_ticket):
    for item in user_ticket:
        if item not in winning_ticket:
            return False
    return True


def create_lottery_ticket(winning_numbers_letters):
    lottery_ticket = []
    while len(lottery_ticket) < 4:
        pulled_number = choice(winning_numbers_letters)
        if pulled_number not in lottery_ticket:
            lottery_ticket.append(pulled_number)
    return lottery_ticket


winning_numbers_letters = ['5', '9', '12', '23', '34',
                           '45', '48', '52', '58', '63', 'r', 'h', 'a', 'm']
winning_ticket = get_winning_ticket(winning_numbers_letters)
plays = 0
won = False
max_tries = 1_000_000

while not won:
    new_ticket = create_lottery_ticket(winning_numbers_letters)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
