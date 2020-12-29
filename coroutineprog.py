import time
def searcher():
    book = "This is the book of abhilash and the programming is good"
    time.sleep(4)
    while True:
        text = (yield) #This yield define that it is a coroutine
        if text in book:
            print("The text is in the book")
        else:
            print("The text is not in the book")   

search = searcher()
print("search started")
next(search) # This next method is used to start the coroutine.
print("Next method run..")
search.send("abhi")
input("Press any key")
search.send("roni")
search.close() # This will close the coroutine
search.send("roni")
