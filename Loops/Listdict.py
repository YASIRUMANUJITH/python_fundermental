students = [
    {"name": "Hermione", "house": "Gryffindor", "patrouns": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patrouns": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patrouns": "Jack Russell terrir"},
    {"name": "Draco", "house": "slytherin", "patrouns": None}
]

for student in students:
    print(student["name"], student["house"], student["patrouns"], sep=",")
