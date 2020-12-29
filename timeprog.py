import time
# initial = time.time() # it will return time tick
# k=0
# while(k<20):
#     print("abhilash")
#     time.sleep(2) # it will stop the excution for the given time
#     k = k+1
# print("while loop run in", initial-time.time(), "seconds")
# initial1 = time.time()    
# for i in range(45):
#     print("abhilash") 
# print("for loop run in", initial1-time.time(), "seconds")   

local_time = time.asctime(time.localtime(time.time())) # it will return the time.
print(local_time)