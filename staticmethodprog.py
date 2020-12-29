class Employee:
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    @staticmethod # this method is used to print any thing by the class or instance, when it is called.
    def printgood(str):
        print("This is the details of " + str)    

abhi = Employee.from_dash("Abhi-6000-Programmer")
print(abhi.salary)
abhi.printgood("abhilash")