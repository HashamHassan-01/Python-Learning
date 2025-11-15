def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    with open("students.txt", "a") as f:
        f.write(f"{roll},{name},{course}\n")
    print("Student added!\n")

def view_students():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()
            if not data:
                print("No records found.\n")
                return
            print("All Students:")
            for line in data:
                roll, name, course = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Course: {course}")
            print()
    except FileNotFoundError:
        print("No records found.")
        print()

def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll, name, course = line.strip().split(",")
                if roll == roll_no:
                    print(f"Found -> Roll: {roll}, Name: {name}, Course: {course}\n")
                    found = True
                    break
        if not found:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def update_student():
    roll_no = input("Enter Roll No to update: ")
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
        with open("students.txt", "w") as f:
            updated = False
            for line in lines:
                roll, name, course = line.strip().split(",")
                if roll == roll_no:
                    name = input("Enter new name: ")
                    course = input("Enter new course: ")
                    f.write(f"{roll},{name},{course}\n")
                    updated = True
                else:
                    f.write(line)
        if updated:
            print("Record updated!\n")
        else:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
        with open("students.txt", "w") as f:
            deleted = False
            for line in lines:
                roll, name, course = line.strip().split(",")
                if roll != roll_no:
                    f.write(line)
                else:
                    deleted = True
        if deleted:
            print("Record deleted!\n")
        else:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

while True:
    print("=== Student Record Management ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        update_student()
    elif ch == "5":
        delete_student()
    elif ch == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
