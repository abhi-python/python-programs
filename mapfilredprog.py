# numbers = ["35", "15", "20"]
# numbers = list(map(int, numbers)) # map is used to apply any function to any list.
# numbers[1] = numbers[1] + 5
# print(numbers[1])
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a    
#  num = [2, 3, 5, 4]
# num = list(map(lambda x: x*x, num)
#  print(num)
# nums = [square, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), nums))
#     print(val)
# list1 = [2,4,3,1,5,3,4,7,8,9,10]
# def isgreaterthan_5(num):
#     return num>5
# gr_than5 = list(filter(isgreaterthan_5, list1))
# print(gr_than5)    

from functools import reduce
list2 = [1,2,3,4]
sum = reduce(lambda x,y: x+y, list2)
print(sum)