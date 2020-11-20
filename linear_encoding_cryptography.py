def encode(str,a,b):
    output_list =[]
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    for elem in str:
        num = alphabet.index(elem)
        output_list.append(a*num + b)
    return output_list

assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43]


def decode(numbers,a,b):
    chars = ''
    
    for num in numbers:
        char_index = (num-b)/a
        is_integer = (round(char_index) == char_index)
        if char_index>=0 and char_index<=26 and is_integer:
            char = ' abcdefghijklmnopqrstuvwxyz'[int(char_index)]
            chars+=char
        else:
            return False
    return chars

assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat'

message = [377,
 717,
 71,
 513,
 105,
 921,
 581,
 547,
 547,
 105,
 377,
 717,
 241,
 71,
 105,
 547,
 71,
 377,
 547,
 717,
 751,
 683,
 785,
 513,
 241,
 547,
 751]

for a in range(1,101):
    for b in range(0,101):
        decoding = decode(message,a,b)
        if decoding:
            print(a,b,decoding)
