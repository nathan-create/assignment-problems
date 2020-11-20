def even_odd_tuples(num_list):
   # output_list=[]
   # for num in num_list:
   #     if num%2==0:
   #         output_list.append((num,"even"))
   #     else:
   #         output_list.append((num,"odd"))
   # return output_list
   return[ (num,"even") if num%2==0 else (num,"odd") for num in num_list ]

print("testing even_odd_tuples on input'[1,2,3,5,8,11]")
assert even_odd_tuples([1,2,3,5,8,11])==[(1,'odd'),(2,'even'),(3,'odd'),(5,'odd'),(8,'even'),(11,'odd')]
print('Passed')


def even_odd_dict(num_list):
    #output_dict={}
    #for num in num_list:
    #    if num%2==0:
    #        output_dict[num]="even"
    #    else:
    #        output_dict[num]="odd"
    #return output_dict
    return {num: "even" if num % 2 == 0 else "odd" for num in num_list}

print("testing even_odd_dict on input '[1,2,3,5,8,11]'")
assert even_odd_dict([1,2,3,5,8,11])=={
    1:'odd',
    2:'even',
    3:'odd',
    5:'odd',
    8:'even',
    11:'odd'
}
print('Passed')