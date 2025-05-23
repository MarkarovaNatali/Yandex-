import math


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        self.p = 2 * (math.fabs(self.x[0] - self.y[0]) + math.fabs(self.x[1] - self.y[1]))
        return round(self.p, 2)

    def area(self):
        self.a = math.fabs(self.x[0] - self.y[0]) * math.fabs(self.x[1] - self.y[1])
        return round(self.a, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.perimeter())
print(rect.area())
