import math

# ДЗ 6. Протоколи, наслідування, поліморфізм

from colors import bcolors

class frange:

    def __init__(self, A, L=None, D=None):
        self.A = A
        self.L = L
        self.D = D



    def __next__(self):

        if self.L == None:
            self.L = self.A + 0.0
            self.A = 0.0
        if self.D == None:
            self.D = 1.0

        if self.D > 0 and self.A >= self.L:
            raise StopIteration("Limit exceeded")
        elif self.D < 0 and self.A <= self.L:
            raise StopIteration("Limit exceeded")


        result = self.A
        self.A = self.D + result

        return result

    def __iter__(self):

        return self




class colorizer:

    def __init__(self, color='red'):
        self.color = getattr(bcolors, color)


    def __enter__(self):
        self.text = print(f"{self.color}")
        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{bcolors.ENDC}")





class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height

class Triangle(Shape):

    def __init__(self, x, y, height, side):
        super().__init__(x, y)
        self.height = height
        self.side = side

    def square(self):
        return (self.height * self.side) / 2

class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def square(self):
        return self.width * self.height * math.sin(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass




if __name__ == "__main__":

    assert (list(frange(5)) == [0, 1, 2, 3, 4])
    assert (list(frange(2, 5)) == [2, 3, 4])
    assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
    assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
    assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
    assert (list(frange(1, 5)) == [1, 2, 3, 4])
    assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
    assert (list(frange(0, 0)) == [])
    assert (list(frange(100, 0)) == [])

    print('SUCCESS!')

    with colorizer(color="green"):
        print('printed in green')
    print('printed in default color')

    r = Rectangle(0, 0, 10, 20)
    r1 = Rectangle(10, 0, -10, 20)
    r2 = Rectangle(0, 20, 100, 20)

    c = Circle(10, 0, 10)
    c1 = Circle(100, 100, 5)

    p = Parallelogram(1, 2, 20, 30, 45)

    p1 = Parallelogram(1, 2, 20, 30, 45)

    t = Triangle(2, 5, 45, 65)
    t1 = Triangle(4, 6, 89, 90)
    str(p1)
    p.x
    scene = Scene()
    scene.add_figure(r)
    scene.add_figure(r1)
    scene.add_figure(r2)
    scene.add_figure(c)
    scene.add_figure(c1)
    scene.add_figure(t)
    scene.add_figure(t1)

    print(scene.total_square())
