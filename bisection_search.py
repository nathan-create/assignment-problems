import math

def bisection_search(entry, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    midpoint = math.floor((low + high) / 2)
    while sorted_list[midpoint] != entry:
        if sorted_list[midpoint] < entry:
            low = midpoint + 1
            midpoint = math.floor((low + high) / 2)

        elif sorted_list[midpoint] > entry:
            high = midpoint - 1
            midpoint = math.floor((low + high) / 2)
    return midpoint

print("Testing bisection search...")
assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9
print("Passed")