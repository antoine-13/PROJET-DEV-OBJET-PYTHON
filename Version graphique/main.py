from tkinter import*
import webbrowser


dimenssion = "8*8".split("*")
global rouge
global vert
global compteur_case_vide
global tab 
tab = [] 
global nbr_joueurs
nbr_joueurs = 2
global tour
tour = 0
global joueurs_du_tour 
joueurs_du_tour = [1] * 1
global non_joueurs 
non_joueurs = [1] * 3

def dessiner():
    "dessiner dix lignes de carrés avec décalage alterné"
    y=0
    for lg in range(1,9):
        a = lg % 2
        x = 0

        for cl in range(1, 9):
            if a == 0: #Si c'est une ligne paire on commence par un carré noir
                can1.create_rectangle(x,y,x+59,y+59,fill='black')

                if tab[lg][cl] == 1:   
                    can1.create_oval(x+5,y+5,x+53,y+53,fill='red', outline="black") #Si le tableau contient 1 on rempli avec un rond rouge
                elif tab[lg][cl] == 2:
                    can1.create_oval(x+5,y+5,x+53,y+53,fill='green', outline="black") #Si le tableau contient 2 on rempli avec un rond vert
                else: can1.create_oval(x+5,y+5,x+53,y+53,fill='black', outline="black") #Sinon on rempli avec la couleur du carré

                a += 1

            elif a != 0: #Si c'est une ligne impaire on commence par un carré blanc
                can1.create_rectangle(x,y,x+59,y+59,fill='white')

                if tab[lg][cl] == 1:
                    can1.create_oval(x+5,y+5,x+53,y+53,fill='red', outline="white") #Si le tableau contient 1 on rempli avec un rond rouge
                elif tab[lg][cl] == 2:
                    can1.create_oval(x+5,y+5,x+53,y+53,fill='green', outline="white") #Si le tableau contient 2 on rempli avec un rond vert
                else: can1.create_oval(x+5,y+5,x+53,y+53,fill='white', outline="white") #Sinon on rempli avec la couleur du carré

                a -= 1
            
            x = x + 60 #On ajoute 60 à x pour faire le carré de la collone suivante


        y = y + 60 #On ajoute 60 à y pour faire le carré de la ligne suivante

#Initialise la partie 
def initialisation():
    global tab, tour
    #Initialisation des variables avec les valeurs de base 
    tab = []
    tour = 0
    rouge = 2
    vert = 2
    reste = 60
    #On initialise les compteurs qui affiche le nombre de pions 
    nbb.configure(text = ("ROUGES : "+ str(rouge)))
    nbn.configure(text = ("VERT : "+ str(vert)))
    nbr.configure(text = ("RESTE : "+ str(reste)))
    #création du tableau
    i = int(dimenssion[1])
    j = int(dimenssion[0])

    message.configure(text = ("c\'est au Rouge de jouer"))

    #Création du tableau qui stocke l'emplacement des pions
    #On le crée avec 2 lignes et 2 colonnes en plus pour pouvoir éffectuer la vérification des coup lorsque l'on pose un pion sur une bordure 
    for a in range(0,i+2):      
        tab.append([0] * (j+2))

    #Place les pions de base
    tab[4][4] = 1
    tab[4][5] = 2
    tab[5][4] = 2
    tab[5][5] = 1

    #dessin du plateau
    dessiner()

#Dessine un pion à l'endroit souhaiter 
def pion(lg,cl):
    global tour, nbr_joueurs
    type_pion = tour % int(nbr_joueurs)

    #On selectionne l'objet le plus proche de la ou l'utilisateur souhaite jouer
    can1.selObject = can1.find_closest((cl-1) * 59 + 30, (lg-1) * 59 + 30)  

    if type_pion == 0:
        can1.itemconfig(can1.selObject,fill ="red", outline=None) #Si c'est au rouge de jouer on rempli le pion en rouge
    elif type_pion == 1:
        can1.itemconfig(can1.selObject,fill ="green", outline=None) #Si c'est au vert de jouer on rempli le pion en vert

#Fonction qui demande à l'utilisateur ou il souhaite jouer
def coup(evt):
    global tour, nbr_joueurs, joueur_du_tour, non_joueur

    type_pion = tour % int(nbr_joueurs)
    

    if type_pion == 0:
        joueurs_du_tour[0] = 1
        non_joueurs[0] = 2
        message.configure(text = ("c\'est au VERT de jouer"))

    elif type_pion == 1:
        joueurs_du_tour[0] = 2
        non_joueurs[0] = 1
        message.configure(text = ("c\'est au Rouge de jouer"))
    
    lg = int(evt.y/59)+1 #La ligne est egale à position de la souris en y diviser par 59 (taille d'un carré) plus 1 car int() arrondi à la valeur inférieur
    cl = int(evt.x/59)+1  #La colonne est egale à position de la souris en x diviser par 59 (taille d'un carré) plus 1 car int() arrondi à la valeur inférieur
    validite_case(lg, cl)
    
#Fonction qui vérifie si la case est vide ou non 
def validite_case(lg, cl):
    global tab
    #vérification si la case est déjà prise par un autre pion
    if tab[lg][cl] == 0:
        validite_pos(lg, cl) #Si elle est pas prise on appelle la fonction qui véifie la validité du coup
    else:
        message.configure(text = ("Cette emplacement déjà pris !")) #Sinonon affiche que la case est déjà prise                                                    
                                                           
def validite_pos(lg, cl):
    global tab
    #On initialise la variable possibilité a 0
    possibilite = 0

    #On crée deux tableau dans lequel on rentre toute les directions possibles dans les collones et lignes
    lg_add = [0, -1, +1]
    cl_add = [0, -1, +1]

    #On initialise deux tableaux dans lesquels on va stocker les directions valables dans lesquels
    #on pourra encadrer au moins un pion
    valid_dir_lg = []
    valid_dir_cl = []

    #On vérifie dans toute les directions en parcourant le tableau des directions des lignes, et collones
    #En fonction de la direction on verifie la case à coté contient un pion autre que celui qui joue
    #Si c'est le cas on continue dans la meme direction tant que le pion est différent de celui qui joue
    #Si on fini par croiser un pion correspondant à celui qui joue
    #On stoke dans le tableau des directions valide la direction dans laquels ont a chercher
    #On ajoute 1 a possibilité pour dire qu'il existe au moins une possibilité de retourner un pion minimum
    
    for a in lg_add:  
        for b in cl_add:                
            if tab[lg + a][cl + b] in non_joueurs:
                nlg = lg + a
                ncl = cl + b
                while tab[nlg][ncl] in non_joueurs:
                    ncl += b
                    nlg += a
                    if tab[nlg][ncl] in joueurs_du_tour:
                        valid_dir_lg.append(a)
                        valid_dir_cl.append(b)
                        possibilite += 1
    #Si il y a au moins une possibilité d'inverser
    if possibilite >= 1:
        inversement(lg, cl, valid_dir_lg, valid_dir_cl) #On inverse 
    else:
        message.configure(text = ("Cette emplacement est invalide")) #Sinon on affiche que le coup est invalide 
                           
#Fonction ajout_pion qui ajoute un pion à la position souaitez par l'utilisateur
def ajout_pion(lg, cl):
    global tab
    tab[lg][cl] = joueurs_du_tour[0]           #ajoute la valeur du pion qui joue à l'emplacement souhaitez
    pion(lg, cl)
                                                    
#Fonction inversement qui retourne les pions encadrés
def inversement(lg, cl, dir_lg, dir_cl):
    global tab, tour
    #Pour toute les index du tableau
    ajout_pion(lg, cl)
    for i in range (0, len(dir_cl)):
        nlg = lg + dir_lg[i]                                #On initialise la variable nlg en ajoutant la direction dans laquel on veux aller en ligne
        ncl = cl + dir_cl[i]                                #On initialise la variable ncl en ajoutant la direction dans laquel on veux aller en collone
        while tab[nlg][ncl] in non_joueurs:                #Tant que la case du tableau contient un pion qui ne joue pas
            ajout_pion(nlg, ncl)                          #On ajoute un pion à cette position
            nlg += dir_lg[i]                                                   #On ajoute les directions pour regarder la case à coter dans la direction souhaitez
            ncl += dir_cl[i]
    test()
    tour +=1
'''
def joueur_eliminer( tour, nbr_joueurs): #Fonction qui vérifie si un joueur est éliminer (pour le multi joueur)
    global rouge, vert, tour
    type_pion = tour % nbr_joueurs
    
    if type_pion == 1:
        if vert == 0:
            tour += 1
            

    elif type_pion == 0:
        if rouge == 0:
            tour += 1
'''

def test(): #Fonction qui gère la fin de partie 
    global tab, rouge, vert
    #gère la fin ou non de la partie
    rouge = 0
    vert = 0
    for a in tab: #parcours le tableau et compte le nombre de pions rouge et vert
        for b in a:
            if b == 1:
                rouge += 1
            elif b == 2:
                vert += 1

    reste = 60 - rouge - vert #Calcul le reste

    #Actualise les compteurs avec las valeurs calculées 
    nbb.configure(text = ("ROUGES : "+ str(rouge)))
    nbn.configure(text = ("VERT : "+ str(vert)))
    nbr.configure(text = ("RESTE : "+ str(reste)))
    
    if reste == 0: #Si toute les cases sont prises 
        compteurs = [rouge, vert]   
        maxi = max(compteurs)   #Stocke le max de pion 

        if rouge == maxi:   #Si les rouges ont plus de pions
            message.configure(text = ("LES ROUGES ONT GAGNE")) #On affiche que les rouges ont gagnés 
        
        if vert == maxi: #Si les vert ont plus de pions
            message.configure(text = ("LES VERTS ONT GAGNE"))  #On affiche que les verts ont gagnés 

    elif vert == 0 and rouge > 0: #Sinon si il n'y a plus de pions vert et il reste des pions rouges
        message.configure(text = ("LES ROUGES ONT GAGNE")) #On affiche que les rouges ont gagnés 

    elif rouge == 0 and vert > 0: #Sinon si il n'y a plus de pions rouges et il reste des pions verts
        message.configure(text = ("LES VERTS ONT GAGNE")) #On affiche que les verts ont gagnés 

def regles(): #Fonction qui redirige vers la page des règles
    webbrowser.open("http://www.ffothello.org/othello/regles-du-jeu/")
        
def propos(): #Fonction qui redirige vers la page officiel de l'othello
    webbrowser.open("http://www.ffothello.org/othello/")

def modif_joueur(): #Fonction qui crée la fenetre pour modifier le nombre de joueurs
    global nbr_joueurs
    fen2 = Tk()
    fen2.resizable(width=False, height=False)
    fen2.title("Changer le nombre de joueurs")
    b1 = Radiobutton(fen2, variable=nbr_joueurs, text="2 joueurs", value=2)
    b1.pack(side='left')
    b1.invoke()
    b2 = Radiobutton(fen2, variable=nbr_joueurs, text="3 joueurs", value=3)
    b2.pack(side='left')  
    b3 = Radiobutton(fen2, variable=nbr_joueurs, text="4 joueurs", value=4)
    b3.pack(side='left')
    bou1 = Button(fen2,text='Valider', command=fen2.destroy)
    bou1.pack(side=BOTTOM)
    
def modif_taile(): #Fonction qui crée la fenetre pour modifier la taille du plateau
    fen3 = Tk()
    fen3.geometry("200x50+300+0") 
    fen3.resizable(width=False, height=False)
    fen3.title("Changer la taille du plateau")
    E1 = Entry(fen3, width=200)
    E1.insert(0, "longueur*largeur")
    E1.pack()
    bou1 = Button(fen3,text='Valider', command=fen3.destroy)
    bou1.pack(side=BOTTOM)

def saut_tour(): #Fonction qui permet de sauter un tour si on clique sur le bouton "sauter son tour"
    global tour
    tour += 1       #ON ajoute 1 au tour 

    type_pion = tour % int(nbr_joueurs)

    #On change le message qui affiche qui doit jouer
    if type_pion == 0:
        message.configure(text = ("c\'est au Rouge de jouer")) 

    elif type_pion == 1:
        message.configure(text = ("c\'est au Vert de jouer"))

''' ebauche de la fonction qui permet de mettre en subrillance les endroit ou l'utilisateur peux jouer
def subbrillance():
    global tab, joueurs_du_tour, non_joueurs
    #On crée deux tableau dans lequel on rentre toute les directions possibles dans les collones et lignes
    lg_add = [0, -1, +1]
    cl_add = [0, -1, +1]

    #On initialise deux tableaux dans lesquels on va stocker les directions valables dans lesquels
    #on pourra encadrer au moins un pion
    valid_lg = []
    valid_cl = []

    lg = 0
    cl = 0

    for c in tab:
        lg += 1
        for d in c:
            cl += 1
            if d in non_joueurs:
                for a in lg_add:  
                    for b in cl_add:           
                        if tab[lg + a][cl + b] in joueurs_du_tour:
                            nlg = lg + a
                            ncl = cl + b
                            if a == 0 and b ==0:
                                break
                            else:
                                while tab[nlg][ncl] in joueurs_du_tour:
                                    ncl += b
                                    nlg += a
                                    if tab[nlg][ncl] not in joueurs_du_tour:
                                        print(nlg, ncl)
                                        valid_lg.append(nlg)
                                        valid_cl.append(ncl)
        cl = 0

    for i in range (0, len(valid_cl)):
        can1.selObject = can1.find_closest(valid_cl[i] * 60 + 30, valid_lg[i] * 60 + 30)
        can1.itemconfig(can1.selObject,fill ="green", outline="yellow")
'''



# Création du widget principal:
fen1 = Tk()
can1 = Canvas(fen1,bg='white',height=490,width=490)
fen1.title("OTHELLO")

menuBar = Menu()

menuFile = Menu(menuBar, tearoff=0)
menuFile.add_command(label="New game", command=initialisation)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=fen1.quit)
menuBar.add_cascade( label="Partie", menu=menuFile)


menuEdit = Menu(menuBar, tearoff=0)
menuEdit.add_command(label="Taille plateau", command=modif_taile)
menuEdit.add_separator()
menuEdit.add_command(label="Nbr joueur", command=modif_joueur)
menuBar.add_cascade(label="Paramètres", menu=menuEdit) 

menuHelp = Menu(menuBar, tearoff=0)
menuHelp.add_command(label="A propos", command=propos)
menuHelp.add_command( label="Règles", command=regles)
menuBar.add_cascade(label="Plus", menu=menuHelp) 

fen1.config(menu = menuBar)   


# Création des widgets :
can1.pack(side=TOP, padx = 10, pady = 10)
can1.bind("<Button-1>", coup)

fr =Frame(fen1, relief=SOLID)
nbb = Label(fr, text="ROUGES : ", width = 16, bg = "white", font="Arial 12")
nbb.pack(side=LEFT, padx=6, pady=5)
nbn = Label(fr, text="VERT : ", width = 16, bg = "white",font="Arial 12")
nbn .pack(side=LEFT, padx=6, pady=5)
nbr = Label(fr, text="Reste : ", width = 17, bg = "white",font="Arial 12")
nbr.pack(side=LEFT, padx=6, pady=5)
fr.pack(side=BOTTOM)

fr1 =Frame(fen1, relief=SOLID)
message = Label(fr1, text="Bonjour !", width=40, bg = "white", font="Arial 12")
message.pack(side=LEFT, padx=5, pady=5)
button = Button(fr1, text="sauter son tour", command=saut_tour)
button.pack()
fr1.pack()



fen1.mainloop()
fen1.destroy()