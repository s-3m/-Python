class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return f'Cell ({self.num + other.num})'

    def __sub__(self, other):
        return f'Cell ({self.num - other.num})' if self.num - other.num > 0 else f'Клетка не может создаться'

    def __mul__(self, other):
        return f'Cell ({self.num * other.num})'

    def __truediv__(self, other):
        return f'Cell ({int(self.num / other.num)})'

    def make_order(self, num_of_cell):
        count = self.num
        while count > 0:
            if count >= num_of_cell :
                print('*' * num_of_cell)
                count -= num_of_cell
            else:
                print('*' * count)
                count -= count




a = Cell(34)
b = Cell(7)
print(a.make_order(5))
