import time
from functools import lru_cache

@lru_cache(maxsize=3) # it will create a cache of last 3 calls
def some_work(n):
    # some working is running which takes n time
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now running some work....")
    some_work(3)
    print("Done calling..")
    some_work(3)
    some_work(4)
    some_work(5)
    print("again called..")