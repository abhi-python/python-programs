class Employee:
    
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole
    
    def printdeatils(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"    
    
    @classmethod
    def from_hash(cls, string):
        return cls(*string.split("-"))

class Programmer(Employee):
    
    def __init__(self, ename, esalary, erole, elanguages):
        self.name = ename
        self.salary = esalary
        self.role = erole
        self.languages = elanguages
    
    def progdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role} and the languages is {self.languages}"

abhi = Employee.from_hash("Abhilash-5000-Instructor")
aman = Employee("Aman", 6000, "designer")
akash = Programmer("Akash", 9000, "Programmer", ["Python", "CPP"])
arpit = Programmer("Arpit", 8000, "Programmer", ["Ruby", ".Net"])

print(abhi.salary, aman.role, arpit.progdetails(), akash.printdeatils())

        