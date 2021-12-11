""" 1. "leetspeak"

Given a paragraph of text as a String, print the paragraph in leetspeak. It's a "clever" way to sound like a "hacker".

(See https://en.wikipedia.org/wiki/Leet for more information.)

To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

A -> 4
E -> 3
G -> 6
I -> 1
O -> 0
S -> 5
T -> 7

Example: If your program is given the String "I am a leet programmer", it should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation """

phrase = input("Please Type in a word or phrase to be translated into leetspeak.  ")
phrase.lower() 

phrase_list = []

for x in phrase: 

    if x in ("a", "e", "g", "i", "o", "s", "t"): 

        if x == "a": 
            phrase_list.append("4")

        elif x == "e": 
            phrase_list.append("3")

        elif x == "g": 
            phrase_list.append("6")

        elif x == "i": 
            phrase_list.append("1")

        elif x == "o": 
            phrase_list.append("0")

        elif x == "s": 
            phrase_list.append("5")

        elif x == "t": 
            phrase_list.append("7") 

    else: 
        phrase_list.append(x)


tuple(phrase_list)

phrase_list = "".join(phrase_list)

print(phrase_list)