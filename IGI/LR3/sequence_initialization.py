def initialize_with_generator(sequence):
    """Initialize sequence using a generator function"""
    return list(sequence)

def initialize_with_user_input():
    """Initialize sequence using user input"""
    sequence = []
    while True:
        try:
            number = int(input("Enter an integer number (Enter < 0 to end): "))
            if number < 0:
                break
            sequence.append(number)
        except ValueError:
            print("Wrong input. Please enter an integer number.")
    return sequence
