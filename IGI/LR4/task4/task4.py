from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from task import Task

class ResizableMixin:
    '''A mixin class providing functionality for resizing geometric shapes.'''
    _a: float
    _b: float

    def resize(self, a, b):
        '''Resizes the shape with new dimensions a and b.'''
        self._a = a
        self._b = b

class GeometricShape(ABC):
    '''An abstract class representing a geometric shape.'''
    def __init__(self, name, color):
        '''Initializes a geometric shape with a given name and color.'''
        self._name = name
        self._color = ShapeColor(color)

    @abstractmethod
    def calculate_area(self):
        '''Abstract method to calculate the area of the shape.'''
        pass

    def getName(self):
        '''Returns the name of the shape.'''
        return self._name

    def getColor(self):
        '''Returns the color of the shape.'''
        return self._color
    
    name = property(getName)
    color = property(getColor)

class ShapeColor:
    '''A class representing the color of a geometric shape.'''
    def __init__(self, color):
        '''Initializes the color of a shape.'''
        self._color = color

    def getColor(self):
        '''Returns the color of the shape.'''
        return self._color

    color = property(getColor)

class Parallelogram(GeometricShape, ResizableMixin):
    '''A class representing a parallelogram.'''
    def __init__(self, a, b, A, name, color):
        '''Initializes a parallelogram with given dimensions and attributes.'''
        super().__init__(name, color)
        self._a = a
        self._b = b
        self._A = A

    def getA(self):
        '''Returns the angle A of the parallelogram.'''
        return self._A

    A = property(getA)

    def calculate_area(self):
        '''Calculates the area of the parallelogram.'''
        return self._a * self._b * np.sin(np.deg2rad(self._A))

    def print_attributes(self):
        '''Prints attributes of the parallelogram.'''
        print('\033[37m\033[1mParallelogram sides a, b: {}, {}, angle A(degrees): {}, color: {}, area: {}'.format(self._a, self._b, self._A,
                                                                                   self._color.color,
                                                                                   self.calculate_area()))
        print("\033[00m")

class ParallelogramDrawer:
    '''A class responsible for drawing parallelograms.'''
    def __init__(self, parallelogram: Parallelogram):
        '''Initializes a ParallelogramDrawer with a given parallelogram.'''
        self._parallelogram = parallelogram

    def plot_parallelogram(self):
        '''Plots the parallelogram using matplotlib.'''
        A = np.array([0, 0])
        B = np.array([self._parallelogram._a, 0])
        C = np.array([self._parallelogram._b * np.cos(np.deg2rad(self._parallelogram._A)),
                      self._parallelogram._b * np.sin(np.deg2rad(self._parallelogram._A))])
        D = B + C

        plt.plot([A[0], B[0]], [A[1], B[1]], color=self._parallelogram._color.color)
        plt.plot([B[0], D[0]], [B[1], D[1]], color=self._parallelogram._color.color)
        plt.plot([D[0], C[0]], [D[1], C[1]], color=self._parallelogram._color.color)
        plt.plot([C[0], A[0]], [C[1], A[1]], color=self._parallelogram._color.color)

        dots = np.array([A, B, C, D])

        hull = ConvexHull(dots)

        plt.fill(dots[hull.vertices, 0], dots[hull.vertices, 1], self._parallelogram.color.color)

        plt.axis('equal')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.title(self._parallelogram.name, color=self._parallelogram._color.color, fontsize=20)
        figure = plt.gcf()
        figure.set_size_inches(10, 5)
        plt.savefig(r'task4\plots.png', dpi=100)
        plt.show()

class Task4(Task):
    """
    A class representing Task 4.
    Inherits from Task class.
    """
    @staticmethod
    def complete_task():
        '''Completes the task of creating and plotting a parallelogram.'''
        while True:
            try:
                a = float(input('Enter the length of the parallelogram side a: '))
                b = float(input('Enter the length of the parallelogram side b: '))
                A = float(input('Enter the angle A in degrees: '))
                color = input('Enter the color of the parallelogram: ')
                name = input('Enter the name of the parallelogram: ')

                parallelogram = Parallelogram(a, b, A, name, color)
                parallelogram.print_attributes()
                parallelogram_drawer = ParallelogramDrawer(parallelogram)
                parallelogram_drawer.plot_parallelogram()
                return
            except ValueError:
                print("Wrong input")

# Task4.complete_task()


# Task4.complete_task()
