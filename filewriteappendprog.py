# f= open("abhi1.txt", "w")
# f.write("I am a good boy.")
# f.close()

# f= open("abhi1.txt", "a")
# f.write("I love to sing music\n")
# f.write("I am a rider\n")
# f.close()

# Handle file in read and write mode both
f= open("abhi2.txt", "r+")
# f.write("I am a fun loving and careless\n")
content= f.read()
print(content)
f.close()
