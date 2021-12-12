""" 

Medium

Tech Startup Name Creator

Prompt the user to enter a name for their tech startup.

Generate their tech startup name by removing the last vowel that comes before a non-vowel.

For example: "Bacon" becomes "Bacn" but "Shrubbery" becomes "Shrubbry"

When you print the name, make sure it prints out as a single word (not with one letter per line).""" 


word = input("Please type a word.  ")

vowels = ("a", "e", "i", "o", "u")

list_word = []

length_of_word = len(word) 

count = length_of_word - 1

list(word)

for x in word: 
    list_word.append(x)

for x in range(length_of_word): 
    if word[count] in vowels:
        list_word.pop(count) 
        count -= count
        break

print(list_word)



