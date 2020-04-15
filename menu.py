###########################################################################################
#                                                                                         #
#                                                                                         #
#                                           Classe menu:                                  #
#                                                                                         #
#                           affiche et demande ce que l'utilisateur                       #
#                           veux faire au début                                           #
#                                                                                         #
#                                                                                         #
###########################################################################################

class menu:

    #définition de la classe qui affiche les différentes possibilitées du menu
    def affichage_main_menu(self):
        print("1-Lancer une partie")
        print("2-Changer la taille du plateau (default : 8*8)")
        print("3-Changer le nombre de joueurs (default : 2)")
        print("4-Règles de jeu")

    #Demande d'entree à l'utilisateur le choix qu'il souhaite faire
    def user_choix(self):
        choix = int(input("Que souhaitez vous faire : "))
        return choix

    #Demande du nombre de joueur
    def nbr_joueur(self):
        joueurs = 0

        #tant que l'utilisateur ne donne pas un nombre entre 4 et 2 on continue de lui demander pour qu'il rentre un nombre valide
        while joueurs > 4 or joueurs < 2:
            print("")
            joueurs = int(input("Saisissez votre nombre de joueurs (entre 2 et 4) : "))
        return joueurs

    #Demande de la taille que l'utilisateur souhaite
    def taille(self):
        test_taille = 0

        #Tant que le test de la taille n'est pas correct on continue de demander
        while test_taille == 0:
            print("")
            user_taille = input('Quel taille de plateau souhaitez vous ? (entrez la taille de la forme longeur*largeur, avec un max de 20 et un min de 8)').split("*",)

            if int(user_taille[0]) > 20 or int(user_taille[1]) > 20 or int(user_taille[0]) < 8 or int(user_taille[1]) < 8: #verifie si la taille demander est entre 8 et 20
                test_taille = 0
            else:
                test_taille = 1

        return user_taille