def square(number):
    return 2 ** (number -1)


def total():
    sum = 0
    for i in range(1, 17):
        sum += square(i)
    return sum
