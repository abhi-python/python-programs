def printabhi(str):
    return f"this is {str}"

def add (num1, num2):
    return num1 + num2

print ("and the name is", __name__)
if __name__ == "__main__": # it will excute only in this file. if import in another it will not excute.
    print (printabhi("abhilash"))
    n = add(5,6)
    print(n)