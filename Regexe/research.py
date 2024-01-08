import re

email =input("what is your email?")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$",email):
    print("Valid")

else:
    print("Invalid")