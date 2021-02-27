from random import randint, seed

class Dice:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        seed()

    def roll(self):
        roll_value = randint(1, self.number_of_sides)
        return roll_value


def main():
    six_sided = Dice(6)
    print(six_sided.number_of_sides)
    six_sided_2nd_die = Dice(6)
    double_count = 0
    number_of_rolls = 100000
    for roll in range(number_of_rolls):
        roll_value = six_sided.roll()
        roll_value2 = six_sided_2nd_die.roll()
        print(roll_value,roll_value2)
        if roll_value == roll_value2:
            print("double!")
            double_count += 1

    print("Doubles were found ", double_count / number_of_rolls)


if __name__ == "__main__":
    main()


