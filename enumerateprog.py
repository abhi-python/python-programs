list1 = ["rice", "chips", "cake", "chocolates"]
for index, item in enumerate(list1): # it will return the list item with index 0 to end.
    if index % 2 == 0:
        print(f"Please buy {item}")