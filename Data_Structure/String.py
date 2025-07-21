"""Write a program to count the number of upper and lower case letters in a string."""

str5="Hello World"
up=0
lo=0
for i in str5:
   if i.isupper():
      up=up+1
   else:
      lo=lo+1
print(f"The uppercase letters are {up} and lower case letters are {lo}.")


"""Write a program that will checck whether a given string is palindrome or not."""
def is_palindrome(str6):
   sta=0
   end=len(str6)-1
   while sta<end:
      if str6[sta]!=str6[end]:
         return False
      sta=sta+1
      end=end-1
   return True

str6=input("Enter a string=")
res=is_palindrome(str6)
print(f"The given string is palindrome: {res}")

"""Given a string, return a new string made of n copies of the first 2
   chars of the original string where n is the length of the string. The 
   string length will be >=2. If the input is Wipro then output sholud be
   WiWiWiWiWi."""

str7=input("Enter a string: ")
n=len(str7)
print(str7[0:2]*n)

"""Given a string , if the first or last character is 'x' , return 
the string without those 'x' character, else return the string unchanged.
If the input is "xHix" ,then output is "Hi" """

str8=input("Enter a string: ")
if str8[0]=='x' and str8[-1]=='x':
   print(str8[1:-1])
else:
   print(str8)

"""Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
 You may assume that n is between 0 and the length of the string inclusive. 
 For example if the inputs are “Wipro” and 3, then the output should be “propropro”."""

def last_char(str9,f):
   return (str9[-(f):]*f)
str9=input("Enter a string: ")
f=int(input("Enter a number beyween 0 and len of str9: "))
res=last_char(str9,f)
print(res)
