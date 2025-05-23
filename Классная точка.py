"""Разработайте класс Point, который при инициализации принимает координаты точки на декартовой плоскости и сохраняет их
в поля x и y соответственно.
Реализуйте методы:
    move, который перемещает точку на заданное расстояние по осям x и y;
    length, который определяет до переданной точки расстояние, округлённое до сотых."""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def move(self, bias_x, bias_y):
        self.x += bias_x
        self.y += bias_y
        return self.x, self.y

    def length(self, object):
        self.distance = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
        return round(self.distance, 2)


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))