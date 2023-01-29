import math


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = sum(divisors(number))

    if aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number or aliquot_sum == 1:
        return "deficient"
    else:
        return "perfect"


def divisors(n):
    divs = [1]
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    return list(set(divs))


classify(1)
