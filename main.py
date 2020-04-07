from Plateau import* 
from Partie import*


def main():
    p = Partie()
    pl = Plateau()
    p.tab = p.initialisation()

    while pl.test(p.tab) == 0:
        pl.affiche(p.tab)
        choix_menu = p.menu()
        
        if choix_menu == 1 or choix_menu == 2:
            a = p.coup()

            if p.validite(a, p.tab) == 0:
                p.ajout_pion(a, p.tab, choix_menu)
                p.inversement(p.tab, a, choix_menu)

            else:
                print("Cette emplacement est déjà pris !")

    pl.affiche(p.tab)


main()