def find_min(number_list):
    lowest_num = number_list[0]
    for num in number_list:
        if num < lowest_num:
            lowest_num = num
    return lowest_num

def tally_sort(num_list):
    min_num = find_min(num_list)
    ind_list = []
    sorted_list = []
    filler_list = []
    for num in range(len(num_list)):
        num_list[num]-=min_num
        ind_list.append(0)
    print(num_list)
    print(ind_list)
    for ind in range(len(ind_list)):
        for num in range(len(num_list)):
            if ind == num_list[num]:
                ind_list[ind]+=1
    for tallies in range(len(ind_list)):
        if ind_list[tallies] > 0:
            for num in range(ind_list[tallies]):
                sorted_list.append(ind_list.index(ind_list[tallies]))



            
            
    print(num_list)
    print(ind_list)
    print(sorted_list)
        
        
    
tally_sort([2, 5, 2, 3, 8, 6, 3])
