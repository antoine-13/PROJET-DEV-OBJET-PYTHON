from Plateau import* 
from Partie import*


def main():
    p = Partie()
    pl = Plateau()

    dimenssion = p.taille()
    p.tab = pl.initialisation(dimenssion)
    tour = 0



    while pl.test(p.tab) == 0:
        tour += 1
        pl.affiche(p.tab, dimenssion)

        type_pion = tour % 2

        if type_pion == 1:
            print("C'est à X de jouer ! (", tour, " tours) ")

        elif type_pion == 0:
            print("C'est à 0 de jouer ! (", tour, " tours) ")
    
        a = p.coup()

        if p.validite(a, p.tab) == 0:
            p.ajout_pion(a, p.tab, type_pion)
            p.inversement(p.tab, a, type_pion)

        else:
            print("Cette emplacement est déjà pris !")

    pl.affiche(p.tab,dimenssion)


main()