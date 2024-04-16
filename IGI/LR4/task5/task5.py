import numpy as np
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

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def sort_last_row(self):
        self.data[-1] = np.sort(self.data[-1])

    def get_last_row(self):
        return self.data[-1]

    def compute_median(self):
        # Медиана через стандартную функцию
        median_std = np.median(self.data[-1])

        # Медиана через программирование формулы (если количество элементов нечетное)
        sorted_row = np.sort(self.data[-1])
        n = len(sorted_row)
        if n % 2 == 1:
            median_formula = sorted_row[n // 2]
        else:
            median_formula = (sorted_row[n // 2 - 1] + sorted_row[n // 2]) / 2

        return median_std, median_formula


# Пример использования:
class Task5(Task):
    @staticmethod
    def perform():
        # Создание матрицы с помощью NumPy
        data = np.random.randint(0, 10, size=(3, 3))

        # Создание объекта матрицы
        matrix = Matrix(data)

        print("Исходная матрица:\n")
        print(matrix.data)

        # Сортировка последней строки матрицы
        matrix.sort_last_row()
        print("\nМатрица с отсортированной последней строкой:\n")
        print(matrix.data)

        # Получение последней строки матрицы
        last_row = matrix.get_last_row()
        print("\nПоследняя строка матрицы:", last_row)

        # Вычисление медианы
        median_std, median_formula = matrix.compute_median()
        print("\nМедиана (стандартная функция):", median_std)
        print("Медиана (программирование формулы):", median_formula)

        # Примеры операций с массивами NumPy и математических/статистических функций:
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        # Умножение каждого элемента на 2
        result1 = arr1 * 2
        # Возведение каждого элемента в квадрат
        result2 = np.square(arr1)
        # Среднее значение всех элементов массива
        mean_value = np.mean(arr1)
        # Коэффициент корреляции между двумя массивами
        corr_matrix = np.corrcoef(arr1, result1)
        # Дисперсия значений массива
        variance_value = np.var(arr1)
        # Стандартное отклонение значений массива
        std_deviation = np.std(arr1)

        print("\nПримеры операций с массивами NumPy и математических/статистических функций:")
        print("Умножение на 2:\n", result1)
        print("Возведение в квадрат:\n", result2)
        print("Среднее значение:", mean_value)
        print("Корреляционная матрица:\n", corr_matrix)
        print("Дисперсия:", variance_value)
        print("Стандартное отклонение:", std_deviation)

# Task5.perform()