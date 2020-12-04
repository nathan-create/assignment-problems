def cartesian_product(arrs):
    result = []
    for arr in arrs:
        for val in arr:
            if arr.index(val) == 0:
                result.append([val])
            else:
                for point in result:
                    point.append(val)
    return result        

print(cartesian_product([['a'], [1,2,3], ['Y','Z']]))