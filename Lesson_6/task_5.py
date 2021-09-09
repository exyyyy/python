class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'You are drawing with the something stationery.')


class Pen(Stationery):
    def draw(self):
        print(f'You are drawing with the {self.title} pen.')


class Pencil(Stationery):
    def draw(self):
        print(f'You are drawing with the {self.title} pencil.')


class Handle(Stationery):
    def draw(self):
        print(f'You are drawing with the {self.title} handle.')


list_1 = [Stationery('something'), Pen('black'), Pencil('grey'), Handle('yellow')]

for i in list_1:
    i.draw()
