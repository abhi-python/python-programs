class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        if self.fname == None or self.lname ==None: 
            return "Name is not set! Please set it using setter."
        return f"This is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname ==None: 
            return "Email is not set! Please set it using setter."
        return f"{self.fname}.{self.lname}@gmail.com"  
    @email.setter
    def email(self, string):
        print("Setting Now...")
        name = string.split("@")[0]
        fname = name.split(".")[0]
        lname = name.split(".")[1]
        self.fname = fname
        self.lname = lname      
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

abhi = Employee("Abhilash", "Saini")
abhi.fname = "aman"
#print(abhi.explain())
abhi.email = "akash.saini@gmail.com"
#print(abhi.explain())
print(abhi.email)
del abhi.email
print(abhi.email)
#print(abhi.explain())
abhi.email = "arpit.poddar@gmail.com"
print(abhi.email)