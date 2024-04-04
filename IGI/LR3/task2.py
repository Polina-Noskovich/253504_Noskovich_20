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
    End of cycle is entering a number greater than 0."""
    while True:
        choice = input("Choose sequence initialization method ('g' for generator, 'u' for user input): ").lower()
        if choice == 'g':
            sequence = list(sequence_initialization.my_generator(2,14,1))
        elif choice == 'u':
            sequence = sequence_initialization.initialize_with_user_input()
        else:
            print("Invalid choice.")
            break

        print("Initialized sequence:", sequence)
        calculate(sequence)
