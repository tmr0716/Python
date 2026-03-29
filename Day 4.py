print('----------------------------------- Classroom Day 4 -----------------------------------')
# print('------------------------------------ DICTIONARIES ------------------------------------')
# student = {"Name": "Sanyam","Age": 20,"City": "Pune"}
# print(student["Age"])
# print(student["City"])
# student["Roll_No"] = 69
# print(student)
# student["Name"] = "Sahil"
# print(student)
# print('------------------------------------ KEYS/VALUES/ITEMS ------------------------------------')
# print(student.keys())
# print(student.values())
# print(student.items())
# print('------------------------------------ LOOPS AND NESTED ------------------------------------')
# user = {"person": {"Name": "Sanyam", "Age": 20, "City": "Pune"}}
# for k,v in user["person"].items():
#     print(f"{k}: {v}")
# print('----------------------------------- SETS -----------------------------------')
# s = {1, 2, 3, 4, 5}
# print(s)
# p = {x*x for x in range(1, 8)}
# print(p)
# q = {1,2,3,6}
# print(q)
# print('----------------------------------- SETS OPERATIONS -----------------------------------')
# r = {7,9,8,6}
# print(q^r)
# print('----------------------------------- HANDS-ON EXERCISES -----------------------------------')
# contact_book = {"NAMES" : "PHONE NUMBERS","Sahil" : 9876543210,"Sanyam" : 9123456780,"Aditya" : 9988776655,"Ajay" : 9876545678,"Rohan" : 9514532048}
# print("=== Contact Book ===")
# for name, number in contact_book.items():
#     print(f"{name}: {number}")
print('----------------------------- Homework -----------------------------')
# - Extend contact book → store email too
contact_book = {"NAMES" : "PHONE NUMBERS","Sahil" : 9876543210,"Sanyam" : 9123456780,"Aditya" : 9988776655,"Ajay" : 9876545678,"Rohan" : 9514532048}
contact_book_email = {"Sahil": "sahil@email.com", "Sanyam": "sanyam@email.com", "Aditya": "aditya@email.com", "Ajay": "ajay@email.com", "Rohan": "rohan@email.com"}
print("=== Contact Book ===")
for name, number in contact_book.items():
    email = contact_book_email.get(name, "EMAIL")
    print(f"{name}: {number}, {email}")
# - Given two class lists → find common and unique using sets
class1 = {"Ajay", "Rohan", "Sanyam", "Sahil"}
class2 = {"Aditya", "Ishaan", "Sushant", "Ajay"}
common_students = class1 & class2
unique_students = class1 ^ class2
all_students = class1 | class2
students = class1 - class2
student = class2 - class1
print("All Students:", all_students)
print("Common Students:", common_students)
print("Unique Students:", unique_students)
print("Students only in Class 1:", students)
print("Students only in Class 2:", student)
# - Build frequency dict for words from input text