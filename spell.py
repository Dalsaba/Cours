class Spell:
    def __init__ (self,name,cost,degat):
        self.name = name
        self.cost = cost
        self.degat = degat

    def __str__(self):
        return f"L'attaque {self.name} vous épuisera {self.cost} points de magie sur {self.degat} !"

if __name__ == "__main__":
    spell = Spell(name ='Eclair',cost = 50,degat = 100)
    print(spell)
    print (spell.degat)