import random
randomNumber = random.randint(1,99)

class Test:
    def __init__(self):
        self.name = 'Test Class'
        self.value = 25
    
    def doSomething(self):
        print('Watch me ne ne , This is from Test class in myMoudle file')

class Calculator:
    def __init__(self):
        print('Calculator Mode On')

    def sum(self,*num_list):
        sum = 0
        for num in num_list:
            sum += num
        return sum