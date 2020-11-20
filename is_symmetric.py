def is_symmetric(input_string):
    output_string=input_string[::-1]
    if output_string==input_string:
        return True
    else:
        return False
    
    
  

print("Testing is_symmetric on input 'racecar'")
assert is_symmetric('racecar')==True, "The entered string is not symmetrical"
print('Passed')

print("Testing is_symmetric on input 'batman'")
assert is_symmetric('batman')==True, "The entered string is not symmetrical"
print('Passed')