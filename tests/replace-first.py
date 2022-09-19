from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    print(items)
    if len(items) > 1:
        print(len(items))
        temp = items.pop(0)
        items.append(temp)
    return items


print("Example:")
print(list(replace_first([1, 2, 3, 4])))
