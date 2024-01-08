class Student:
    def __init__(self,name,house,patrous):
        if not name:
            raise ValueError("Missing Name")
        if house not in("Gryffindor","Slytherin","Ravenclaw","Hufflepuff"):
            raise ValueError("Invaid house")
        if patrous not in("Stage","Otter","Jack Russell"):
            raise ValueError("Invaild patrous")
        
        self.name=name
        self.house=house
        self.patrous=patrous

    def __str__(self):
            return f"{self.name} from {self.house}"

    def charm(self): 
        match self.patrous:
            
            case "Stage":
                return "🐴"
            case "Otter":
                 return "🦦"
            case "Jack Russell":
                return "🐶"
            case _:
                return "🪄"
                
def main():
    student =get_student()
    print("Expecto patroum!")
    print(student.charm())


def get_student():
    name=input("Name: ")
    house=input("House: ")
    patrous=input("Patrous: ") or None
    
    return Student(name,house,patrous)

if __name__ == "__main__":
 main()


 
         
            