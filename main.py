from Plateau import* 
from Partie import*
from menu import*
import webbrowser


def main():
    p = Partie()
    pl = Plateau()
    m = menu()
    choix = 0

    while choix != 1:
        m.affichage_main_menu()
        choix = m.user_choix()
        
        if choix == 2:
            pl.dimenssion = m.taille()
        elif choix == 3:
           p.nbr_joueurs = m.nbr_joueur()
        elif choix == 4:
            webbrowser.open("http://www.ffothello.org/othello/regles-du-jeu/")
        
        print("")

    
    p.tab = pl.initialisation(nbr_joueurs=p.nbr_joueurs)


    while pl.test(p.tab) == 0:
        if pl.joueur_eliminer(p.tour, p.nbr_joueurs) == 0 :
            p.joueurs()
            pl.affiche(p.tab, pl.dimenssion)
            print("C'est à", p.joueurs_du_tour[0], "de jouer !")
            a = p.coup()
        
        
            if p.validite_case(a, p.tab) == 0:
                if p.validite_pos(a, p.tab) == 1:
                    p.ajout_pion(a, p.tab)
                    p.inversement(p.tab, a)
                    p.tour += 1
                else:
                    print("Merci de choisir un emplacement correct")

            else:
                print("Cette emplacement est déjà pris !")

        else:
            p.tour +=1
            
        

    pl.affiche(p.tab,pl.dimenssion)


main()