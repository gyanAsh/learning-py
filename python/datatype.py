print(float(2))
print(int(5.2))
print(1.1*3) # needs to be rounded else results can vary.
#round
print(round(2.4))
print(round(2.5))
print(round(2.6))

#multiline print;
test = 'Line 1: some text \nLine 2: some more text'
print(test)
multi_string= '''This is supposed to be
a multiline string the python'''
print(multi_string)
print("")
# Dynamic value in string
name='Tom'
age =50
greeting="Hey,I'm {}, and I'm {} years old.".format(name,age)
greeting_again="Hey,I'm {1}, and I'm {0} years old.".format(name,age)
greeting_again_again="Hey,I'm {one}, and I'm {two} years old.".format(one=name,two=age)
simple_greeting = f'This is {name}, and I\'ll be {age+1} next year old.'

#just to show how it works
print(greeting)
print(greeting_again)
print(greeting_again_again)
print(simple_greeting)
print("")
## List and Tuples
print("# list and tuples")
# Both can contain any kind of data
# (string, numbers, booleans, other lists/tuples & quite a bit more)
firstList = [1,2,3,4,'words']
firstList.reverse()
firstList.append(0)
firstList.append('minus one')
print(firstList)

print("")
firstTuple = (1,3,4,5.5,'this is tuple',[10,30,40,55.5])
print(firstTuple)
print(firstTuple[5][1])

#Exercise
exerciseList = ['first entry',[123,456,[0,'Hello : )']],'bye']
print(exerciseList[1][-1][1])

#extracting data from lists/tuples ( [start:end:step] )
testList = [1,2,3,4,5,6,7,8,9,10]
print(testList[0:8])
print(testList[0:8:2])
print(testList[8:0:-1]) 
print(testList[-1:4:-1])
print("")
print(testList[::2]) #every even position(!value) as steps == 2 
#and start-end 's default value is the 0-len 

#exercise
#start from 8 and 2, pick every second element
print(testList[-3:0:-2])

#unpacking
unpackList = [10,20,'Sword']
energy,health,weapon = unpackList
print(health)

#exercise
#swap value
value1 = 10
value2 = 'test'
value1,value2 = [value2,value1]
print(value1)

testString = "this is a test string"
strList = list(testString) #converts every character to list's element
print(''.join(strList)) #joining every element of the list with ( '' ) empty value
numList = [1,2,3,4]
print(str(numList).replace(',','').strip('[').strip(']'))

#Dictionary in python ( key:value ) pair
testDict = {'A':123,'B':[1,2,3],1:True}
print(testDict.keys())
print(testDict.items())

#converting a dict
print(tuple(testDict.values()))

## Indexing with dict 
print(testDict['A']) #Runtime error when the key is not found.
print(testDict.get('A')) #No runtime error when the key is not found.

##Exercise dictionary
## Use update() and add a new key value pair
testDict.update({'newKey':(1,2,3)})
testDict.update(C='test',d=1788)
testDict['J'] = 'john'
print(testDict)

# Set in python has to be unique values ( indexing and slicing does not work)
mySet = {1,2,3,4,4} #duplicate values will be exterminated
mySet.add(5)
mySet.remove(2)
print(mySet)

# for indexing in set, convert the set to another type
print(list(mySet)[0])

## Comparasion in Set
set1 = {1,2,3,4,4}
set2 = {4,5,6}
print(set1.union(set2))
print(set2 | set1)
print(set1.intersection(set2)) 
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)

testSetInList = [11,22,33,44,56,8,88,79,44,11,22,3]
print(set(testSetInList))

#Boolean (anything "empty or 0 or None" is false else true)
print(11 in testSetInList)
print('e' in 'hello')
print(4 not in [1,2,3])
print (not 1 == 10)
print(bool(1788))
print(bool(-788))
print(bool(0))
