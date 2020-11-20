def update_bounds(bounds):
    midpoint = (bounds[0]+bounds[1])/2
    if midpoint**2 <= 2:
        return [midpoint, bounds[1]]
    else:
        return [bounds[0], midpoint]
print("testing update_bounds")
assert update_bounds([1, 2]) == [1, 1.5]
assert update_bounds([1, 1.5]) == [1.25, 1.5]
print("Passed")

def estimate_root(precision):
    bounds = [1, 2]
    while bounds[1]-bounds[0] >= precision:
        bounds = update_bounds(bounds)
    return (bounds[0]+bounds[1])/2

print("testing estimate_root")
assert estimate_root(0.1) == 1.40625
print("Passed")