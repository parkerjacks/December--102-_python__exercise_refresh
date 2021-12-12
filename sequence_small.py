""" 

Small

Vowels only, please

Prompt the user to enter a string.

Print out the letters they typed, but only the vowels.

Make sure your program handles both uppercase and lowercase letters. 

 """

word = input("Please type a word.  ")


vowel = ("a", "e", "i", "o", "u")

for x in word: 
    if x.lower() in vowel: 
        print(x) 


