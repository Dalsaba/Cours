import pickle
import os
from Classes.player import Player
from Classes.spell import Spell

class Jeu :

    path_save = "game.pkl"
    """
    classe representant logique du jeu
    prend en parametre deux playeurs
    """
    def __init__ (self, player :Player, enemy: Player) : #on type pr recuperer les données des players
        self.player = player
        self.enemy = enemy

    def whoWin (self):
        if self.player.dead :
            print ('Game over')
        elif self.enemy.dead:
            print('Bravo vous avez gagné')

    def endTurn (self):
        #enemy attaque physique
        degat = self.enemy.generate_damage()
        self.player.take_damage( degat )
        print( 'Le Méchant vous a infligé ', degat, 'points de dégats lui!' )
        #mdegat = self.enemy.generate_magic_damage()
        #self.player.take_damage(mdegat)


    def round (self):
        #tant que l'un des deux joueurs n'est pas mort
        while not self.player.dead and not self.enemy.dead: #tant que les deux sont en vie!
        #while not (self.player.dead or self.enemy.dead):
            #afficher des joueurs
            print(self.player,self.enemy) #grace a la fonction str, on verra leur vie :D
            #demande au joueur de choisir une action
            choice = input ('Voulez-vous attaquer avec votre épée (x), votre magie (c) ou ne rien faire (v)')
            if choice == 'x' :
                #Faire une attaque physique
                degat = self.player.generate_damage()
                self.enemy.take_damage (degat)
                print('Vous attaquez avec votre épée. Vous infligez', degat, 'points de dégats au Méchant!')
            elif choice == 'c' :
                i = 0
                print(dir(self.player))
                for spell in self.player.sorts:
                    print(i, spell)
                    i +=1
                magic_choice = input ('choix?')
                sort_choisi = self.player.sorts[magic_choice]
                self.enemy.take_damage(sort_choisi.degat)

            self.endTurn()
            self.save() #sauvegarde
        self.whoWin()
        Jeu.delete_save()  #efface la sauvegarde
    def start (): #c'est une methode statique car ça n'utilise pas de self. pr l'appeller on est obligé d'utiliser jeu.start
        print ('La partie commence!')
    def comparePlayer(self):
        if self.player > self.enemy :
            print('Vous devriez gagner')
        else :
            print ("Ca va être compliqué")

    def save(self): #ouverture du fichier, ecrire en mode binaire
        with open(Jeu.path_save, "wb") as fichier:  #wb car on veut l'ecrire et en mode binaie
            pickle.dump(self,fichier)

    @staticmethod
    def delete_save(): #spprime ma sauvegarde. C'est Statique et donc on met Statitc avant et on enleve le self
        os.unlink(Jeu.path_save)

    @staticmethod
    def load ():
        #es-ce que le fichier existe
        if os.path.exists(Jeu.path_save) :
            with open(Jeu.path_save, "rb") as fichier : #lecture en mode binaire = rb
                data = pickle.load(fichier)
                return data
        return None

