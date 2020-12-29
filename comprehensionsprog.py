# comprehensions are used to create list, dictionary, sets, generators in one line.

# ...............list comprehension..................
# ls = [i for i in range (100) if i%3==0]
# print(ls)

#..............Dictionary comprehension............
# dict1 = {i: f"item{i}" for i in range(10) if i%2==0}
# dict1 = {i: f"item{i}" for i in range(5)}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

#...........set comprehension........
# dresses = {dress for dress in ["dress1", "dress2","dress1", "dress2","dress1", "dress2"]}
# print(dresses)

#..............generator comprehension.........
evens = (i for i in range(100) if i%2==0)
for item in evens:
    print(item)