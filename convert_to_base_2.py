import math
def convert_to_base_2(decnum):
    subtract_num=0
    num_list=[]
    highest_power = math.floor(math.log2(decnum))
    new_num = decnum-decnum**highest_power
    for i in range(math.floor(math.log2(decnum))+1):
        num_list.append('0')
        num_list[0]='1'
    for num in num_list[::-1]:
        if 2**num_list.index(num) <= new_num and type(2**num_list.index(num))==int:
            new_num-=2**num_list.index(num)
            print(new_num)
            num_list[num_list.index(num)]='1'
            print(num_list)
        else:
            num_list[num_list.index(num)]='0'
    for i in num_list:
        if i =='0':
            i='1'
        else:
            i=='1'
    return num_list

print(convert_to_base_2(19))
