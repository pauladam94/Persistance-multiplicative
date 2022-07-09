# coding: utf8

"""
Ensemble de fonction avec la persistance
muliplicative

"""

def pm_nb(nb):
    resultat=nb
    compteur=0
    while len(str(resultat))!=1:
        liste =[int(j) for j in str(resultat)]
        compteur+=1
        resultat=1
        for i in liste:
            resultat*=i
    return(compteur)


# programme nombre finale persistace multiplicative
def pm_fin(nb):
    while len(str(nb))!=1:
        liste =[int(j) for j in str(nb)]
        nb=1
        for i in liste:
            nb*=i
    return(nb)


def pm_nb_fin(nb):
    res=[0,0]
    resultat=1
    resultat=nb
    compteur=0
#    print(resultat)
    while len(str(resultat))!=1:
        liste =[int(j) for j in str(resultat)]
        compteur+=1
        resultat=1
        for i in liste:
            resultat*=i
#        print(resultat)
    res[0]=nb
    res[1]=resultat
    return res


def aff_pm_nb_fin():
    w=0
    while w==0 or  w=="o" or w=="O":
        e=int(input("depart du nombre : "))
        c=int(input("   aller jusqu à : "))
        compt_spc=0
        pourcentage=0
        d=int(input("persistance multiplicative supèrieur à : "))
        for i in range(e,c):
            compt_spc+=1
            if compt_spc>=(c-e)/100:
                pourcentage+=1
                print("programme exécuté à ",pourcentage," % ")
                compt_spc=0
            a=pm_nb(i)
            if a[0]>=d:
                print("nb= ",i, "  pers mult : ",a[0],"  finit par: ",a[1])
        w=int(input("voulez vous continuez ? (Oui=0 NON=1)"))


def pm_gen(nb_max):
    liste=[[] for i in range(10)]
    for i in range(nb_max):
        a=pm_nb(i)
        for r in range(10):
            if a[1]==r:
                liste[r].append(a[0])
#    print(liste)
    for i in range(10):
        print("le prctge de persistance multiplicative finissant par ",i," est de " ,len(liste[i])*100/nb_max)
    for i in range(9):
        print(liste[i+1])

def aff_pm_gen():
    w=0
    while w==0:
        b=int(input("jusqu'a combien aller : "))
        pm_gen(b)
        w=int(input("voulez vous continuez ? (Oui=0 NON=1)"))

#def des couleurs
NOIR    = (0,0,0)
BLANC   = (255,255,255)
RED     = (255,0,0)
DEEPPINK= (255, 20, 147)
ORANGE  = (255, 69, 0)
YELLOW  = (255,255,0)
PURPLE  = (128, 0, 128)
GREEN   = (84,173,65)
AQUA    = (0, 255, 255)
NAVY    = (0, 0, 128)
BROWN   = (165, 42, 42)
BLUE    = (0,0,255)

#variable
COULEUR1=   [
YELLOW   ,
BLANC    ,
DEEPPINK   ,
BLUE     ,
GREEN    ,
 ORANGE,
PURPLE   ,
NAVY     ,
AQUA     ,
RED      ,
BLANC    ,
BROWN    ,
]


COULEUR2=[]
n=10
for i in range(n):
    a=int((n-i)*255/n)
    COULEUR2.append((a,a,a))

COULEUR3=   [
BLANC    ,
BLANC    ,
BLANC    ,
BLANC    ,
BLANC    ,
BLANC   ,
BLANC  ,
PURPLE ,
PURPLE    ,
PURPLE    ,
PURPLE    ,
PURPLE   ,
]


#  vérification rapide du module :
if __name__ == "__animation1__":
    print(pm_nb(77))
    print(pm_fin(125))
    pm_gen(30)
