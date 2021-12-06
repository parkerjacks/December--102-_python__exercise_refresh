""" Prompt the user for a day of the week just like 

the previous problem. But this time, 

print 'Go to work' if it's a work day 

and 'Sleep in' if it's a weekend day.

"""

day = int( input ( " Type a Day of the week 0 - 6 " ) )

if day == 1 or day <= 5: 
    print("Go to work!")

elif day == 0  or day <= 6: 
    print("Sleep in!")
