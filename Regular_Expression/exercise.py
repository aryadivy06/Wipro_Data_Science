#1)Write a program to find check if a string has only octal digits. 
#Given string ['789','123','004']

strin=['789','123','004']

def is_octal(st):
    for i in st:
        if i in "89":
            return False
    return True

for i in strin:
    if is_octal(i):
        print(f"{i} contains only octal digits.")
    else:
        print(f"{i} does not contains only octal digits.")
    


#2)Extract the user id, domain name and suffix from the following email addresses. 
#emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""

import re

emails = "zuck@facebook.com sunder33@google.com jeff42@amazon.com"
pattern= r'(\w+)@(\w+)\.(\w+)'

matches=re.findall(pattern,emails)

for i in matches:
    print(f"User id={i[0]}, Domain Name={i[1]}, Suffix={i[2]}")
   

"""3)Split the following irregular sentence into proper words sentence = A, 
very very; irregular_sentence expected output : A very very irregular sentence """

sentence="A, very very; irregular_sentence"

correc_sentence=re.sub(r'[^\w\s]|_',' ',sentence)
correc_sentence=re.sub(r'\s+',' ',correc_sentence).strip()
print(correc_sentence)

"""4)Clean up the following tweet so that it contains only the user’s message. 
That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. #tweet = '''Good advice! RT @TheNextWeb: What I would do 
differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' ##desired_output = 'Good advice 
What I would do differently if I was learning to code today'"""

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub(r'RT\s+', '', tweet)                    
tweet = re.sub(r'cc:', '', tweet)                      
tweet = re.sub(r'http\S+', '', tweet)                   
tweet = re.sub(r'@\w+', '', tweet)                      
tweet = re.sub(r'#\w+', '', tweet)                     
tweet = re.sub(r'[^\w\s]', '', tweet)  

print(tweet)
"""5)Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.
html Code to retrieve the HTML page is given below: import requests r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text 
 html text is contained here desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 
'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']"""

import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
text =  re.findall(r'>([^<>\n]+)<',html)
text=[te.strip() for te in text if te.strip()]
print(text)

#6)Given below list of words, identify the words that begin and end with the same character. civic trust widows maximum museums aa as
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in words if word[0].lower() == word[-1].lower()]

print(matching_words)

