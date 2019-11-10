# on importe les bibliotheques necessaires
import copy
import time
from tkinter import *
from random import *

def carre_magique_ale(n,prec):

    # initialisation de la liste et de l'interface graphique
    L=[]
    root=Tk()

    # on insere dans notre liste ainsi que sur l'interface les nombres qui seront sur les bords du carre
    for i in range(n):
        x=float(input("donner un nombre "))
        L.append(x)
        label=Label(root,width="10",height="4",text=str(L[i]),bg="white")
        label.grid(row=0,column=i+1)
    for i in range(n,2*n):
        x=float(input("donner un nombre "))
        L.append(x)
        label=Label(root,width="10",height="4",text=str(L[i]),bg="white")
        label.grid(row=i-n+1,column=n+1)
    for i in range(2*n,3*n):
        x=float(input("donner un nombre "))
        L.append(x)
        label=Label(root,width="10",height="4",text=str(L[i]),bg="white")
        label.grid(row=n+1,column=3*n-i)
    for i in range(3*n,4*n):
        x=float(input("donner un nombre "))
        L.append(x)
        label=Label(root,width="10",height="4",text=str(L[i]),bg="white")
        label.grid(row=4*n-i,column=0)

    # on initialise notre carre avec des zeros
    for i in range(n):
        L.append([0 for j in range(n)])
    deb=time.time()
    a=0
    y=0
    i=4*n
    j=0

    while a==0:
        y+=1

        # on utilise une deuxieme liste afin de realiser la comparaison entre deux iterations successives
        M =copy.deepcopy(L)

        h=i
        b=j

        #si on se trouve sur la premiere ligne du carre
        if i == 4*n:
            #si on se trouve sur la premiere colonne du carre
            if j==0:
                L[i][j]=(L[0]+L[4*n-1]+L[i][j+1]+L[i+1][j])/4
                x=randint(0,1)
                if x==0:
                    i=i+1
                else:
                    j=j+1
            #si on se trouve sur la derniere colonne du carre
            elif j==n-1:
                L[i][j]=(L[n-1]+L[n]+L[i][j-1]+L[i+1][j])/4
                x=randint(0,1)
                if x==0:
                    i=i+1
                else:
                    j=j-1
            else:
                L[i][j]=(L[j]+L[i][j-1]+L[i][j+1]+L[i+1][j])/4
                x=randint(0,2)
                if x==0:
                    i=i+1
                elif x==1:
                    j=j+1
                else:
                    j=j-1

        #si on se trouve sur la derniere ligne du carre
        elif i==len(L)-1:
            #si on se trouve sur la premiere colonne du carre
            if j==0:
                L[i][j]=(L[3*n-1]+L[3*n]+L[i][j+1]+L[i-1][j])/4
                x=randint(0,1)
                if x==0:
                    i=i-1
                else:
                    j=j+1
            #si on se trouve sur la derniere colonne du carre
            elif j==n-1:
                L[i][j]=(L[2*n]+L[2*n-1]+L[i][j-1]+L[i-1][j])/4
                x=randint(0,1)
                if x==0:
                    i=i-1
                else:
                    j=j-1
            else:
                L[i][j]=(L[3*n-j-1]+L[i][j-1]+L[i][j+1]+L[i-1][j])/4
                x=randint(0,2)
                if x==0:
                    i=i-1
                elif x==1:
                    j=j+1
                else:
                    j=j-1

        else:
            #si on se trouve sur la premiere colonne du carre
            if j==0:
                L[i][j]=(L[8*n-i-1]+L[i][j+1]+L[i-1][j]+L[i+1][j])/4
                x=randint(0,2)
                if x==0:
                    i=i-1
                elif x==1:
                    i=i+1
                else:
                    j=j+1
            #si on se trouve sur la derniere colonne du carre
            elif j==n-1:
                L[i][j]=(L[i-3*n]+L[i][j-1]+L[i-1][j]+L[i+1][j])/4
                x=randint(0,2)
                if x==0:
                    i=i-1
                elif x==1:
                    i=i+1
                else:
                    j=j-1
            else:
                L[i][j]=(L[i][j+1]+L[i][j-1]+L[i-1][j]+L[i+1][j])/4
                x=randint(0,3)
                if x==0:
                    i=i-1
                elif x==1:
                    i=i+1
                elif x==2:
                    j=j+1
                else:
                    j=j-1

        # si la difference entre le nombre atteint et lui-meme dans la seconde iteration est trop petite on s'arrete
        if ((L[h][b]-M[h][b])<= prec):
            a=1

    # on arrondit les resultats obtenus et on affiche notre carre
    for i in range(4*n,len(L)):
        for j in range(n):
            L[i][j]=round(L[i][j],2)
            if int(L[i][j])==L[i][j]:# Ces deux lignes sont optionnels
                L[i][j]=int(L[i][j]) # Elles servent à afficher les entiers sans ".0" à la fin
            label=Label(root,width="10",height="4",text=str(L[i][j]))# insertion dans l'interface graphique
            label.grid(row=i-4*n+1,column=j+1)
    fin=time.time()
    print(fin-deb,y)
    root.mainloop()
    return(L)

