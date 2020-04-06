def coup():
    coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
    return coord

choix = coup()
print(choix)