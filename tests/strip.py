def end_zeros(a: int) -> int:
    # your code here
    var = str(a)
    print(var)
    small = var.strip("0")
    print(small)
    return len(var) - len(small)


print("Example:")
print(end_zeros(10))