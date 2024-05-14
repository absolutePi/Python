employee_file = open("employees.txt", "r")#r for read w for write a for append
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
# import os

# print(os.getcwd())


