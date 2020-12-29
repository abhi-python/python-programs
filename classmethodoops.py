class Employee:
    no_of_leaves = 10
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

abhi = Employee("Abhilash", 5000, "Programmer")
aman = Employee("Aman", 15000, "Designer")
print(aman.no_of_leaves)
aman.change_leaves(34)
print(aman.no_of_leaves)