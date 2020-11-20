def insert_element_into_sorted_list(element, sorted_list):
    for elem in range(len(sorted_list)):
        if sorted_list[elem]>element:
            break_point = elem
            break
    sorted_list=sorted_list[:break_point]+[element]+sorted_list[break_point:]
    return sorted_list


def card_sort(num_list):
    sorted_list=[]
    for num in range(len(num_list)):
        sorted_list=insert_element_into_sorted_list(num_list[num],sorted_list)
    return sorted_list
print(card_sort([5,6,11,12,13]))