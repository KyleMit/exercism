def is_isogram(text: str):
    chars = set()
    for c in text.lower():
        if not c.isalpha():
            continue
        if c in chars:
            return False
        chars.add(c)

    return True
