'''i=0
while(True):
    if(i<5):
        i=i+1
        continue
    print(i+1, end=" ")
    if (i==44):
        i=i+1
        break
    i=i+1'''

while(True):
    inp=int(input("Enter a number"))
    if(inp>100):
        print("you enter a number greater than 100!")
        break
    else:
        print("Enter again!")
        continue