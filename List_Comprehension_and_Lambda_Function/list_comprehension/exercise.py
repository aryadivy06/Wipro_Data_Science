"""1)Write a LC program to create an output dictionary
 which contains only the odd numbers that are present in the 
 input list = [1,2,3,4,5,6,7] as keys and their cubes as values"""

list=[1,2,3,4,5,6,7,8,9]
cube={x:x**3 for x in list if x%2!=0}
print(cube)

#2)Make a dictionary of the 26 english alphabets mapping each with the corresponding integer 
alpha_dic={chr(i+96): i for i in range(1,27)}
print(alpha_dic)
