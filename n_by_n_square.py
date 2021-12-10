#Prompt user for an interger; print out a square 

n = int(input("Please type a numeric value")) 
character = "|"
length = 1

# while isinstance(n, int):
#     n = int(input("not a numeric value "))

while length <= n: 
    print(character*n)
    length +=1 

