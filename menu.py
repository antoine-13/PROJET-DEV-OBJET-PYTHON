class menu:
    def __init__(self):
        super().__init__()

    def affichage_main_menu(self):
        print("1-Lancer une partie")
        print("2-Changer la taille du plateau (default : 8*8)")
        print("3-Changer le nombre de joueurs (default : 2)")
        print("4-Règles de jeu")

    def user_choix(self):
        choix = int(input("Que souhaitez vous faire : "))
        return choix

    def nbr_joueur(self):
        joueurs = 0
        while joueurs > 4 or joueurs < 2:
            print("")
            joueurs = int(input("Saisissez votre nombre de joueurs (entre 2 et 4) : "))
        return joueurs


    def taille(self):
        test_taille = 0

        while test_taille == 0:
            print("")
            user_taille = input('Quel taille de plateau souhaitez vous ? (entrez la taille de la forme longeur*largeur, avec un max de 20 et un min de 8)').split("*",)

            if int(user_taille[0]) > 20 or int(user_taille[1]) > 20 or int(user_taille[0]) < 8 or int(user_taille[1]) < 8:
                test_taille = 0
            else:
                test_taille = 1

        return user_taille