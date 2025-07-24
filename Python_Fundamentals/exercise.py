# Q1. Write a program to check if a given number is Positive, Negative or Zero.

def pos_or_neg(a):
    a=int(a)
    if a>0:
        return "Positive"
    elif a<0:
        return "Negative"
    else:
        return "0"
    
a=input("Enter a number: ")
print("The number is:",pos_or_neg(a))

# Q2. Write a program to check if a given number is odd or even.

def even_or_odd(num):
    num=int(num)
    if num%2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("Enter a number: "))
print("The number is ",even_or_odd(num))

# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

def is_last_digit_same(num1,num2):
    if num1%10 ==num2%10:
        return True
    else:
        return False
    
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print("The numbers last digit is same or not: ",is_last_digit_same(num1,num2))

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

def fun():
    for i in range(1,11):
        print(i,end=" ")

fun()

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

def even():
    for i in range(23,57):
        if i % 2==0:
            print(i)
even()

# Q6. Write a program to check if a given number is prime or not.

def is_prime(num):
    a=False
    for i in range(2,num):
        if num%i==0:
            a= False
            break
        else:
            a= True
    return a

num=int(input("Enter the number: "))
result=is_prime(num)
print(f"The number {num} is prime or not: ",result)

# Q7. Write a program to print prime numbers between 10 and 99.

def prime():
    for i in range(2, 100):
        a = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                a = False
                break
        if a:
            print(i, end=" ")

prime()

# Q8. Write a program to print the sum of all the digits of a given number.

def sum_digit(num):
    quotient=num
    sum1=0
    while quotient:
        sum1=sum1+(quotient%10)
        quotient=quotient//10
    return sum1

a=int(input("Enter a number: "))
print("The sum of digits=",sum_digit(a))

# Q9. Write a program to reverse a given number and print.

def reverse_num(num):
    quotient=num//10
    reverse_num=num%10
    while quotient:
        reverse_num=(reverse_num*10)+ (quotient%10)
        quotient=quotient//10
    return reverse_num
    
num=int(input("Enter a number: "))
print("The reversed number is: ",reverse_num(num))

# Q10. Write a program to find if the given number is palindrom or not.

def is_palindrome(num):
    num = str(num)
    start = 0
    end = len(num) - 1
    while start < end:
        if num[start] != num[end]:
            return False
        start += 1
        end -= 1
    return True

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")
