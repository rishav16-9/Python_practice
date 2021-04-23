import random

class spell:
    def __init__(self, Name, cost, dmg, property):
        self.Name = Name
        self.cost = cost
        self.dmg = dmg
        self.property = property
        
    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
        
    
    