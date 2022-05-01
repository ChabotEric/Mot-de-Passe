#coding:utf-8
# Programe pour générer des mots de passe
# administratif ou pédagogique.
# Auteur: Eric Chabot
# 2021-05-26

import tkinter
from fonctions import *
import clipboard

# Observateur:
def updatemDp(*args):
    mDp.set(adm())
    copie = str(mDp.get())
    clipboard.copy(copie)

def copiemDp(*args):
    copie = str(mDp.get())
    clipboard.copy(copie)

# Création et paramètrage de la fenêtre:
app = tkinter.Tk()
app.title("Mot de passe 4.2")
app.geometry("400x300")

# Création du câdre (frame):
frame1 = tkinter.Frame(app, width = 400, height = 150)
frame1.pack(side = "top")

frame2 = tkinter.Frame(app, width = 400, height = 100)
frame2.pack(side = "top")

frame3 = tkinter.Frame(app, width = 400, height = 50)
frame3.pack(side = "top")

# Variables:
iconeCopie = tkinter.PhotoImage(file = "imageCopie.png")
mDp = tkinter.StringVar()

# Widgets:
bouton = tkinter.Button(frame1, text = "Générer un mot de passe", command = updatemDp, width = 25, bg = "lightgray")

labelmDp = tkinter.Entry(frame2, justify = "center", state = "readonl", textvariable = mDp, width = 15, borderwidth = 1, relief = "ridge", font = ("verdana italic", 12))

boutonCopie = tkinter.Button(frame2, command = copiemDp, image = iconeCopie)

labelInfo = tkinter.Label(frame3, text = "Copié automatiquement dans le presse-papier !", font = ("verdana italic", 7))

bouton.pack(pady = 50)
labelmDp.pack(side = "left", ipady = 3)
boutonCopie.pack(side = "left", padx = 4)
labelInfo.pack(pady = 7)

# Boucle principale
app.mainloop()




	
