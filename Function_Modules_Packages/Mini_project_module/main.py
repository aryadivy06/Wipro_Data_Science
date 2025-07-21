import countvowels
import frequency_letter
import ispalindrome

name=input("Enter a string: ")
print("The string is plaindrome:",ispalindrome.is_palindrome(name))
print("The number of vowels in string:",countvowels.count_the_vowels(name))
print("Frequency of letters:",frequency_letter.frequency(name))
