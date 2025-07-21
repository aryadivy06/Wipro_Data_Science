"""Write a python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-seperated sequence after sorting
them alphabatically.

Constraints: All the colors will be completely in either lower case or upper case.
Sample Input 1: green-red-yellow-black-white
Sample Output 1: black-green-red-white-yellow"""

def color_sort(str1):
    li=str1.split("-")
    li.sort()
    str2="-".join(li)
    return str2
    
str1=input("Enter colors separated by hyphen ").lower()
res=color_sort(str1)
print(res)

