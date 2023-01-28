def response(hey_bob: str):
    trimmed = hey_bob.strip()
    isEmpty = trimmed == ""
    isQuestion = trimmed.endswith("?")
    isYelling = hey_bob.isupper()
    if isEmpty:
        return "Fine. Be that way!"
    elif isQuestion and isYelling:
        return "Calm down, I know what I'm doing!"
    elif isQuestion:
        return "Sure."
    elif isYelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."
