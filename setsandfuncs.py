#s= set()
#print(type(s))
l= [1,2,3,4]
s1 = set(l)
#s1.add(5)
#s1.add(5)
#l2=[5,6,7,8]
#s3= {8,9,10,11}
#print(type(s3))
s2= s1.difference({5,6,7,8,3,4})
s3= s1.union({5,6,7,8})
s4= s1.intersection({5,6,3,4,7,8})
s5= s1.isdisjoint(s4)
print(s2, s3, s4, s5)
#s4=[5,6,8,9]
#set1=set(s4)
#print(set1)