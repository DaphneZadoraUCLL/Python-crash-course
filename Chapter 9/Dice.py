from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides on the die."""
        return randint(1, self.sides)


# Example usage:
die6 = Die()  # Default 6-sided die
die10 = Die(10)  # 10-sided die
die20 = Die(20)  # 20-sided die
print("Rolling a 6-sided die:", die6.roll_die())
print("Rolling a 10-sided die:", die10.roll_die())
print("Rolling a 20-sided die:", die20.roll_die())
