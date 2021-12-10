""" 
Write a program that will prompt you for how many coins you want. Initially you have no coins. 

It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally.  

If you type no, it will stop the program.

"""





coin_amount = 0 

print (f'You have {coin_amount} coins. ')

more_coins = input("Would you like more coins? Type Y = Yes Type N = No  ")
more_coins.lower() 

while more_coins != "y" and more_coins != "n": 
    more_coins = input("Please type a valid response!  ")

while more_coins == "y": 
    coin_amount += 1
    print (f'You have {coin_amount} coins.')
    more_coins = input("Would you like more coins? Type Y = Yes Type N = No  ")

    while more_coins != "y" and more_coins != "n": 
        more_coins = input("Please input a valid response!  ")

if (more_coins == "n"):
    print(f"Your total amount of coins is equal to {coin_amount}")
    
