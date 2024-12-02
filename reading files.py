employee_file= open("employee.txt", "r")
print (employee_file.readable())
employee_file.close()                   


employee_file= open("employee.txt", "r")
print (employee_file.readline())
employee_file.close()                   

employee_file= open("employee.txt", "r")
for employee in employee_file:
    print(employee)

employee_file.close()                   











