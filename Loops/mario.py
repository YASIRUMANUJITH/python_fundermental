def main():
    print_square(2)

 # For each row in square


def print_square(size):
    for x in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
