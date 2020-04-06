from Plateau import* 
from Partie import*


def main():
    tab = Partie.initialisation()

    while Plateau.test(tab) == 0:
        Plateau.affiche(tab)
        choix_menu = Partie.menu()
        
        if choix_menu == 1 or choix_menu == 2:
            a = Partie.coup()

            if Partie.validite(a, tab) == 0:
                Partie.ajout_pion(a, tab, choix_menu)

            else:
                print("Cette emplacement est déjà pris !")


main()