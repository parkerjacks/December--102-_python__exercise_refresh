#Given a height and width, input by the user, print a box consisting of * characters as its border.

from typing import Counter


width = int(input("Please type a value to represent width. "))
height = int(input("Please type a value to represent height ")) 
character = "*"
count = 1
empty_string=" "

for x in range(height): 

    #first and the last printfull list of characters
    if x == 0 or x == (height -1):
        print(character * width)
    #print character for the 1st and last in width    
    else:
        print(character + (empty_string * (width-2)) + character)
      