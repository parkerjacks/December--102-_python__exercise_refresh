""" 
2. Long words

Given a word as a string, print the result of extending any long vowels to the length of 5.

Examples:

Good => Goooood
Cheese => Cheeeeese
Man => Man
Spoon => Spooooon

Hint: Consider using a second variable.

"""

word  = input("Please type a word.") 

longWord = ""

count = 0 

for x in word: 


    if x in ("a", "e", "i", "o", "u") and count != (len(word) - 1) : 


        if x == word[count + 1]: 
            longWord = longWord + (3 * x) 

        else: 
            longWord = longWord + x
    
    else: 
        longWord = longWord + x 
    
    count += 1   


print(longWord) 

