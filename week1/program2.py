
def func():
    for i in range(1):
        global name,age,roll_no,marks
        name=input("name: ")
        age=int(input("age: "))
        if age<18:
            print("wrong age he is not eligible for university student")
            break
        roll_no=input("roll_no: ")
        marks=int(input("marks: "))
        if marks>100 or marks<0:
            print("invalid marks")
            break
        print()

def print_info():
    if(student["age"]<18 or student1["age"]<18 or student2["age"]<18 or student3["age"]<18 or student4["age"]<18):
        print("wrong age he is not eligible for university student")
        if(student["marks"]>100 or student1["marks"]>100 or student2["marks"]>100 or student3["marks"]>100 or student4["marks"]>100) or (student["marks"]<0 or student1["marks"]<0 or student2["marks"]<0 or student3["marks"]<0 or student4["marks"]<0):
            print("invalid marks")
    else:
        print("roll_no|name|age|marks")
        print(f'{student["rollno"]}|{student["name"]}|{student["age"]}|{student["marks"]}')
        print(f'{student1["rollno"]}|{student1["name"]}|{student1["age"]}|{student1["marks"]}')
        print(f'{student2["rollno"]}|{student2["name"]}|{student2["age"]}|{student2["marks"]}')
        print(f'{student3["rollno"]}|{student3["name"]}|{student3["age"]}|{student3["marks"]}')
        print(f'{student4["rollno"]}|{student4["name"]}|{student4["age"]}|{student4["marks"]}')
        avg=(student["marks"]+student1["marks"]+student2["marks"]+student3["marks"]+student4["marks"])/5
        max_marks=max(student["marks"],student1["marks"],student2["marks"],student3["marks"],student4["marks"])
        min_marks=min(student["marks"],student1["marks"],student2["marks"],student3["marks"],student4["marks"])
        print(f'the class avg is {avg}')
        print(f'this is the {max_marks}')
        print(f'this is the {min_marks}')
        
        
if __name__=="__main__":
    func()
    student={"name":name,"age":age,"rollno":roll_no,"marks":marks}
    func()
    student1={"name":name,"age":age,"rollno":roll_no,"marks":marks}
    func()
    student2={"name":name,"age":age,"rollno":roll_no,"marks":marks}
    func()
    student3={"name":name,"age":age,"rollno":roll_no,"marks":marks}
    func()
    student4={"name":name,"age":age,"rollno":roll_no,"marks":marks}
    print_info()

    

    

         



