class Employee:
    
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole

    def printdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"
# These are dunder method which start from __ and end to __ that helps to operator overloading. repr and str are also special dunder method if reper and str prensent then always str run.
    
    def __add__(self, other):  
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"  

emp1 = Employee("Abhi", 10000, "Programmer")
emp2 = Employee("Rohit", 5000, "Designer")
print(emp1+emp2)  
print(emp1/emp2) 
print(repr(emp1))  
print(emp2)                   