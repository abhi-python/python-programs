'''a= int(input("Enter A\n"))
b= int(input("Enter B\n"))
print("A is greater than B") if a>b else print("B is greater than A")'''

'''numbers=[1,2,3,4,5,6,7]
for number in numbers:
    if number==3:
        pass
    elif number==4:
       pass
    elif number==5:
        pass
    else:
        print(number)'''
for i in range(1,8):
    if i==3 or i==4 or i==5:
        continue
    else:
         print(i)    