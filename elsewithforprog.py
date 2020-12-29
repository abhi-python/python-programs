# khana = ["roti", "sabzi", "chawal"]
# for item in khana:
#     print(item)
# else:
#     print("This for loop ended poperly") #else only work with for loop when for loop ended normally without break statement. 

# uses of else with for loop like searching.

khana = ["roti", "sabzi", "chawal"]
for item in khana:
    if item == "Roll":
        break
else:
    print("Item was not found.")    