## Fuctions in python use 'def' while defining fuctions.
def testFuction():
    print('Hello')
    test=1+2
    print(test)

testFuction()

# Adding arguments and parameters to functions
def cal(num1,num2):
    sum= num1+num2
    print(sum)

cal(5,6)

#operations inside functions
def coolCal(num1,num2,operator):
    if(operator=='plus'):
        results = num1+num2
        print(results)
    else:
        results = num1-num2
        print(results)

coolCal(5,6,'plus')


## Assigning arguments to perameters

def assginArgs(arg1,arg2,arg3,arg4='Arg 4'):
    print(arg1,arg2,arg3,arg4)

assginArgs(1,'TEST',[9.35,'Hello'],'nice to replace you arg4')
assginArgs(arg3=1,arg2='TEST',arg1=[9.35,'Hello'])
assginArgs(1,arg3='TEST',arg2=[9.35,'Hello']) ## positional arguments
assginArgs(1,arg3='TEST',arg2=[9.35,'Hello'],arg4="whaaattt!!!") ## Override default parameters

print("")
print("")
#list unpacking ,working with multiple arguments
def printAll(first,*args):
    print(first)
    print(f"   {args}")
    for arg in args:
        print(arg)

printAll(526,36,1,8,5,'ash',8502,655)
print("")
##keyword unpacking
def keyPrint(**args): #takes and work with keyvalue pair
    print(args)

keyPrint(aarg1="super",key=2,key3='value pair')