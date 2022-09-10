class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    def damage(poison_damage):
        print(f"Damage taken by monster {poison_damage}")

class Scorpion(Monster):
    def __init__(self,health,energy,attack):
        self.attack = attack
        # Monster.__init__(self,health,energy)  #old syntax
        super().__init__(health,energy)
        
    def damage(self,poison_damage):
        print(f"Damage taken by Scorpion {poison_damage}")
        self.health -= poison_damage
        self.energy -= poison_damage
        print(f"Current health: {self.health} and energy: {self.energy}")
    
scorpion = Scorpion(100,80,50)
print(scorpion.energy)
print(scorpion.health)
scorpion.damage(50)