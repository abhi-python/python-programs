class Employee:
    no_of_leaves = 10
    pass
abhi = Employee()
aman = Employee()

abhi.name = "Abhilash"
abhi.salary = 5000
abhi.role = "Programmer"

aman.name = "Aman"
aman.salary = 7000
aman.role = "designer"
aman.no_of_leaves = 15

Employee.no_of_leaves = 20

print(aman.__dict__)
print(Employee.no_of_leaves)