'''
string functions- 
  1. len-count the number of characters in a string.
  2. capitalize- Capital the first letter of the sting.
  3. upper- convert the string in upper case.
  4. lower- convert the string in lower case.
  5. isalnum- Return TRUE if all the words are alphanumeric in a string.
  6. isalpha- Return TRUE if all the words are alphabatic in a string.
string slincing using the index.
'''

mystr = "sHrEyA#is#a#good#girl"
#print(mystr)
#print(len(mystr))
#print(mystr[5])
#print(mystr[0:6])
#print(mystr[0:21])
#print(mystr[0:6:2])
#print(mystr[::-1])
#print(mystr.capitalize())
#print(mystr.isalnum())
#print(mystr.isalpha())
#print(mystr.upper())
#print(mystr.lower())
#tp = (5,8,10)
#print(type(tp))
x=mystr.split("#", 3)
print(x)
