student ={}
while True:
    print("\n----STUDENT MANAGER APP ----")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3.CHECK RESULT")
    print("4. QUIT ")
    
    choice = input("enter your choices ")
    # ADD STUDENT 
    if choice == "1":
        name  = input("ENTER YOUR NAME  :")
        marks = int(input(f"ENTER MARKS of : {name} :"))
        student[name] = marks
        print(f"{name} added succesfully")
        
    elif choice =="2":
        if not student:
            print("NO STUDENT  FOUND ")
        else:
            for name , marks in student.items():
                print(f"{name} : {marks}") 
    elif choice == "3":
        name = input("ENTER THE STUDENT NAME YOU WANT TO CHECK :")
        if name  in student:
            marks = student[name]
            print(f"\nStudent Name : {name}")
            print(f"Marks        : {marks}")

            if marks >=40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("STUDENT NAME NOT FOUND ")            
    elif choice =="4":
        print("exiting ...")
        break
    else:
        print("invalid syntax , please enter valid syntax")

            
        
        