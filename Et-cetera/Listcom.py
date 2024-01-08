Students=[{"name":"Hermione","House":"Gryffindor"},
          {"name":"Harry","House":"Gryffindor"},
          {"name":"Ron","House":"Gryffindor"},
          {"name":"Draco","House":"Slytherin"},
          

]

gryffindor = [

    student["name"] for student in Students if student["House"]=="Gryffindor"
]

for gryffindor in sorted(gryffindor):
    print(gryffindor)