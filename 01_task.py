class Matrix:
    def __init__(self, list_list):
        self.list = list_list

    def __str__(self):
        return f"{self.list}"

    def __add__(self, other):
        item = [[int(self.list[line][num]) + int(other.list[line][num]) for num in range(len(self.list[line]))] for line
                in range(len(self.list))]
        return item

    def output(self):
        for i in self.list:
            print("|", *i, "|")


matrix_1 = Matrix([[21, 5], [3, 54], [56, 67]])
matrix_2 = Matrix([[79, 95], [97, 46], [44, 33]])

matrix_1.output()
print(matrix_1)
print(matrix_1 + matrix_2)
