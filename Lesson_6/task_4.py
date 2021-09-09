from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.car_speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{str(self.color).title()} {self.name} starts!')
        pass

    def stop(self):
        print(f'{str(self.color).title()} {self.name} stops!')

    def turn(self):
        print(f'{str(self.color).title()} {self.name} turns to the {choice(["North", "East", "South", "West"])}.')

    def speed(self):
        print(f'{str(self.color).title()} {self.name} goes with speed {str(self.car_speed)}.' if self.is_police == False
              else f'{str(self.color).title()} police {self.name} goes with speed {str(self.car_speed)}.')


class TownCar(Car):

    def speed(self):
        if self.car_speed <= 60:
            super().speed()
        else:
            print(f'It is terrible!!!{str(self.color).title()} {self.name} goes with speed {str(self.car_speed)}!!!')


class SportCar(Car):
    def speed(self):
        if self.car_speed <= 110:
            super().speed()
        else:
            print(f'It is wonderfull!!!{str(self.color).title()} {self.name} goes with speed {str(self.car_speed)}!!!')


class WorkCar(Car):
    def speed(self):
        if self.car_speed <= 60:
            super().speed()
        else:
            print(f'It is terrible!!!{str(self.color).title()} {self.name} goes with speed {str(self.car_speed)}!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def speed(self):
        if self.car_speed <= 60:
            super().speed()
        else:
            print(f'Make way!!!{str(self.color).title()} police {self.name} with flashing '
                                           f'lights is hurry to call with speed {str(self.car_speed)}!!!')


car_1 = TownCar(70, 'orange', 'BMW X5')
car_2 = SportCar(250, 'red', 'Bugatti Veiron')
car_3 = WorkCar(35, 'grey', 'Ford Transporter')
car_4 = PoliceCar(80, 'white', 'Shkoda Octavia')

cars = [car_1, car_2, car_3, car_4]

for i in cars:
    i.go()
    i.car_speed = 35
    i.speed()
    i.turn()
    i.car_speed = 80
    i.speed()
    i.stop()
    print()
