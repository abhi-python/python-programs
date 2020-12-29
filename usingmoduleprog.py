import random
random_number= random.randint(1,5) # it print a random integer number for given range.
# print(random_number)
number= random.random()*100 # it print random number from 0 to 1 but multiply by 100 gives no. 0 to 100
#print(number)

lst = ["abhi", "rohit", "akash", "aman"]
choice = random.choice(lst)
print(choice)