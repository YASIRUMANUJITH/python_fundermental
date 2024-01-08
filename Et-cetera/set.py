students=[
    {"name":"Hermione","House":"Gryffindor"},
    {"name":"Harry","House":"Gryffindor"},
    {"name":"Ron","House":"Gryffindor"},
    {"name":"Draco","House":"Slytherin"},
    {"name":"Padma","House":"Ravenclaw"},


]

houses =set()
for student in students:
    if student["House"]not in houses:
        houses.add(student["House"])

for house in sorted(houses):
    print(house)



    


