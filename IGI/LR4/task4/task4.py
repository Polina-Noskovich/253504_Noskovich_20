from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import sys
import os
# Получаем путь к текущей директории (где находится task3.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Переходим на уровень выше, чтобы получить доступ к каталогу LR4
parent_dir = os.path.dirname(current_dir)
# Добавляем путь к каталогу LR4 в PYTHONPATH
sys.path.append(parent_dir)
# Теперь мы можем импортировать модуль task
from task import Task

class ResizableMixin:
    _a: float
    _b: float

    def resize(self, a, b):
        self._a = a
        self._b = b

class Shape(ABC):
    def __init__(self, color, shape_name):
        self._color = ShapeColor(color)
        self._shape_name = shape_name

    def getColor(self):
        return self._color

    color = property(getColor)

    def getShapeName(self):
        return self._shape_name

    name = property(getShapeName)

    @abstractmethod
    def calculate_area(self):
        pass

class ShapeColor:
    def __init__(self, color):
        self._color = color

    def getColor(self):
        return self._color

    color = property(getColor)


class Parallelogram(Shape, ResizableMixin):
    def __init__(self, a, b, A, color, figure_name):
        super().__init__(color, figure_name)
        self._a = a
        self._b = b
        self._A = A

    def getA(self):
        return self._A

    A = property(getA)

    def calculate_area(self):
        return self._a * self._b * np.sin(np.deg2rad(self._A))

    def print_attributes(self):
        print('parallelogram sides: {}, {}, angle: {}, color: {}, area: {}'.format(self._a, self._b, self._A,
                                                                                   self._color.color,
                                                                                   self.calculate_area()))


class ParallelogramDrawer:
    def __init__(self, parallelogram: Parallelogram):
        self._parallelogram = parallelogram

    def plot_parallelogram(self):
        A = np.array([0, 0])
        B = np.array([self._parallelogram._a, 0])  # Corrected attribute name
        C = np.array([self._parallelogram._b * np.cos(np.deg2rad(self._parallelogram._A)),
                      self._parallelogram._b * np.sin(np.deg2rad(self._parallelogram._A))])
        D = B + C

        plt.plot([A[0], B[0]], [A[1], B[1]], color='black')
        plt.plot([B[0], D[0]], [B[1], D[1]], color='black')
        plt.plot([D[0], C[0]], [D[1], C[1]], color='black')
        plt.plot([C[0], A[0]], [C[1], A[1]], color='black')

        dots = np.array([A, B, C, D])

        hull = ConvexHull(dots)

        plt.fill(dots[hull.vertices, 0], dots[hull.vertices, 1], self._parallelogram.color.color)

        plt.axis('equal')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.title(self._parallelogram.name)
        figure = plt.gcf()
        figure.set_size_inches(16, 9)
        plt.savefig(r'task4\plots.png', dpi=300)
        plt.show()

class Task4(Task):
    @staticmethod
    def perform():
        a = float(input('Please enter the length of side a: '))
        b = float(input('Please enter the length of side b: '))
        A = float(input('Please enter the angle A in degrees: '))
        color = input('Please enter the color of the parallelogram: ')
        name = input('Please enter the name of the parallelogram: ')

        parallelogram = Parallelogram(a, b, A, color, name)
        parallelogram.print_attributes()
        parallelogram_drawer = ParallelogramDrawer(parallelogram)
        parallelogram_drawer.plot_parallelogram()

        while True:
            choice = input('Enter 1 to change the sides of the parallelogram, or anything else to quit: ')
            if choice == '1':
                a = float(input('Please enter the length of side a: '))
                b = float(input('Please enter the length of side b: '))
                parallelogram.resize(a, b)
                parallelogram_drawer.plot_parallelogram()
            else:
                break

# Task4.perform()
