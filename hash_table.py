def hash_function(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for char in string:
        sum += alphabet.index(char)
    return sum % 5

def insert(array, key, val):
    key_bucket = hash_function(key)
    array[key_bucket].append((key, val))

def find(array, key):
    key_bucket = hash_function(key)
    for tuple in array[key_bucket]:
        if tuple[0] == key:
            return tuple[1]

print("Testing hash table...")

array = [[], [], [], [], []]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
    print("Passed")