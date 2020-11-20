def count_characters(input_string):
    chars = "abcdefghijklmnopqrstuvwxyz"

    count = {}
    new_input=input_string.lower()
    for s in new_input:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count

print("testing count_characters on input 'A cat!!!'")
assert count_characters('A cat!!!')=={'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}, "The actual output was {} while the desired output was {}".format(count_characters('A cat!!!'),{'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3})
print('Passed')
