def main():
    X = get_int("what is x?")
    print(f"x is {X}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("X is not integer")
        pass


main()
