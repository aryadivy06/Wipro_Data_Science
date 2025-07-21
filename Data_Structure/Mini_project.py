"""1.Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people.
Also add an additional person and corresponding fact. Display the new list of people and facts.
Run the program multiple times and notice if the order changes."""

dic={"Jeff":"Is affraid of Dogs.","David":"Plays the piano","Jason":"Can fly an airplane"}
print(dic)
dic["Jill"]="Can Dance"
dic["Jeff"]="Is affraid of heights."
print(dic)

"""2.Given the participant's score sheet for your University Sports Day, you are
required to find the runner-up-score. You have scores. Store them in a list and
find the score of the runner-up."""

def runner_up(scores):
   scores.sort(reverse=True)
   for i in scores:
      if i!=scores[0]:
        return i

a=[2,3,6,6,5]
print("The runnerup score is:",runner_up(a))

        
"""3.You have a record of n students. Each record containd the student's name,and
their percent marks in Maths,Physics and Chemistry. The marks can be floating
values.You are required to save the record in a dictionary data type. 

Student's name is the key.Maarks stored in a list is the values. The user enter
the student's name. Output the average percentage marks obtained by that student"""

def average_marks(stu_marks,name):
   a=stu_marks[name]
   sum=0
   n=len(a)
   for i in a:
      sum=sum+i
   return sum/n

lis={"Krishna":[67,68,69],"Arjun":[70,98,63],"Malika":[52,56,60]}
name=input("Enter name of the student: ")
ans=average_marks(lis,name)
print(f"The average marks of {name} is {ans}")

"""4.Given a string of n words, help Alex find out how many times his name appears in the string."""

def count_str(str1,str2):
    str1=str1.split(" ")
    cou=0
    for i in str1:
     if str2 in i or i==str2:
        cou=cou+1
    return cou

str1="Hi Alex WelcomeAlex Bye Alex."
str2="Alex"
ans=count_str(str1,str2)
print("The result is ",ans)
