
# Project - Magic 8-Ball

import random

name = "Rob"
question = "Will it snow today?"
answer = ""
random_number = random.randint(1, 10)

# print(random_number)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidely so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "No!"
else:
    answer = "Error"

print(name + " asks: " +  question)
print("Magic 8-Ball's answer: " + answer)


# Project - Sal's Shipping
"""
weight = 25

# Ground Shipping
if weight <= 2:
    print("The cost for ground shipping is $" + str(weight * 1.50 + 20))
elif weight <= 6:
    print("The cost for ground shipping is $" + str(weight * 3.00 + 20))
elif weight <= 10:
    print("The cost for ground shipping is $" + str(weight * 4.00 + 20))
else:
    print("The cost for ground shipping is $" + str(weight * 4.75 + 20))

# Premium Shipping
print("The cost for premium shipping is $125")

# Drone Shipping
if weight <= 2:
    print("The cost for drone shipping is $" + str(weight * 4.50))
elif weight <= 6:
    print("The cost for drone shipping is $" + str(weight * 9.00))
elif weight <= 10:
    print("The cost for drone shipping is $" + str(weight * 12.00))
else:
    print("The cost for drone shipping is $" + str(weight * 14.25))
"""
# add some comments here
# these are more comments