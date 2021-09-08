class Road:

    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def massa(self, plotnost = 25, tolschina = 5):
        print(f'Масса асфальта для дороги длинной {self._lenght / 1000}км, шириной {self._width}м и толщиной '
              f'покрытия {tolschina}см при плотности {plotnost}кг/м3 будет равна {self._lenght * self._width * tolschina * plotnost / 1000}т.')

try:
    road = Road(int(input('Введитн длинну дороги в метрах: ')), int(input('Введитн ширину дороги в метрах: ')))
    road.massa()

except ValueError:
    print('Некорректные входные данные!')
