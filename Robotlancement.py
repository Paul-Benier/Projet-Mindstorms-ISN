########################################################################
########################################################################
                            #Partie de LOUIS#
########################################################################
########################################################################
from tkinter import* #module permettant de réaliser l'interface
import time  #module permettant d'utiliser des fonctions en rapport avec le temps
#Fonction evaluer pour prendre en compte les lettres inscrites puis les ecrire dans un fichier
def evaluer():
        ofi=open("fichiercaracteres",'w')
		#variable contenant tout les caractères réalisables par le robot
        listecarac = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?!<>()[],;./ 0123456789"
        varrejet, compteur = "", 0
        liste= []
        texte = str(entr1.get()) #prend en compte des chaines de characteres
        txt = texte.upper()#majuscules

        labelmesserreur.pack_forget() #cache le message d'erreur
        #vérifie si les caractère saisis par l'utilisateur sont réalisables
        for carac in txt:
            if carac not in listecarac and carac not in varrejet:
                varrejet = varrejet + " " + carac
                compteur += 1
        if compteur != 0: #si ce n'est pas réalisable, message d'erreur
            labelmesserreur.pack()
            labelmesserreur.config(text= "Votre phrase comporte des caractères non réalisables par le robot qui est/sont: " + varrejet)

        else:
            txt == ofi.write(txt)#ecrit dans le fichier
            ofi.close()
            lbldecompte.pack()
            lbltermine.pack_forget()
            bou1.pack_forget()
            decompte()


def decompte(count=15): #fonction decompte de 3 sec
        lbldecompte.config(text="Lancement dans " + str(count)+" sec") #str convertit des données en chaines
        if count > 0 :#actualiser le decompte afficher toute les secondes avec after
                fen.after(1000,decompte, count-1)
        if count==0: #a 0 une boucle se forme pour reutiliser le programme autant de fois que souhaiter
             lbldecompte.pack_forget()
             bou1.pack()
             lbltermine['text']="Tache effectué, voulez écrire autre chose ?"
             lbltermine.pack()


#10s envoie des lettres puis 20s par lettre === afficher programme terminer
#dessiner les caracteres sur tkinter
#esthetique du programme



                                #------ Programme principal ------#
# Création du widget principal ("maître") :
fen=Tk()
fen.title("Interface utilisateur du robot Mindstorm")

# création des widgets "esclaves" :
bou=Button(fen, text='Quitter',command=fen.quit, fg='red')
bou.pack()

entr1 = Entry(fen) # instanciation du widget
entr1.bind(evaluer)
entr1.pack()# application de la mise en page

bou1=Button(fen,text='Valider',command=evaluer, fg="blue")
bou1.pack()

flag=0
depart = 0

lbldecompte=Label(fen, fg='brown')
labelmesserreur = Label(fen, fg='red')

lbltermine=Label(fen, fg='red')

fen.mainloop()
fen.destroy()
