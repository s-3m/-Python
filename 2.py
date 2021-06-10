class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_road_cover(self):
        formula = int((self._width * self._length * 25 * 5) / 1000)
        print(f'Необходимо {formula} т.')


my_road = Road(2000, 5)
my_road.calc_road_cover()
