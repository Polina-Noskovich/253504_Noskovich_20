import math
from decorator import funcInfoDec

def get_input():
    """Function to get input from the user."""
    while True:
        try:
            x = float(input("Enter x value for decomposing the function into a Taylor series: "))
            if math.fabs(x) > 1 or math.fabs(x) == 1:
                print("|x| >= 1. Enter again.")
            else:
                eps = float(input("Enter eps value of the calculation accuracy: "))
                return x, eps
        except ValueError:
            print("Wrong input")

@funcInfoDec
def calculate_tailor(x, eps):
    """Function to calculate Taylor series approximation."""
    result = 0.0
    for n in range(1, 500):
        result += x**n 
        if math.fabs(result - 1/(1-x)) <= eps:
            print(f"x = {x}, n = {n}, F[x]= 1/(1-x) = {result}, Math F[x] = {1/(1 - x)}, eps = {eps}")
            return
    print("iterations > 500")
    return None


def task1():
    """Function to perform Task 1."""
    x, eps= get_input()
    calculate_tailor(x, eps)
