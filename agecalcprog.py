age = int(input("Enter your age or birth year : "))
isage = False
isyear = False
if len(str(age)) == 4:
    isyear = True
else :
    isage = True

if (age<1900 and isyear):
    print("You seems to be oldest person alive")
    exit()

if age>2020:
    print("You are not yet born")
    exit()

if isage:
    age = 2020 - age

print(f"You will be 100 years old in {age + 100}")

instersetedYear = int(input("Enter year you want to know your age in : "))
print(f"You will be {instersetedYear - age} years old in {instersetedYear}")
