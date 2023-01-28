def is_pangram(sentence):
    stripped = [i for i in sentence.lower() if i.isalpha()]
    return len(set(stripped)) == 26
