email = input("what us your email?").strip()

username, domain= email.split("@")

if username and domain.endswith(".com"):
    print("Vaild")
else:
    print("invalid")