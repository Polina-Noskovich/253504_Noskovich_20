from math import fabs, sqrt
import matplotlib.pyplot as plt
import numpy as np
from statistics import median, mode
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from task import Task

class AttributesCalculator:
    @staticmethod
    def calculate_dispersion(series):
        """Calculates the dispersion of a series."""
        average = sum(series)/len(series)
        elements_sum = sum(i*i for i in series)
        return elements_sum/len(series) - average**2

class Series:
    def __init__(self, x, eps):
        """Initializes Series object."""
        self._x = x
        self._eps = eps
        self._attribute_calculator = AttributesCalculator()

    def calculateSeries(self):
        """Function to calculate Taylor series approximation."""
        series = []
        result = 0.0
        for n in range(1, 500):
            series.append(self._x**n)
            result += self._x**n
            if fabs(result - 1/(1-self._x)) <= self._eps:
                print("\033[37m\033[1m----------------------------\033[00m")
                print("\033[37m\033[1mThe result:")
                print("----------------------------\033[00m")
                print(f"x = {self._x}, n = {n}, F(x) = {round(result, 10)}, Math F(x) = {round(1/(1-self._x), 10)}, eps = {self._eps}")
                print("\033[37m\033[1m----------------------------\033[00m")
                print("\033[37m\033[1mAdditional parameters:")
                print("----------------------------\033[00m")
                print(f"Arithmetic mean of sequence elements: {round(result/(n + 1), 10)}")
                print(f"Median of sequence elements: {median(series)}")
                print(f"Mode of sequence elements: {mode(series)}")
                print(f"Dispersion of sequence elements: {self._attribute_calculator.calculate_dispersion(series)}")
                print(f"Sequence standard deviation: {sqrt(self._attribute_calculator.calculate_dispersion(series))}")
                return series, n

        print("Iterations > 500")
        return None, None
    
class PlotDrawer:
    def __init__(self, series, n):
        """Initializes PlotBuilder object."""
        self._series = series
        self._n = n

    def show_plot(self):
        """Displays the plot of the function decomposition into a series."""
        x = np.linspace(-0.25, 1, 80)
        y1 = 1/(1-x)
        y2 = sum(x**i for i in range(self._n))
        plt.plot(x, y1, label='1/(1-x)', color='blue', linewidth=2)  # Синий цвет и толщина линии 2
        plt.plot(x, y2, label='∑x^n', color='orange', linewidth=2)  # Оранжевый цвет и толщина линии 2
        plt.subplots_adjust(bottom=0.05, left=0.05)

        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('The graph of the decomposition of the function into a series') # Series convergence graph
        plt.annotate('---------- Annotation ----------', (0.25, 55))
        plt.text(0.02, 50, 'There are two plots: blue is our math function, orange is our series ')

        plt.grid(True)
        figure = plt.gcf()
        figure.set_size_inches(10, 5)
        plt.savefig(r'task3\plots.png', dpi=100)
        plt.show()


class Task3(Task):
    """
    A class representing Task 3.
    Inherits from Task class.
    """
    @staticmethod
    def complete_task():
        """Function to get input from the user."""
        while True:
            try:
                x = float(input("Enter x value for decomposing the function into a Taylor series: "))
                if fabs(x) >= 1:
                    print("|x| >= 1. Enter again.")
                else:
                    eps = float(input("Enter eps value of the calculation accuracy: "))
                    series = Series(x, eps)
                    series_list, n = series.calculateSeries()

                    series_plot = PlotDrawer(series_list, n)
                    series_plot.show_plot()
                    return
            except ValueError:
                print("Wrong input")
        
# Task3.complete_task()