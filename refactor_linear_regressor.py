def calculate_coefficients(self):
    final_dict = {}
    matrix = [[1 for x in list(self.df.data_dict.values())[0][0]]]
    matrix_dict = {}
    for key in self.df.data_dict:
        if key != self.dependent_variable:
            matrix_dict[key] = self.df.data_dict[key]
    for row in range(len(matrix_dict)):
        matrix.append(list(self.df.data_dict.values()))
    matrix = Matrix(matrix)
    matrix = matrix.transpose()
    matrix_t = matrix.transpose()
    matrix_mult = matrix_t.matrix_multiply(matrix)
    matrix_inv = matrix_mult.inverse()
    matrix_pseudo_inv = matrix_inv.matrix_multiply(matrix_t)
    multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
    multiplier_matrix = matrix_pseudo_inv.matrix_multiply(Matrix(multiplier))
    for num in range(len(multiplier_matrix.elements)):
        if num == 0:
            key == 'constant'
        else:
            key = list(self.df.data_dict.keys())[num-1]
        final_dict[key] = [row[0] for row in multiplier_matrix.elements][num]
    return final_dict