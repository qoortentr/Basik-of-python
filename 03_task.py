class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num >= other.num:
            return self.num - other.num
        else:
            raise ValueError("!!!Уменьшаемое меньше вычитаемого!!!")

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

    def __floordiv__(self, other):
        return self.num // other.num

    def make_order(self, num_row):
        arr = [("*" * num_row + '\\n') * (self.num // num_row) + "*" * (self.num % num_row)]
        if self.num % num_row == 0:
            arr = arr[0][0:len(arr) - 3]
        return arr


cell_1 = Cell(20)
cell_2 = Cell(18)

print(cell_2)

print("".join(cell_1.make_order(5)))

print("Сложение:", f"{cell_2} + {cell_1} =", cell_2 + cell_1)
print("Вычитание:", f"{cell_1} - {cell_2} =", cell_1 - cell_2)
print("Умножение:", f"{cell_1} * {cell_2} =", cell_1 * cell_2)
print("Деление:", f"{cell_1} / {cell_2} =", (cell_1 / cell_2))
print("Целочисленное деление:", f"{cell_1} // {cell_2} =", cell_1 // cell_2)


