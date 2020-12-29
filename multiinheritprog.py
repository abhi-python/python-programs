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

class Player:

    def __init__(self, pname, pgame):
        self.name = pname
        self.game = pgame

    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}"    


class Programmer(Player, Employee):
    
    language = "Python"
    def Printlanguage(self):
        print(self.language)     

abhi = Employee.from_hash("Abhilash-6000-Instructor")
akash = Employee("Akash", 7000, "Doctor")
#aman = Programmer("Aman", 8000, "programmer")
rohit = Programmer("Rohit", ["Cricket", "Tennis"])
print(rohit.printdetails()) 
print(rohit.game)           