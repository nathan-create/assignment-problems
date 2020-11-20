def intersection(list_a, list_b):
    output_list=[]
    for char_a in list_a:
        for char_b in list_b:
            if char_a==char_b:
                output_list.append(char_a)
    return output_list    

print("testing intersection on inputs '[1,2,'a','b'], [2,3,'a']'")
assert intersection([1,2,'a','b'], [2,3,'a'])==[2,'a']
print('Passed')

def union(list_1, list_2):
    output_list = list(set(list_1) | set(list_2)) 
    return output_list 


print("testing union on inputs '[1,2,'a','b'], [2,3,'a']'")
assert union([1,2,'a','b'], [2,3,'a'])==[1,2,3,'a','b'], 'the actual output was {}'.format(union([1,2,'a','b'], [2,3,'a']))
print('Passed')