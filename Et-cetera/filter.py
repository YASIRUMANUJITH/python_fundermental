Students=[{"name":"Hermione","House":"Gryffindor"},
          {"name":"Harry","House":"Gryffindor"},
          {"name":"Ron","House":"Gryffindor"},
          {"name":"Draco","House":"Slytherin"},
          

]

def is_gryffindor(s):
    return s["House"]== "Gryffindor"

gryffindors = filter(is_gryffindor,Students)

for gryffindor in sorted(gryffindors,key=lambda s:s["name"]):
    print(gryffindor["name"])