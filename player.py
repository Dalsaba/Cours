import random
from Classes.color import Color

class Player:
    dead = False
    def __init__ (self, name, hp, atk,sorts, mp):
        self.mp = mp
        self.mp_max = mp
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.sorts = sorts
        # self.dead = False

    def generate_damage(self):
        """
        génére un dégat aléatoire compris entre l'attaque haute (atkh)
        et l'attaque basse ( atkl) .
        Retourne la valeur de ce dégat
        :return:

        choix liste sort
        coix atk ou mp
        modif fin de tour pr que lenneoy puisse attaquer
        dans player : partie reduced mp
        """
        return random.randrange( self.atkl, self.atkh )

        

       # spell_choisi = random.choice(self.spell)
        #return spell_choisi.degat

    def take_damage(self, degat):
        """
        prend un degat en paramètre et le fait encaisser au hp du joueur
        si celui si est en hp négative après l'encaissement du dégat alors
        on passe son status de joueur dead à True.
        :return:
        """
        self.hp -= degat
        if self.hp <= 0:
            self.dead = True


    def __str__(self): #str = pr afficher
        return f"{self.name} :  {Color.RED} {self.hp}/{self.max_hp}"\
                f"{Color.ENDC} Vie"


    def __gt__(self, other):
        """
        comparez des players
        :param other:
        :return:
        """
        return self.hp > other.hp


"""

import random
création de la classe personnage
mon personnage a un nom, une vie et un niveau d'attaque
class Player:
    dead = False
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp #vie
        self.max_hp = hp
        self.atk = atk
        self.atkh = atk + 10
        self.atkl = atk - 10
        #self.dead = False
    def generate_damage (self) :

        génère un dégat aléatoire compris entre l'atkh et l'atkl
        retourne la valeur de ce dégat

        return random.randrange(self.atkl,self.atkh)
    def take_damage (self,degat):

        prend un dégat en paramètre et le fait encaisser au hp du joueur
        si celui-ci est est un hp négatif après l'encaissement du dégat alors
        on passe son statut de dead à True

        :return:


        self.hp = degat
        if self.hp <= 0 :
            self.dead = True

        def __str__ (self):
            return f"{self.name} : {self.hp}/{self.max_hp} Vie"

        def __gt__ (self,other) :


            comparez des players

            return self.hp > other.hp

    if __name__ == "__main__" : #pour le tester qd il n'est pas importer. 
        player = Player(name = "Lucy", hp = 500, atk = 60)
        enemy = Player(name="Méchant", hp = 700, atk = 40)

        degat = player.generate_damage()
        print(degat)
        enemy.take_damage (degat)
        print (enemy)
        assert enemy.hp == enemy.max_hp - degat
        __

"""


