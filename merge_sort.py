def merge(x,y):
    sorted_list = []
    numx = 0
    numy = 0
    while numx < len(x) and numy <len(y):
        if x[numx] < y[numy]:
            sorted_list.append(x[numx])
            numx+=1
        else:
            sorted_list.append(y[numy])
            numy+=1
    sorted_list+= x[numx:] + y[numy:]
    return sorted_list

assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7], merge([-2,1,4,4,4,5,7],[-1,6,6])


def merge_sort(x):
    if len(x) != 1:
        mid = len(x)//2
        left = x[:mid]
        right = x[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left,right)
        return result
    else:
        return x

print("Testing merge sort")
assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8]
print("passed")