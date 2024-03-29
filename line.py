import math
from utils import _from_rgb


class Line:
    def __init__(self, point1, point2, canvas, color=tuple([0]*3)):
        self.point1: tuple = point1
        self.point2: tuple = point2
        self.obj = canvas.create_line(point1[0], point1[1], point2[0], point2[1], width=10)
        self.color = color
        self.carsOn: set = set()
        self.updateColor(canvas)

    @property
    def xLength(self):
        return self.point2[0] - self.point1[0]

    @property
    def yLength(self):
        return self.point2[1] - self.point1[1]

    @property
    def length(self):
        return math.sqrt(self.xLength ** 2 + self.yLength ** 2)

    @property
    def slope(self):
        return self.yLength / self.xLength

    def updateColor(self, canvas):
        canvas.itemconfig(self.obj, fill=_from_rgb(tuple(max(min(255, e1 + e2), 0) for e1, e2 in zip(self.color, (0, 0, 50 * len(self.carsOn))))))

    def addCar(self, car, canvas):
        self.carsOn.add(car)
        self.updateColor(canvas)

    def removeCar(self, car, canvas):
        self.carsOn.remove(car)
        self.updateColor(canvas)

    def delete(self, canvas):
        canvas.delete(self.obj)
