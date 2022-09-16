from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    print(items.index(border))
    
    for x in range(border - 1):
        items.pop(0)
    return items

print('Example:')
print(remove_all_before([1, 2, 3, 4, 5], 3))