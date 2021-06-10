from random import randint


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self):
        rand_number = randint(1, 10)
        if rand_number % 2 == 0:
            print(f'Машина {self.name} поаернула направо.')
        else:
            print(f'Машина {self.name} поаернула налево.')

    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')
        if self.speed > 60:
            print(f'Вы привысили скорость на {self.speed - 60}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Ваша текущая скорость {self.speed}')
        if self.speed > 40:
            print(f'Вы привысили скорость на {self.speed - 40}')


class PoliceCar(Car):
    def police_go(self):
        if self.is_police:
            print(f'{self.name} преследует преступника:', 'Виу-' * 10 + 'Виу')


first_town_car = TownCar(100, 'Белая', 'Ford')
police_car = PoliceCar(200, 'Black', 'Police car', is_police=True)
first_town_car.show_speed()
first_town_car.go()
first_town_car.turn()
first_town_car.turn()
first_town_car.turn()
first_town_car.turn()
first_town_car.stop()
police_car.police_go()
