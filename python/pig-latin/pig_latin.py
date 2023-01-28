import re


def translate(text: str):
    words = [pigLatinify(w) for w in text.split(" ")]
    return " ".join(words)


def pigLatinify(word: str) -> str:
    vowelSounds = ("a", "e", "i", "o", "u", "yt", "yr", "xr")
    startsWithVowelSound = word.lower().startswith(vowelSounds)
    if startsWithVowelSound:
        return word + "ay"

    # https://regexr.com/7731m
    pattern = (
        "(qu|sch|ch|rh|thr|th|b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)(qu)?(y)?(.*)"
    )
    m = re.match(pattern, word)
    if m:
        consanant = m[1]
        qu = m[2] or ""
        y = m[3] or ""
        rest = m[4]
        word = f"{y}{rest}{consanant}{qu}ay"
        return word
