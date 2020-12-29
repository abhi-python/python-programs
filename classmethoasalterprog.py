class Employee:
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-")) # it works same as above method in one line
        

abhi = Employee("Abhi", 4000, "Programmer")
aman = Employee("Aman", 5000, "Designer")
akash = Employee.from_dash("Akash-6000-Doctor")
print(aman.salary)
print(akash.role)
