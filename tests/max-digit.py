def max_digit(a: int) -> int:
    # your code here
    num = list(str(a))
    print(num)
    max_ = max(num)
    return int(max_)


print('Example:')
print(max_digit(10))
