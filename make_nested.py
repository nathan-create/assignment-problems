def make_nested(dct):
    result = dict()
    vals=dct.values()
    list_vals=list(vals)
    keys=[]
    inner_dict1=dict()
    inner_dict2=dict()
    for key_loop in dct:
        key1 = key_loop.split("_")
        keys.append(key1)
        for i in range(len(keys)):
            desig_val=list_vals[i]
            desig_key=keys[i][1]
            if keys[i][0]==keys[0][0]:
                inner_dict1[desig_key]=desig_val
            else:
                inner_dict2[desig_key]=desig_val
    result['animal']=inner_dict1
    result['food']=inner_dict2
    return result 





colors = {'animal_bumblebee': ['yellow', 'black'],
'animal_elephant': ['gray'],
'animal_fox': ['orange', 'white'],
'food_apple': ['red', 'green', 'yellow'],
'food_cheese': ['white', 'orange']
}
print("testing make_nested...")
assert make_nested(colors)=={'animal': {'bumblebee': ['yellow', 'black'],'elephant': ['gray'],'fox': ['orange','white']},'food': {'apple': ['red', 'green', 'yellow'],'cheese': ['white', 'orange']}},'actual output was {}'.format(make_nested(colors))
print("passed")