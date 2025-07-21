"""Write a program to read the entire content from a txt file and display it to the user."""

with open("io.txt",'r') as file:
    text=file.read()

print(text)

"""Write a program to read first n lines from a txt file. Get n as user input."""

def read_n_lines(n):
    with open("io.txt",'r') as file:
          for i in range(n):
              n_lines=file.readline()
              if n_lines == "":
                    print("File has fewer than", n, "lines.")
                    break
              print(n_lines.strip()) 
m=int(input("Enter the number: "))
read_n_lines(m)

""" Write a program to accept input from user and append it to a txt file."""

wor=input("Enter the string=")
with open("test.txt",'a') as file1:
    file1.write(wor)

""" Write a program to read contents from a txt file line by line and store each line into a list"""

with open("io.txt",'r') as file2:
    lines=[line.strip() for line in file2]
    print(lines)

"""Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it."""

def longest_word(dic2):
    return max(dic2,key=len)

with open("test.txt",'r') as file:
    text=file.read().lower()
    words=text.split()
    dic2={}
    for word in words:
        if word not in dic2:
            dic2[word] = len(word)

o=longest_word(dic2)
print(o)

"""Write a program to count the frequency of a user entered word in a txt file."""

def frequency_word(str3):
    with open("io.txt",'r') as file5:
        text1=file5.read().lower()
        words1=text1.split()
        count=0
        for word in words1:
                if str3==word:
                    count =count+ 1
    return count

str3=input("Enter the string=")
re2=frequency_word(str3)
print(re2)
