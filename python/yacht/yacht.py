# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    if category == ONES:
        return sum([i for i in dice if i == 1])
    if category == TWOS:
        return sum([i for i in dice if i == 2])
    if category == THREES:
        return sum([i for i in dice if i == 3])
    if category == FOURS:
        return sum([i for i in dice if i == 4])
    if category == FIVES:
        return sum([i for i in dice if i == 5])
    if category == SIXES:
        return sum([i for i in dice if i == 6])
    if category == FULL_HOUSE:
        return sum(dice) if (len(set(dice))) == 2 else 0
    if category == CHOICE:
        return sum(dice)
    return 0
