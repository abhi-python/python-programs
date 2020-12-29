import inspect
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def explain(self):
        return f"This is {self.fname} {self.lname}"   
    @property
    def email(self):
        return f"{self.fname.lower()}.{self.lname.lower()}@gmail.com"
    @email.setter
    def email(self, string):
        name = string.split("@")[0]
        fname = name.split(".")[0]
        lname = name.split(".")[1]
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()   

abhi = Employee("Abhilash", "Saini")
print(inspect.getmembers(abhi)) 
print(abhi.email)  
abhi.email = "akash.saini@gmail.com"  
print(abhi.explain())