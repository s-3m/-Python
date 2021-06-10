class Stationery:


    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


all = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
all.draw()
pen.draw()
pencil.draw()
handle.draw()
