# l=10 #Global Variable
# def function1(n):
#     global l # Global keyword to make any changes in global variable.
#     l=l+15
#     m=8 #local variable
#     print(l,m)
#     print(n, "This is printed")
# function1("My name is abhi")
# print(l)
x=95
def abhi():
    x=88
    def rohit():
        global x
        x=90
    print("before calling rohit()",x)  
    rohit()  
    print("after calling rohit()",x)    
abhi()
print(x)