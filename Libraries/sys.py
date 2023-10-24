import sys

#check for errors

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many argumnets")

#print name tags
else:
    print("hello ,my name is", sys.argv[1])
    
