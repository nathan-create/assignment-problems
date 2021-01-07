def get_children(val, pair_list):
    result = []
    for pair in pair_list:
        if pair[0] == val:
            result.append(pair[1])
    return result

def get_parents(val, pair_list):
    result = []
    for pair in pair_list:
        if pair[1] == val:
            result.append(pair[0])
    return result

def get_roots(pair_list):
    parents = []
    for pair in pair_list:
        if pair[0] not in parents:
            parents.append(pair[0])    
    for parent in parents:
        children_count = 0
        for pair in pair_list:
            if parent == pair[1]:
                children_count+=1
        if children_count == 0:
            return ['{}'.format(parent)]

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
print("Testing get_children")
assert get_children('e',edges) == ['g', 'i', 'a']
assert get_children('c',edges) == []
assert get_children('f',edges) == ['h']
print("Passed")
print("Testing get_parents")
assert get_parents('e',edges) == []
assert get_parents('c',edges) == ['a']
assert get_parents('f',edges) == ['d']
print("Passed")
print("Testing get_roots")
assert get_roots(edges) == ['e']
print("Passed")