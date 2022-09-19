def between_markers(text: str, start: str, end: str) -> str:
    idx1 = text.index(start)
    idx2 = text.index(end)

    res = ''
    for idx in range(idx1 + len(start), idx2):
        res = res + text[idx]
    return res


print('Example:')
print(between_markers('What is >apple<', '>', '<'))
