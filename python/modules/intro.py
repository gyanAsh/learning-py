# modules are extra piece of code that can be called 
# and used in the progarm.

import random ,string ,datetime
from math import floor as getFloor
# from random import *   -  imports all of the

#random - google them...
randomNumber = random.randint(0,100)
print(randomNumber)


# random from list
testList = [
    'Hello World',
    False,
    [1,2,3,59.2],
    59.36,
    88
]

print(random.choice(testList))
print("")

#string module
print(string.ascii_lowercase)
print("")

#floor import specific function from module
print(getFloor(8.9))
print("")

#get current datetime
print(datetime.date.today())