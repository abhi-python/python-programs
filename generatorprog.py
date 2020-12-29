'''
iterable- In which __iter__() and __getitem__() method is defined.
iterator - In which __next__() method is defined.
iteration - traversing a object. 
'''
def gen(n):
    for i in range(n):
        yield i # it will create a generator.

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

a = "abhi" #str object is iterable and int is not iterable
b = a.__iter__()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
# print(b.__next__())