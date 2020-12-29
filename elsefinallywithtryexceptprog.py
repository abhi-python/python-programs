f1 = open("abhi.txt")
try:
    f = open("doesnot.txt")
except EOFError as e:
    print("This is end of file error", e)
except IOError as e:
    print("This is input output error", e)    
else:
    print("This will excute when except is not running")    
finally:
    print("This will excute anyway")
    f1.close()    

print("Imortant stuff")        