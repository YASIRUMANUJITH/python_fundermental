# ask user for their name
name = input("what is your name? ")

#Remove Whitespace from str 
name = name.strip().title()

#split user's name into first name and last name
first, last = name.split(" ")

# say hello to user
print("Hello,", first )


