import re

email= input("what is your email?")

if re.search(r"^\w+@\w.+\.(com|edu|gov|org)$",email):
    print("Valid")

else:
    print("Invalid")
