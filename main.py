from Classes.jeu import Jeu
from Classes.player import Player
from colorama import init
from Classes.spell import Spell


def main():

    #definition de la liste des sorts
    m1 = Spell(name="Boule de feu", cost=10, degat=60)
    m2 = Spell( name="Grèle", cost=15, degat=80 )

    #creation de la liste  de sorts
    spells = m1, m2 #tuple

    # definitions des joueurs
    player = Player(name="Lucy", hp=500 , atk = 60, sorts=spells, mp=100)
    enemy = Player(name="Méchant", hp=700, atk=40, mp = 30, sorts=spells)

    game = Jeu.load()
    if game :
        print('Reprise de la partie non terminée')
    else :
        print ('Nouvelle partie!')
        game = Jeu(player, enemy)

    # démarrage
    Jeu.start()

    # comparons les joeurs
    game.comparePlayer()

    game.round()


# quand le fichier est éxécuté
if __name__ == "__main__":
    ##initialisation
    init()
    # lancement du jeu
    main()