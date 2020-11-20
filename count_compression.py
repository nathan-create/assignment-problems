def count_compression(string):
    output = []
    character = string[0]
    times = 0
    for char in string:
        if char == character:
            times+=1
        else:
            output.append((character, times))
            character = char
            times = 1
    output.append((character, times))
            

    return output

print("Testing compression...")
assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)], count_compression('22344444')
print("Passed")

def count_decompression(compressed_string):
    output_str = ''
    for group in range(len(compressed_string)):
        output_str += compressed_string[group][0] * compressed_string[group][1]
    return output_str

print('testing decompression...')
assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa'
assert count_decompression([('2',2), ('3',1), ('4',5)]) == '22344444'
print("Passed")