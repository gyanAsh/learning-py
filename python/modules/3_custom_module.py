import myModule as myMod
print("")
# you can import all the variable and functions from the file as module
print(f"This \"{myMod.randomNumber}\" is comming from intro file")
print("")

test = myMod.Test()
test.doSomething()
print("")

calculator = myMod.Calculator()
print(f"Sum is: {calculator.sum(1,5,8,6,8,28,46,55)}")