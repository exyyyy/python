from time import sleep
from itertools import cycle


class TrafficLight:
    __color = [['\033[30m\033[41m{}\033[0m'.format("red"), 7], ['\033[30m\033[43m{}\033[0m'.format("yellow"), 2],
               ['\033[30m\033[42m{}\033[0m'.format("green"), 5]]

    def works(self):
        for light in cycle(self.__color):
                print(f'\r{light[0]}', end='')
                sleep(light[1])


svetofor = TrafficLight()

svetofor.works()
