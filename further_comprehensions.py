def tester_function(n):
    result = [[(1 if row_index == col_index else 0) for row_index in range(n)] for col_index in range(n)]

    result2 = []
    for num in range(20):
        x = num
        result2.append(x)
    print(result2)    
    return result

       
def identity_matrix_elements(n):
    return [[(1 if row_index == col_index else 0) for row_index in range(n)] for col_index in range(n)]

assert identity_matrix_elements(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

def counting_across_rows_matrix_elements(m,n):
    return [[(4*col_index + row_index + 1) for row_index in range(n)] for col_index in range(m)]

assert counting_across_rows_matrix_elements(3,4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], "actual output was {}".format(counting_across_rows_matrix_elements(3,4))
print("Passed")