#Print a triangle consisting of * characters like this:
"""  *
    ***
   ***** 
  ******* """

count = 1
character = "*"
mid_point = int((1 + 7)/2)
spaces = " "

for x in range(4): 
    print((mid_point * spaces) + (count * character))
    count += 2
    mid_point = mid_point - 1



