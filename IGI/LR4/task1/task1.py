import csv
import pickle
import sys
import os
# Get the path to the current directory (where task1.py is located)
# Go up a level to access the LR4 directory
# Add the path to the LR4 directory to PYTHONPATH
# Now we can import the task module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from task import Task

class Student:
    """Represents a student with surname, street, house, and apartment attributes."""
    def __init__(self, surname, street, house, apartment):
        """Initializes a Student object with the given attributes."""
        self.surname = surname
        self.street = street
        self.house = house
        self.apartment = apartment

    def __repr__(self):
        """Returns a string representation of the Student object."""
        return f"{self.surname}, {self.street}, building {self.house}, apartment {self.apartment}"

class School:
    """Represents a school with a collection of students."""
    def __init__(self):
        """Initializes a School object with an empty dictionary of students."""
        self.students = {}

    def students_on_street(self, street_name):
        """Retrieves a list of students who live on the specified street."""
        return [student for student in self.students.values() if student.street == street_name]
    
    def students_in_house(self, house_number):
        """Retrieves a list of students who live in the specified house."""
        return [student for student in self.students.values() if student.house == house_number]

    def add_student(self, student_id, student):
        """Adds a student to the school."""
        self.students[student_id] = student

    def save_to_csv(self, filename):
        """Saves the school's student data to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for student_id, student in self.students.items():
                writer.writerow([student_id, student.surname, student.street, student.house, student.apartment])

    def load_from_csv(self, filename):
        """Loads student data from a CSV file into the school."""
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                student_id, surname, street, house, apartment = row
                self.add_student(student_id, Student(surname, street, house, apartment))

    def save_to_pickle(self, filename):
        """Saves the school's student data to a pickle file."""
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)

    def load_from_pickle(self, filename):
        """Loads student data from a pickle file into the school."""
        with open(filename, 'rb') as file:
            self.students = pickle.load(file)

class Task1(Task):
    """Represents Task1, a specific task involving school management."""
    @staticmethod
    def complete_task():
        """
        Completes the Task1 assignment.
        The function creates a School object, adds students to it, saves the data to CSV and pickle files,
        loads the data from the files into a new School object, performs operations on the data, and displays the results.
        """
        school = School()
        school.add_student(1, Student("Ivanov", "Gikalo", 10, 5))
        school.add_student(2, Student("Petrov", "Lenina", 5, 15))
        school.add_student(3, Student("Sidorov", "Gikalo", 10, 7))
        school.add_student(4, Student("Noskovich", "Prushinskih", 78, 1))
        school.add_student(5, Student("Guseva", "Prushinskih", 10, 7))

        # Saving to CSV and pickle files
        school.save_to_csv("task1/students.csv")
        school.save_to_pickle("task1/students.pkl")

        # Creating a new School object and loading data from files
        input("\033[37m\033[1mCSV:")
        print("\033[00m")
        new_school = School()
        new_school.load_from_csv("task1/students.csv")
        print(new_school.students)
        input("\033[37m\033[1m\nPickle:")
        print("\033[00m")
        new_school.load_from_pickle("task1/students.pkl")
        print(new_school.students)
        print("\033[00m")
        # Creating a school object
        school = School()
        
        # Loading data from file
        school.load_from_csv("task1/students.csv")  # Any saving format can be used

        # Taking street name and house number from the keyboard
        street_name = input("\033[37m\033[1mEnter the street name: \033[00m")
        house_number = input("\033[37m\033[1mEnter the house number: \033[00m")
        print("\033[37m\033[1m     --------------------------")

        # Determining the number of students on the specified street
        students_on_street = school.students_on_street(street_name)
        print(f"\033[37m\033[1mNumber of students on \033[37m\033[4m{street_name}\033[37m\033[0m\033[1m street: \033[00m{len(students_on_street)}")
        
        # Displaying a list of students living in the specified house
        students_in_house = school.students_in_house(house_number)
        if students_in_house:
            print(f"\033[37m\033[1mList of students living in house \033[37m\033[4m{house_number}\033[37m\033[0m:\033[00m")
            for student in students_in_house:
                print(student)
        else:
            print(f"No students live in house {house_number}.")

Task1.complete_task()

