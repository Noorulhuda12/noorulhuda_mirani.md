def get_height():
    """
    Prompt the user for a positive integer between 1 and 8 (inclusive).
    If the input is invalid, re-prompt until a valid number is given.
    """
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass  # Ignore invalid inputs and re-prompt


def print_pyramids(height):
    """
    Print two pyramids of hashes (#) separated by two spaces.
    The number of rows is equal to the given height.
    """
    for i in range(1, height + 1):
        # Left pyramid
        spaces = " " * (height - i)
        hashes = "#" * i
        # Print the row
        print(f"{spaces}{hashes}  {hashes}")


# Corrected the variable name to _name_ (double underscores)
if _name_ == "_main_":  
    # Get the pyramid height from the user
    height = get_height()
    # Print the pyramids
    print_pyramids(height)
