from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    if len(text) % 2:
        text += '_'
    print(text)
    result = []
    while text:
        result.append(text[:2])
        text = text[2:]
    return result


print(list(split_pairs("abc")))
