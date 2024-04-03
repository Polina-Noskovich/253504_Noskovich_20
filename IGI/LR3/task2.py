import sequence_initialization
from decorator import funcInfoDec

@funcInfoDec

def calculate(list_):
    """Function to calculate the sum of positive integers in a list."""
    counter = 0

    for i in list_:
        if i > 0:
            counter += i
    print(f'Sums of integer numders more then 0 is {counter}')
    return counter


def task2():
    """Runs task2 
    Task: Create a loop that takes integers from the keyboard 
    and counts the number of even numbers. 
    End of cycle is entering a number greater than 0"""
    while True:
        initialization_choice = input("Choose sequence initialization method ('g' for generator, 'u' for user input): ")
        if initialization_choice == 'g':
            sequence = sequence_initialization.initialize_with_generator((x for x in range(10)))
        elif initialization_choice == 'u':
            sequence = sequence_initialization.initialize_with_user_input()
        else:
            print("Invalid choice.")
            break

        print("Initialized sequence:", sequence)
        calculate(sequence)
