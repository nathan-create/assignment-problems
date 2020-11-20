def skip_factorial_nonrecursive(n):
    product = 1
    for elem in range(n,1,-2):
        product *=elem
    return product

print("Testing skip_factorial_nonrecursive")
assert skip_factorial_nonrecursive(6)==48
assert skip_factorial_nonrecursive(7)==105
print("Passed")


def skip_factorial_recursive(n):
    if n <= 1:
        return 1
    return n*skip_factorial_recursive(n-2)

print("Testing skip_factorial_recursive")
assert skip_factorial_nonrecursive(6)==48
assert skip_factorial_nonrecursive(7)==105
print("Passed")