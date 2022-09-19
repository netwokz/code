def beginning_zeros(a: str) -> int:
    nums = list(str(a))
    count = 0
    for num in nums:
        if num == '0':
            count += 1
        else:
            break
    return count


print('Example:')
print(beginning_zeros('10'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4
