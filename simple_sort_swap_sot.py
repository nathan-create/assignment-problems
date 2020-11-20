def minimum(num_list):
    lowest_num=1000
    for elem in num_list:
        if elem<lowest_num:
            lowest_num=elem
    return lowest_num


def simple_sort(num_list):
    sorted_list=[]
    while len(num_list)>0:
        lowest_num=minimum(num_list)    
        num_list.remove(lowest_num)
        sorted_list.append(lowest_num)
    return sorted_list
    
print("testing simple_sort")
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])==[-5,0,2,2,2,2,3,3.14,4,5,8] , "Actual out put is {}".format(simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))
print("Passed")

def swap_sort(num_list):
    list_length=len(num_list)
    for elem in range(list_length-1):
        for new_elem in range(list_length-elem-1):
            if num_list[new_elem]>num_list[new_elem+1]:
                num_list[new_elem], num_list[new_elem+1] = num_list[new_elem+1], num_list[new_elem]
    return num_list

print("testing swap_sort")
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2])==[-5,0,2,2,2,2,3,3.14,4,5,8], "Actual output is {}".format(swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))
print("Passed")

    