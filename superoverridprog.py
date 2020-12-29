class A:
    classvar1 = "I am a variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "I am an instance variable of class A"
        self.special = "special"

class B(A):
    classvar1 = "I am a variable in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "I am an instance variable of class B"

a = A()
b = B()
print(b.classvar1, b.special)    