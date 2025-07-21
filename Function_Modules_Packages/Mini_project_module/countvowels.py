def count_the_vowels(name):
    count_vowel=0
    for i in name:
        if i in "aeiou" or i in "AEIOU":
            count_vowel=count_vowel+1
    return count_vowel
