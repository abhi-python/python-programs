class Employee:
    no_of_leaves = 10
    def __init__(self, aname, asalary, arole): # init is a constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and role is {self.role}"    

abhi = Employee("Abhilash", 5000, "Programmer")
aman = Employee("Aman", 10000, "designer")
print(aman.no_of_leaves)
print(abhi.printdetails())
print(aman.printdetails())
