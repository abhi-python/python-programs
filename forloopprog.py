'''list1= [["akki", 10], ["freak", 20], ["david", 30], ["carry", 40]]
mydict= dict(list1)
#for item in list1:
#    print(item)
for item, roll in mydict.items():
    print(item, "and roll no. is", roll)'''

list2= ["rohti", "ronny", 10, 3, 45, 30]
for item in list2:
    if str(item).isnumeric() and item>5:
        print(item)