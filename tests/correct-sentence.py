def correct_sentence(text: str) -> str:
    print(text)
    fixed = text[0].upper() + text[1:]
    if fixed[-1] != ".":
        fixed += "."
    return fixed


print('Example:')
print(correct_sentence("greetings, friends"))
