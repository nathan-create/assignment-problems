string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
lists = string.split('\n')
strings = [x.split(',') for x in lists]

output_arr = []
for string in strings:
  newstring = []
  if len(string) > 0:
    for char in string:
      if char[0]=='"' and char[-1]=='"':
        char = char[1:-1]
      elif '.' in char:
        char = float(char)
      else:
        char = int(char)
      newstring.append(char)
    output_arr.append(newstring)
print(output_arr)