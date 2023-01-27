def is_armstrong_number(number):
    digits = [int(i) for i in str(number)]
    length = len(digits)
    armstrongSum = sum([i**length for i in digits])
    return number == armstrongSum
