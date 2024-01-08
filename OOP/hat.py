import random


class Hat:
   
   house=["Gryffindor","Slytherin","ravencllaw","Hufflepuff"]

   @classmethod
   def sort(cls, name):
        print(name,"is in", random.choice(cls.house))


Hat.sort("Harry")