class A:
    def met(self):
        print("I am in class A")

class B(A):
    def met(self):
        print("I am in class B")

class C(A):
    def met(self):
        print("I am in class C")

class D(B,C):
    pass
    # def met(self):
    #     print("I am in class D")
a = A()
b = B()
c = C()
d = D()
print(d.met())
