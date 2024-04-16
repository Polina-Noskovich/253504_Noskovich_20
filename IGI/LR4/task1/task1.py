import csv
import pickle
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

class Student:
    def __init__(self, surname, street, house, apartment):
        self.surname = surname
        self.street = street
        self.house = house
        self.apartment = apartment

    def __repr__(self):
        return f"{self.surname}, {self.street}, д. {self.house}, кв. {self.apartment}"

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def students_on_street(self, street_name):
        return [student for student in self.students if student.street == street_name]

    def students_in_house(self, house_number):
        return [student for student in self.students if student.house == house_number]

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow([student.surname, student.street, student.house, student.apartment])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.add_student(Student(*row))

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)

    def load_from_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.students = pickle.load(file)



class Task1(Task):
    @staticmethod
    def perform():
        school = School()
        school.add_student(Student("Иванов", "Пушкина", 10, 5))
        school.add_student(Student("Петров", "Ленина", 5, 15))
        school.add_student(Student("Сидоров", "Пушкина", 10, 7))
        school.add_student(Student("Носкович", "Прушинских", 78, 1))
        school.add_student(Student("Гусева", "Прушинских", 10, 7))

        # Сохранение в файлы CSV и pickle
        school.save_to_csv("task1/students.csv")
        school.save_to_pickle("task1/students.pickle")

        # Создание нового объекта School и загрузка данных из файлов
        input("\033[33m\033[1mCSV:")
        new_school = School()
        new_school.load_from_csv("task1/students.csv")
        print(new_school.students)
        print("\033[00m")
        input("\033[33m\033[1mPickle:")
        new_school.load_from_pickle("task1/students.pickle")
        print(new_school.students)
        print("\033[00m")
        # Создаем объект школы
        school = School()
        
        # Загружаем данные из файла
        school.load_from_csv("task1/students.csv")  # Можно использовать любой формат сохранения

        # Вводим с клавиатуры название улицы и номер дома
        street_name = input("Введите название улицы: ")
        house_number = input("Введите номер дома: ")

        # Определяем количество учеников на указанной улице
        students_on_street = school.students_on_street(street_name)
        print(f"Количество учеников на улице {street_name}: {len(students_on_street)}")
        
        # Выводим список учеников, живущих в указанном доме
        students_in_house = school.students_in_house(house_number)
        if students_in_house:
            print(f"Список учеников, живущих в доме {house_number}:")
            for student in students_in_house:
                print(student)
        else:
            print(f"В доме {house_number} не живут ученики.")

# Task1.perform()