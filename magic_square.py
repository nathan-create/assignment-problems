def col_check_help(arr):
    col_list = []
    for num in range(len(arr[0])):
        col = [arr[i][num] for i in range(len(arr))]
        col_list.append(col)
    return col_list

def diag_check_help(arr):
    top_left_diag = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                top_left_diag.append(arr[i][j])
    top_right_diag = []
    j = len(arr[0]) - 1
    for i in range(len(arr)):
        top_right_diag.append(arr[i][j])
        j -= 1
    return [top_left_diag, top_right_diag]



def is_valid(arr):
    for row in arr:
        if None not in row:
            if sum(row) != 15:
                return False
    
    for col in col_check_help(arr):
        if None in col:
            continue
        if sum(col) != 15:
            return False
    
    for diag in diag_check_help(arr):
        if None in diag:
            continue
        if sum(diag) != 15:
            return False

    return True
def create_magic_square():
    arr = [[None for num in range(3)] for num in range(3)]
    for num1 in range(1,10):
        arr = [[None for num in range(3)] for num in range(3)]
        arr[0][0] = num1
        if not is_valid(arr):
            continue

        for num2 in range(1,10):
            if num2 == num1:
                continue
            arr = [[None for num in range(3)] for num in range(3)]
            arr[0][0] = num1
            arr[0][1] = num2
            if not is_valid(arr):
                continue

            for num3 in range(1,10):
                if num3 == num1 or num3 == num2:
                    continue
                arr = [[None for num in range(3)] for num in range(3)]
                arr[0][0] = num1
                arr[0][1] = num2
                arr[0][2] = num3
                if not is_valid(arr):
                    continue

                for num4 in range(1,10):
                    if num4 == num1 or num4 == num2 or num4 == num3:
                        continue
                    arr = [[None for num in range(3)] for num in range(3)]
                    arr[0][0] = num1
                    arr[0][1] = num2
                    arr[0][2] = num3
                    arr[1][0] = num4
                    if not is_valid(arr):
                        continue

                    for num5 in range(1,10):
                        if num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                            continue
                        arr = [[None for num in range(3)] for num in range(3)]
                        arr[0][0] = num1
                        arr[0][1] = num2
                        arr[0][2] = num3
                        arr[1][0] = num4
                        arr[1][1] = num5
                        if not is_valid(arr):
                            continue

                        for num6 in range(1,10):
                            if num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
                                continue
                            arr = [[None for num in range(3)] for num in range(3)]
                            arr[0][0] = num1
                            arr[0][1] = num2
                            arr[0][2] = num3
                            arr[1][0] = num4
                            arr[1][1] = num5
                            arr[1][2] = num6
                            if not is_valid(arr):
                                continue

                            for num7 in range(1,10):
                                if num7 == num1 or num7 == num2 or num7 == num3 or num7 == num4 or num7 == num5 or num7 == num6:
                                    continue
                                arr = [[None for num in range(3)] for num in range(3)]
                                arr[0][0] = num1
                                arr[0][1] = num2
                                arr[0][2] = num3
                                arr[1][0] = num4
                                arr[1][1] = num5
                                arr[1][2] = num6
                                arr[2][0] = num7
                                if not is_valid(arr):
                                    continue

                                for num8 in range(1,10):
                                    if num8 == num1 or num8 == num2 or num8 == num3 or num8 == num4 or num8 == num5 or num8 == num6 or num8 == num7:
                                        continue
                                    arr = [[None for num in range(3)] for num in range(3)]
                                    arr[0][0] = num1
                                    arr[0][1] = num2
                                    arr[0][2] = num3
                                    arr[1][0] = num4
                                    arr[1][1] = num5
                                    arr[1][2] = num6
                                    arr[2][0] = num7                    
                                    arr[2][1] = num8
                                    if not is_valid(arr):
                                        continue

                                    for num9 in range(1,10):
                                        if num9 == num1 or num9 == num2 or num9 == num3 or num9 == num4 or num9 == num5 or num9 == num6 or num9 == num7 or num9 == num8:
                                            continue
                                        arr = [[None for num in range(3)] for num in range(3)]
                                        arr[0][0] = num1
                                        arr[0][1] = num2
                                        arr[0][2] = num3
                                        arr[1][0] = num4
                                        arr[1][1] = num5
                                        arr[1][2] = num6
                                        arr[2][0] = num7                    
                                        arr[2][1] = num8
                                        arr[2][2] = num9
                                        if not is_valid(arr):
                                            continue
                                        return arr

print('testing is_valid...')
arr1 = [[1,2,None],
        [None,3,None],
        [None,None,None]]
assert is_valid(arr1) == True

arr2 = [[1,2,None],
        [None,3,None],
        [None,None,4]] 
assert is_valid(arr2) == False

arr3 = [[1,2,None],
        [None,3,None],
        [5,6,4]] 
assert is_valid(arr3) == False

arr4 = [[None,None,None],
        [None,3,None],
        [5,6,4]] 
assert is_valid(arr4) == True
print('passed')

for row in create_magic_square():
    print(row)