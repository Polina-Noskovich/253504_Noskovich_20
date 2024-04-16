from math import fabs, sqrt
import matplotlib.pyplot as plt
import numpy as np
from statistics import median, mode
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

class SeriesPlotBuilder:
    def __init__(self, series, iterations):
        self._series = series
        self._iterations = iterations

    def showPlot(self):
        x = np.linspace(-0.99, 0.99, 200)
        y1 = 1/(1-x)
        y2 = sum(x**i for i in range(self._iterations))
        plt.style.use('_mpl-gallery')
        plt.plot(x, y1, label='1/(1-x)', color='r')
        plt.plot(x, y2, label='Series', color='g')
        plt.subplots_adjust(bottom=0.05, left=0.05)

        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Series Convergence')
        plt.text(-1.05, 85, 'There are two plots:\nred is our math function\ngreen is our series ')
        plt.annotate('Annotation :)', (-1.05, 80))

        plt.grid(True)
        figure = plt.gcf()
        figure.set_size_inches(16, 9)
        plt.savefig(r'task3\plots.png', dpi=300)
        plt.show()


class SeriesAttributesCalculator:
    @staticmethod
    def calculate_dispersion(series):
        selective_average = sum(series)/len(series)
        all_elements_squares_sum = sum(i*i for i in series)
        return all_elements_squares_sum/len(series) - selective_average**2


class Series:
    def __init__(self, x, eps):
        self._x = x
        self._eps = eps
        self._attribute_calculator = SeriesAttributesCalculator()

    def calculateSeries(self):
        """Function to calculate Taylor series approximation.
    result = 0.0
    for n in range(1, 500):
        result += x**n 
        if math.fabs(result - 1/(1-x)) <= eps:
            print(f"x = {x}, n = {n}, F[x]= 1/(1-x) = {result}, Math F[x] = {1/(1 - x)}, eps = {eps}")
            return
    print("iterations > 500")
    return None"""
        series = []
        result = 0.0
        for n in range(1, 500):
            series.append(self._x**n)
            result += self._x**n
            if fabs(result - 1/(1-self._x)) <= self._eps:
                print(f"x = {self._x}, n = {n}, F(x) = {round(result, 10)}, Math F(x) = {round(1/(1-self._x), 10)}, eps = {self._eps}")
                print(f"average of series elements: {round(result/(n + 1), 10)}")
                print(f"median : {median(series)}")
                print(f"mode: {mode(series)}")
                print(f"dispersion: {self._attribute_calculator.calculate_dispersion(series)}")
                print(f"mean deviation: {sqrt(self._attribute_calculator.calculate_dispersion(series))}")
                return series, n

        print("max count of iterations")
        return


class Task3(Task):
    @staticmethod
    def perform():
        """Function to get input from the user."""
        while True:
            try:
                x = float(input("Enter x value for decomposing the function into a Taylor series: "))
                if fabs(x) >= 1:
                    print("|x| >= 1. Enter again.")
                else:
                    eps = float(input("Enter eps value of the calculation accuracy: "))
                    series = Series(x, eps)
                    series_lst, n = series.calculateSeries()

                    seriesPlotBuilder = SeriesPlotBuilder(series_lst, n)
                    seriesPlotBuilder.showPlot()
                    return
            except ValueError:
                print("Wrong input")
        
# Task3.perform()