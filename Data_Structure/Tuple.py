"""Write a program to print the 4th element from first and 4th element from last in a tuple."""

a=(1,2,3,4,5,6,7)
if len(a)>4:
   b=int(input("Enter the place or element"))
   print(a[b-1],a[-b])
else:
   print("The tuple doesn't have enough elements.")

"""Write a program to check whether an element exists in a tuple or not."""
tup1=(1,2,3,4,5,6,6,7,23,4)
a1=int(input("Enter a number you want to check: "))
for i in tup1:
   if a1==i:
      print(f"The number {a1} exist")
      break
   else:
      print(f"The number {a1} not exist")

"""Write a program to convert a list into a tuple."""
lis7=(1,2,3,4,5,5,3)
lis7=tuple(lis7)
print(type(lis7))

"""Write a program to find the index of an item in a tuple."""

tup3=(1,2,3,4,5,5,3)
a2=int(input("Enter the number you want to check: "))
if a2 in tup3:
   print(tup3.index(a2))

"""Write a program to replace last value of tuples in a list to 100"""
list8=[(10,20,30),(40,50,60),(70,80,90)]
list9=[]
for i in list8:
   list9.append(list(i))
for i in list9:
   i[-1]=100
print(list9)
