def unlist_nonrecursive(input_x):
    x = input_x
    while len(x) == 1:
        if type(x[0]) == int:
            return x[0]
            break
        else:
            x = x[0]
        
    return x

print("Testing unlist_recursive...")
assert unlist_nonrecursive([[[[1], [2,3], 4]]])==[[1], [2,3], 4], "actual output was {}".format(unlist_nonrecursive([[[[1], [2,3], 4]]]))

assert unlist_nonrecursive([[[[1]]]])==1,"actual output was {}".format(unlist_nonrecursive([[[[1]]]]))
print("Passed")



def unlist_recursive(input_x):
    
    if type(input_x) != list or len(input_x)>1:
        return input_x
    else:
        return unlist_recursive(input_x[0])

print("Testing unlist_recursive...")
assert unlist_recursive([[[[1], [2,3], 4]]])==[[1], [2,3], 4], "actual output was {}".format(unlist_recursive([[[[1], [2,3], 4]]]))

assert unlist_recursive([[[[1]]]])==1,"actual output was {}".format(unlist_recursive([[[[1]]]]))
print("Passed")