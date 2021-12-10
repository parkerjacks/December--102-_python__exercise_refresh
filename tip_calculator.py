""" 
Your task is to write a program that calculates how much of a tip to leave at a restaurant.

Prompt the user for two things:

The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

good -> 20%
fair -> 15%
bad -> 10%

"""

bill_total = int(input("Enter in your bill total "))
service_level = str(input("Choose an option of your level of service: Good, Fair, or Bad " ))
service_level.lower()
print(f'service level variable is {service_level}')

service_Good = .20
service_Fair = .15
service_Bad = .10
tip_amount = 0 

# a = "good"
# b = "fair"
# c = "bad"

while service_level != "good" and service_level != "fair" and service_level != "bad": 

   service_level = input("please type in a valid response ")


if service_level == "good": 
    bill_total = bill_total + (bill_total * service_Good)

elif service_level == "fair": 
    bill_total = bill_total + (bill_total * service_Fair)

else: 
    bill_total = bill_total + (bill_total * service_Bad)

print(bill_total)
