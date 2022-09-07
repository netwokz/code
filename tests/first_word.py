

def first_word(text: str) -> str:
    words = text.split()
    # print(words)
    return words[0]


assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

first_word("Hello world")
