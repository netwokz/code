def nearest_value(values: set, one: int) -> int:
    nums = list(values)
    return nums[min(range(len(nums)), key=lambda i: abs(nums[i]-one))]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({0, -2}, -1))

assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5 
