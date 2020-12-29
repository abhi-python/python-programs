import pickle
#Pickling a file
# cars = ["Audi", "BMW", "Maruti", "Honda", "Ferrari"]
# file = "mycars.pkl"
# fielobj = open(file, "wb")
# pickle.dump(cars, fielobj)
# fielobj.close()

file = "mycars.pkl"
fielobj = open(file, "rb")
mycars = pickle.load(fielobj)
print(mycars)