import mysql.connector


# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",   
    database="student_db"
)

cursor = conn.cursor()


# Add Student
def add_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    query = """
    INSERT INTO students(name, course, email, phone)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, course, email, phone))
    conn.commit()

    print("Student Added Successfully!")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No Students Found!")
        return

    print("\n----- STUDENT RECORDS -----")
    for row in records:
        print(
            f"ID: {row[0]} | "
            f"Name: {row[1]} | "
            f"Course: {row[2]} | "
            f"Email: {row[3]} | "
            f"Phone: {row[4]}"
        )


# Search Student
def search_student():
    student_id = int(input("Enter Student ID: "))

    query = "SELECT * FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    record = cursor.fetchone()

    if record:
        print("\nStudent Found")
        print(f"ID: {record[0]}")
        print(f"Name: {record[1]}")
        print(f"Course: {record[2]}")
        print(f"Email: {record[3]}")
        print(f"Phone: {record[4]}")
    else:
        print("Student Not Found!")


# Update Student
def update_student():
    student_id = int(input("Enter Student ID to Update: "))

    name = input("Enter New Name: ")
    course = input("Enter New Course: ")
    email = input("Enter New Email: ")
    phone = input("Enter New Phone: ")

    query = """
    UPDATE students
    SET name=%s, course=%s, email=%s, phone=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (name, course, email, phone, student_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")


# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    query = "DELETE FROM students WHERE id=%s"

    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")


# Main Menu
while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        conn.close()
        break

    else:
        print("Invalid Choice!")


