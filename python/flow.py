x = 10
if x>10:
    print("This means it is true")
    print("stay inside the indentation to stay inside the flow")
elif x>5:
    print("in python elif is written for else if")
    print("And it works the same,Just make sure of the indentation")
else:
    print("This means it is false")
    print("This is works just like else statement")
print("")
if(True  and True) or False:
    print("This is how && and || is written in python")

print("")
if True:
    if not True:
        print("This is nesting") 
    else:
        print("This is else in nesting")

# match : works just like switch
mood = 'hungry'
match mood:
    case 'hungry': print("You are hungry !!")
    case 'thirsty': print("You are thirsty !!")
    case _: print("Works like default") #Works like default value

# while loop
j =10
while j>0:
    j-=1
    print(j)
    if j == 5:
        print("j is 5")

# break and continue works the same

# For loop

basicList = [1,2,3,4,5,6,7]
for x in basicList:
    print(f"print: {x}")

end = 3
for x in range(end):
    print(f"Range function: {x}")

for x in range(2,20,2): #range(start:stop:step)
    print(x)

print("")
#exercise
pList = [[10,40,20,50],[2,42,10],[101,10,4]]
for x in pList:
    for y in x:
        if(y < 50) and y>=10:
            print(y)
        elif y>100:
            break

print("")
# ternary operator
check =5
color = 'blue'if check == 15 else 'red'
print(f"color: {color}")
print(f"color: {'pink' if check==5 else 'black'}")
liste =1
print(liste == True)