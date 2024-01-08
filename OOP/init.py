class Student:
    def __init__(self,name,house,patrous):
        if not name:
            raise ValueError("Missing Name")
        if house not in["Gryffindor","Slytherin","Ravenclaw","Hufflepuff"]:
            raise ValueError("Invaid house")
        if patrous not in["Draco","Otter","Russell"]:
            raise ValueError("Missing name")
        

        self.name=name
        self.house=house
        self.patrous=patrous
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
        student=get_student()
        print(student)
    
def get_student():
    name=input("Name: ")
    house=input("House: ")
    patrous=input("Patrous:")
    return Student(name,house,patrous)


if __name__ == "__main__":
 main()
