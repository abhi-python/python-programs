def dec1(func1):
    def execut():
        print("executing now")
        func1()
        print("executed")
    return execut
@dec1
def my_name():
    print("My name is abhi")
my_name()            