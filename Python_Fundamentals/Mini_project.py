"""1.create a python program that asks the user how far they want to travel. 
if they want to travel less than three miles tell them to ride Bicycle.
if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. 
if they want to travel three hundred miles or more tell them to driver Super-Car."""

# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

def far_you_travel(distance):
    if distance<0:
        return 
    if distance<3:
        return "Bicycle"
    elif distance>=3 and distance<300:
        return "Motor-Cycle"
    else:
        return "Super-car"
    
distance=int(input("Enter distance in miles: "))
print(f"The vehicle you should use for {distance} is ",far_you_travel(distance))

"""2.Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. 
you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
"""
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

def how_it_cost(amount):
    print("How much does it cost to operate one server per day?")
    print("The cost of operating sever per day=$",24*0.51)
    print("How much does it cost to operate one server per week?")
    print("The cost of operating sever per week=$",7*24*0.51)
    print("How much does it cost to operate one server per week?")
    print("The cost of operating sever per week=$",7*24*0.51)
    print("The cost of operating server per month=$",30*24*0.51)
    print(f"How much days can I operate one server with ${amount}")
    print("The number of days you can run server=",amount/(24*0.51)) 

amount=int(input("Enter the amount you have to run server="))
how_it_cost(amount)
