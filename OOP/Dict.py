def main():
    student =get_student()
    if student["name"]== "padma":
     student["House"] = "ravenclaw"
    print(f"{student['name']} from {student['House']}")


def get_student():
    name=input("NAEM: ")
    House=input("House: ")
    return {"name":name,"House":House}

if __name__ == "__main__":
    main()