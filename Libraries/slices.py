import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for X in sys.argv[1:-1]:
    print("hello,may name is", X)