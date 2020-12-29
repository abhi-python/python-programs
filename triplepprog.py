class Employee:
    no_of_leaves = 10 # Public var which can be use anywhere and anytype
    _protec = 15 #Protected var which can be use in this class and other class derived from this class.
    __pr = 20 # Private var which can be used in this class only
    
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole

    def printdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"  

abhi = Employee("Abhilash", 5000, "Programmer")
print(abhi._protec)
print(abhi.no_of_leaves)
print(abhi._Employee__pr) #print private var with the class name 
