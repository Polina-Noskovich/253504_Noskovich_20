from decorator import funcInfoDec

@funcInfoDec
def input_list():
    """Function to input a list of float items from the user"""
    while True:
        try:
            elements = input("Enter the list float items separated by a space: ").split()
            elements = [float(element) for element in elements]
            return elements
        except ValueError:
            print("Wrong input")

def find_max_absolute(lst):
    """Function to find the maximum absolute value element in a given list"""
    max_abs = max(lst, key=abs)
    return max_abs

def find_sum_between_negatives(lst):
    """Function to find the sum of elements located between the first and second negative elements in a list"""
    neg_indices = [i for i, num in enumerate(lst) if num < 0]
    if len(neg_indices) < 2:
        return "There are fewer than two negative numbers in the list"
    start_index, end_index = neg_indices[0], neg_indices[1]
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    sum_between_negatives = sum(lst[start_index + 1 : end_index])
    return sum_between_negatives

def print_list(lst):
    print("List:", lst)

def task5():
    my_list = input_list()
    print_list(my_list)

    if my_list.count(0) == len(my_list):
        print("Error: The list should not contain only zero values")
        exit()

    max_abs_element = find_max_absolute(my_list)
    print("The maximum modulo element of the list:", max_abs_element)

    sum_between_negatives = find_sum_between_negatives(my_list)
    print("The sum of the list items located between the first and second negative elements:", sum_between_negatives)
