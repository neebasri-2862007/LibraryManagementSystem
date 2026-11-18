
# Library Management System

book_name = "Python Programming"
author = "Guido van Rossum"
price = 450

print("===== LIBRARY MANAGEMENT SYSTEM =====")
print("Book Name :", book_name)
print("Author    :", author)
print("Price     : Rs.", price)

# Book Issue Function

def issue_book():
    student_name = input("Enter Student Name: ")
    book_name = input("Enter Book Name: ")

    print("\n===== BOOK ISSUE DETAILS =====")
    print("Student Name:", student_name)
    print("Book Name:", book_name)
    print("Book issued successfully!")


issue_book()