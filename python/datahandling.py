#Better for loop in python
names = [
    'Screws', 'Wheels','Metal parts','Rubber bits','Screwdrivers','Wood'
]
numbers =[5,6,2,3,8,9]

for things in zip(names,numbers): #zip combines both lists
    print(things[0],things[1])
            #or
print("")
for name, num in zip(names, numbers): #destructuring elements from zip
    print(name, num)

#enumerate function - get the current index
print("")
for thing in enumerate(names):
    print(thing)
    #or
print("")
for index, thing in enumerate(names):
    print(index, thing)
    if index+1 == len(names)//2:
        print("     We are half way there")

# COMBINATION of zip and enumerate
for index,thing in enumerate(zip(names, numbers)):
    print(f'{thing[0]} [id: {index}] - inventory: {thing[1]}')

        # List comprehension - create list in one line
print("")
#from
myList = []
for num in range(0,10):
    myList.append(num)
print(myList)
#two
myListOne = [num for num in range(0,10)]
print(myListOne)

#list comprehension with if operations
print("")
myListTwo=[num for num in range(0,10) if num % 2 == 0]
print(myListTwo)
#use if else before for loop
print("")
myListTwo=[num if num % 2 == 0 else 'odd' for num in range(0,10) ]
print(myListTwo)

#from first example
print("")
myTempList = [(name,num) for name,num in zip(names, numbers) if num<5]
print(myTempList)

#chess exercise
print("")
chessAlph = ['a','b','c','d','e','f','g','h']
chessNum = [1,2,3,4,5,6,7,8]

# chessBoard =[[(y,x) for x in chessNum] for y in chessAlph] 
        # or
# chessBoard =[[(y,x) for x in range(1,9)] for y in 'ABCDEFGH']
        #  actual chess board
chessBoard =[[(y,x) for x in range(1,9)] for y in 'ABCDEFGH'[::-1]] #reverse step counting
for row in chessBoard:
    print(row)

#   just like list comprehension you can create 
#   dict and set and tuple comprehension
#   example
print("")
print("dict ::")
dicComp = {num:num+17 for num in range(10)}
print(dicComp)
print("")
print("set ::")
setComp = {num for num in range(10)}
print(setComp)
print("")
print("tuple ::")
tupleComp = tuple(num for num in range(0,10))
print(tupleComp)

print("")
# sorting in python 
    # sorted(iterable,function) -> iterable:[list], func:asce/desc
print(sorted(numbers))
print(sorted(numbers,reverse=True)) #rev sort
print("")
list2=[('a',7),('m',20),('c',91),('b',47)]

# def sortFunc(item):
#     return item[1]

# print(sorted(list2,key=sortFunc))  

print(sorted(list2,key= lambda x:x[0])) #other way to do it

print("")
#map and filter in python
print(list(map(lambda x:x**2,numbers))) # map(function, list)
print("             Filter:")
print(list(filter(lambda x: True if x<5 else False,numbers )))

print("")
print(" File Handling")
#File handling in python
        ## open and close file manually

file = open('test.txt')
print(list(file))
file.close()

        ## open and close file automatically

with open('test.txt') as file:
    for line in list(file):
        print(line)

        ## write to File
with open('test.txt','a') as file:
    file.write('\n This is new text ha ha ha')

# delete things in python
a=10
del a
# print(a)  will show error as a is deleted

#       del list[index]
#       list.remove(index)
#       list.pop(index)
#       list.clear() --> to delete complete list