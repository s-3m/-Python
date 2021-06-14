class Matrix:

    def __init__(self, lst_matrix):
        self.lst_matrix = lst_matrix

    def __str__(self):
        num_for_str = '\n'.join([str(el).strip('[]') for el in self.lst_matrix])
        return f'{num_for_str}'

    def __add__(self, other):
        new_list = []
        for (el, el_2) in zip(self.lst_matrix, other.lst_matrix):
            sum_lst = list(map(lambda a, b: a + b, el, el_2))
            new_list.append(sum_lst)
        return Matrix(new_list)


matrix_1 = Matrix([[1, 2, 45], [3, 4, 66]])
matrix_2 = Matrix([[3, 4, 5], [6, 8, 10]])
m_3 = Matrix([[1, 2, 4], [5, 7, 9]])
print(matrix_2 + matrix_1 + m_3)
