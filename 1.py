import time


class bcolors:
    RED = "\033[41m"
    YELLOW = "\033[43m"
    GREEN = '\033[42m'


class TrafficLight:
    __color = ['       ', '        ', '        ']

    def running(self):
        print('Светофор погнал:')
        while True:
            print(f'{bcolors.RED}{self.__color[0]}', end='')
            time.sleep(7)
            print('\r', end='')
            print(f'{bcolors.YELLOW}{self.__color[1]}', end='')
            time.sleep(2)
            print('\r', end='')
            print(f'{bcolors.GREEN}{self.__color[2]}', end='')
            time.sleep(4)
            print('\r', end='')


obj_one = TrafficLight()
obj_one.running()