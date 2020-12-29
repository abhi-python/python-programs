'''
Dictionary- It is used to store key value pairs.
   1. del- delete the key value.
   2. copy- create another copy of that dictionary.
   3. get- fetch the key value of given item.
   4. update- add new item to the dictionary.
   5. keys- print all the keys of dictionary.
   6. items- print all the key values of dictionary.
d1 = {"Abhi": "Burger", "Shreya": "Chowmin", "Aman": "Rice", "Akash": "Dal",
        "Tulsi":{"B":"Meggie", "L":"Roti", "D":"Chicken"}}
d1["Arpit"] = "Pizza"
del d1["Arpit"]
d2 = d1.copy()
#print(d1["Tulsi"])
#print(d1.get("Abhi"))
d1.update({"Leena":"Toffee"})
#print(d1.keys())
print(d1.items())
'''
d3 = {15:"shreya", 20:"tanu", 25:"rohit", 30:"shanu",
     35:{"harry":"football", "rohan":"basketball", "mohit":"tennis"}}
#print(d3[35]["harry"])
d3[40] = "mini"
del d3[40]
d3.update({40:"mini"})
#print(d3.keys())
#print(d3.get(30))
print(d3.items())