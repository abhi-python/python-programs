#iterative approach
'''def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact    
n= int(input("Enter a number\n"))
print(factorial(n))  '''

# recursive approach
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)    
n=int(input("Enter a number\n"))
print(factorial(n))        