def convert_to_numbers(string):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    num_list = []
    for char in string:
        num = alphabet.index(char)
        num_list.append(num)
    return num_list

actual_output=convert_to_numbers('a cat')
desired_output=[1,0,3,1,20]

print("testing convert_to_numbers on input 'a cat'")
assert convert_to_numbers('a cat')==[1,0,3,1,20], "the actual output {} does not match the desired output {}".format(actual_output, desired_output)
print('Passed')


def convert_to_letters(num_list):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    output_string=""
    for num in num_list:
        letter=alphabet[num]
        output_string+=letter
    return output_string

print("testing convert_to_letters on input '[1,0,3,1,20]'")
assert convert_to_letters([1,0,3,1,20])=="a cat", 'the test did not pass'
print('Passed')



