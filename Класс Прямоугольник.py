"""Разработайте класс Rectangle.

При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).

Класс должен реализовывать методы:

perimeter — возвращает периметр прямоугольника;
area — возвращает площадь прямоугольника.
get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
get_size() — возвращает размеры в виде кортежа;
move(dx, dy) — изменяет положение на заданные значения;
resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
Все результаты вычислений нужно округлить до сотых."""

import math


class Rectangle:

    def __init__(self, a_point, b_point):
        self.a_point = a_point
        self.b_point = b_point

    def perimeter(self):
        return round(2 * (math.fabs(self.a_point[0] - self.b_point[0]) +
                          math.fabs(self.a_point[1] - self.b_point[1])), 2)

    def area(self):
        return round(math.fabs(self.a_point[0] - self.b_point[0]) *
                     math.fabs(self.a_point[1] - self.b_point[1]), 2)

    def get_pos(self):
        x_min = round(min(self.a_point[0], self.b_point[0]), 2)
        y_max = round(max(self.a_point[1], self.b_point[1]), 2)
        return (x_min, y_max)

    def get_size(self):
        widht = round(abs(self.a_point[0] - self.b_point[0]), 2)
        height = round(abs(self.a_point[1] - self.b_point[1]), 2)
        return (widht, height)

    def move(self, dx, dy):
        self.a_point = (self.a_point[0] + dx, self.a_point[1] + dy)
        self.b_point = (self.b_point[0] + dx, self.b_point[1] + dy)
        return (self.a_point, self.b_point)

    def resize(self, width, height):
        x_min = min(self.a_point[0], self.b_point[0])
        y_max = max(self.a_point[1], self.b_point[1])
        self.a_point = (x_min, y_max - height)
        self.b_point = (x_min + width, y_max)
        return (self.a_point, self.b_point)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())

