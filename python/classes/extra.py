class Monster:
    '''This monster has some attributes'''
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
        self._id =5
    
    def attack(self,strengths):
        print(f"Monster has attacked, with damage of {strengths}!")
        self.energy-=strengths

monster = Monster(100,95)

# hasattr and setattr functions
hasattr(monster, 'height') # hasattr(object,'attribute')
#returns value in booleans

setattr(monster, 'weapon','Super Punch') # setattr(object,'attribute','value')
#set value to attributes
# monster.height = 65 # also works
print(monster.weapon)