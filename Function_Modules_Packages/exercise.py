""" Write a function to return the sum of all numbers in a list.  
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""

def sum_li(li):
    sum1=0
    for i in li:
        sum1=sum1+i
    return sum1

li=list(map(int,input().split(" ")))
res=sum_li(li)
print("The sum of list element= ",res)

""" Write a function to return the reverse of a string.  
Sample String : "1234abcd"
Expected Output : "dcba4321" """

def rev_str(str1):
    return str1[::-1]
str1=input("Enter a string: ")
res2=rev_str(str1)
print(res2)

"""Write a function to calculate and return the factorial of a numner"""

def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)

num=int(input("Enter a number: "))
res3=fact(num)
print(f"The factorial of number {num}  is {res3}")

"""Write a function that accepts a string and prints the number of
upper case letters and lower caseletters in it."""

def count_up_lo(str3):
    up=0
    lo=0
    for i in str3:
       if i.isupper():
          up=up+1
       else:
          lo=lo+1
    return up,lo

str3=input("Enter a string ")
res4=count_up_lo(str3)
print(f"The upper case letters are {res4[0]} and lowercase letters are {res4[1]}")

"""Write a function to print the even numbers from a given list.
List is passed to the function as an argument."""

def even_li(li3):
    li4=[]
    for i in li3:
        if i%2==0:
            li4.append(i)
    return li4

li3=list(map(int,input().split(" ")))
print(even_li(li3))

"""Write a function that takes a number as a parameter
and checks the number is prime or not"""

def is_prime(num4):
    for i in range(2,num4//2):
        if num4%i==0:
            return False
    return True

num4=int(input("Enter a number: "))
print("The number is prime:",is_prime(num4))
