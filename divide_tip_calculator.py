
#take user input for level of service and bill amount and calculate total bill and divide it evenly by the number of people in party
total_friends = int(input("How many friends are in your dinner party : "))
total_bill = float(input("How much is your bill?  ")) 
level_service = input("Choose an option to represent your level of service: Good, Fair, or Bad  ")

#tip percentages base on service
service_good = .20
service_fair = .15
service_bad = .10

#make all values lower case for this variable 
level_service.lower()

#loop if value is not equal to a specified option
while level_service != "good" and level_service != "fair" and level_service != "bad": 
    level_service = input("please type a valid option ")
    level_service.lower() 

#condition to calculate total bill amount if the service is good
if level_service == "good": 
    total_bill = (total_bill + (total_bill * service_good)) / total_friends


#condition to calculate total bill amount if service is fair
elif level_service == "fair": 
    total_bill = (total_bill + (total_bill * service_fair)) / total_friends



#condition to calculate total bill amount if service is bad
else: 
    total_bill = (total_bill + (total_bill * service_bad)) / total_friends


#print the amount to the console
print(total_bill)
