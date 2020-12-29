# a = input("What is your name : ")
# b = input("your age : ")
# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello {a}")
c = input("Enter your name : ")
try:
    print(c)
except Exception as e:
    if c == "abhi":
        raise ValueError("abhi is blocked")
    print("Exception handled")    