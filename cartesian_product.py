def cartesian_product(arrs):
    points=[[]]
    for arr in arrs:
        for val in arr:
            for point in points:
                point.append(val)
    return points     

print(cartesian_product([['a'], [1,2,3], ['Y','Z']]))