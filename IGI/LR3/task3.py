from decorator import funcInfoDec

@funcInfoDec
def get_count(string):
    """Function to count the number of characters in a string within the range 'f' to 'y' (case insensitive)."""
    count = 0
    for char in string:
        if 'f' <= char <= 'y' or 'F' <= char <= 'Y':
            count += 1
    return count


def task3():
    """Function to perform Task 3."""
    string = input("Enter string to count the number of characters within the range 'f' to 'y': ")
    print(f"Amount of chars: {get_count(string)}")

