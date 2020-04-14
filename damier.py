from tkinter import*
class Damier:
    def __init__(self):
        self.can1 = Canvas(fen1,bg='white',height=300,width=300)

    def ligne_de_carres(self, x, y, a):
        for i in range(0, 10):
            if a == 0:
                self.can1.create_rectangle(x,y,x+30,y+30,fill='black')
                self.can1.create_oval(x+2,y+2,x+28,y+28,fill='black', outline="black")
                a += 1
            elif a != 0:
                self.can1.create_rectangle(x,y,x+30,y+30,fill='white')
                self.can1.create_oval(x+2,y+2,x+28,y+28,fill='white', outline="white")
                a -= 1
            
            x = x + 30


    def dessiner(self):
        "dessiner dix lignes de carrés avec décalage alterné"
        y=0
        for lg in range(0,10):
            a = lg % 2
            x = 0
            self.ligne_de_carres(x, y, a)
            y = y + 30
                

    def effacer(self):
        self.can1.delete(ALL)

    def pion(self, evt):
        self.can1.selObject = self.can1.find_closest(evt.x, evt.y)
        self.can1.itemconfig(self.can1.selObject,fill ="red", outline=None) 
        

# Création du widget principal:
fen1 = Tk()

# Création des widgets :
d = Damier()
d.can1.pack(side=TOP, padx = 5, pady = 5)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='dessinner',command=d.dessiner)
bou2.pack(side=BOTTOM)
bou2 = Button(fen1,text='effacer',command=d.effacer)
bou2.pack(side=BOTTOM)
d.can1.bind("<Button-1>", d.pion)
fen1.mainloop()
fen1.destroy()