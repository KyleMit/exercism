from collections import Counter

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
        cnt = Counter(dice)
        if len(cnt) != 2:
            return 0
        first, second = cnt.most_common(2)
        return sum(dice) if first[1] == 3 and second[1] == 2 else 0
    if category == CHOICE:
        return sum(dice)
    if category == FOUR_OF_A_KIND:
        cnt = Counter(dice)
        die, qty = cnt.most_common()[0]
        return die * 4 if qty >= 4 else 0
    if category == LITTLE_STRAIGHT:
        return (
            30
            if longestConsecutiveSubsequence(dice) == 5 and sorted(dice)[0] == 1
            else 0
        )
    if category == BIG_STRAIGHT:
        return (
            30
            if longestConsecutiveSubsequence(dice) == 5 and sorted(dice)[0] == 2
            else 0
        )
    return 0


def longestConsecutiveSubsequence(xs):
    uniques = list(set(sorted(xs)))

    longestRun = 0
    currentRun = 0

    for i, el in enumerate(uniques):
        if i == 0:
            currentRun = 1
        elif el == uniques[i - 1] + 1:
            currentRun += 1
        else:
            currentRun = 1

        longestRun = max(longestRun, currentRun)

    return longestRun
