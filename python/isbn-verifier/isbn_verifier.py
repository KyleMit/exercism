def is_valid(isbn: str):
    # remove all non digits except final X
    stripped = ""
    for i, c in enumerate(isbn):
        if c.isdigit():
            stripped += c
        elif i == len(isbn) - 1 and c.lower() == "x":
            stripped += c
        elif c.isalpha():
            return False

    if len(stripped) != 10:
        return False

    nums = [int(x) if x.isdigit() else 10 for x in stripped]
    multiple = range(10, 0, -1)

    check_sum = sum([a * b for a, b in zip(nums, multiple)])

    return check_sum % 11 == 0
