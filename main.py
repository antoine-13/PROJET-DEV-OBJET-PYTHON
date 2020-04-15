###########################################################################################
#                                                                                         #
#                                                                                         #
#                                         Classe Main:                                    #
#                                                                                         #
#                           Rassemble les classes et gère la partie                       #
#                                                                                         #
#                                                                                         #
#                                                                                         #
###########################################################################################

#Importation des librairies
from Plateau import* 
from Partie import*
from menu import*
import webbrowser

#définition du main 
def main():

    #création des objets
    p = Partie()
    pl = Plateau()
    m = menu()

    #définition du choix à 0
    choix = 0

    #Tant que le choix n'est pas de lancer une partie 
    while choix != 1:
        m.affichage_main_menu()             #On affiche le menu
        choix = m.user_choix()              #On demande à l'utilisateur son choix
        
        if choix == 2:                      #Si son choix est de changer la taille
            pl.dimenssion = m.taille()          #On lui demande la taille qu'il veut
        elif choix == 3:                    #Si son choix est de changer le nombre de joueurs
           p.nbr_joueurs = m.nbr_joueur()          #On lui demande le nombre de joueurs
        elif choix == 4:                    #Si il veut connaitre les règles 
            webbrowser.open("http://www.ffothello.org/othello/regles-du-jeu/")  #On le redirige vers la page officiel avec les règles
        
        print("")   #saut de ligne

    #Une fois qu'il à lancer une partie on initialise la partie
    p.tab = pl.initialisation(nbr_joueurs=p.nbr_joueurs)

    #tant que la fin de partie n'est vérifié
    while pl.test(p.tab) == 0:
        p.joueurs()                                         #On définie qui joue 
        if pl.joueur_eliminer(p.tour, p.nbr_joueurs) == 0 : #Si le joueur n'est pas éliminé
            pl.affiche(p.tab, pl.dimenssion)                    #On affiche le plateau de jeu
            print("C'est à", p.joueurs_du_tour[0], "de jouer !")            #On affiche le nom du joueur qui doit jouer
            a = p.coup()                                                    #On lui demande ou il veux jouer 
        
        
            if p.validite_case(a, p.tab) == 0:                      #Si la case est vide
                possibilite, valid_dir_lg, valid_dir_cl = p.validite_pos(a, p.tab)                    
                if possibilite >= 1:                       #Si le coup est valide (qu'il retourne bien un pion adverse)
                    p.ajout_pion(a, p.tab)                                  #On ajoute son pion
                    p.inversement(p.tab, a, valid_dir_lg, valid_dir_cl)                                 #On retourne les pions encadrés 
                    p.tour += 1                                             #On passe au tour suivant 
                else:                                                   #Sinon
                    print("Merci de choisir un emplacement correct")        #On lui demande de choisir une position correcte

            else:                                                   #Sinon
                print("Cette emplacement est déjà pris !")              #On lui dis que la case est deja occupé

        else:                                           #Sinon on saute son tour 
            p.tour +=1
            
        
    #Quand la partie prend fin on affiche le tableau final
    pl.affiche(p.tab,pl.dimenssion)


main()