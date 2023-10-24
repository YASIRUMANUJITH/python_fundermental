try:
    X = int(input("what is x?"))
except ValueError:
    print("X is not an integer")
print(f"x is {X}")
