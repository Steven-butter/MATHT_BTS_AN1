import random

paquet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
k=0
continuer = True

def melanger(paquet, k) :
    while k < 49 :
        i = random.randrange(0,13,1)
        j = random.randrange(0,13,1)
        temp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = temp
        k = k + 1
    return paquet


def diviser(p_melanger) :
    paquet1 = []
    paquet2 = []
    for i in range (0,int(len(p_melanger)),2):
        h = i+1
        paquet1.append(p_melanger[i])
        paquet2.append(p_melanger[h])
    #print("diviser p1 ", paquet1)
    #print("diviser p2 " , paquet2)
    return paquet1, paquet2
    
def partie(p1, p2):
    points1 = 0
    points2 = 0
    for i in range(0,7):
        if p1[i] > p2[i]:
            print("p1 gagne")
            points1 += 1
        elif p1[i] < p2[i]:
            print("p2 gagne")
            points2 += 1
            
    if points1 > points2:
        print("points p1 = ", points1)
        print("points p2 = ", points2)
        print("p1 gagne la partie")
    elif points1 < points2:
        print("points p1 = ", points1)
        print("points p2 = ", points2)
        print("p2 gagne la partie")
    else:
        print("Egalité")


while continuer:

    ############ MENU ###########

    print("=== Menu moyenne ===")
    print("1. Mélanger paquet")
    print("2. Diviser paquet")
    print("3. Jouer la partie")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 Entrer les notes ############# OK

    if choix == "1":
        print(melanger(paquet,k))
    if choix == "2":
        p_melanger = melanger(paquet,k)
        print(p_melanger)
        print(diviser(p_melanger))
    if choix == "3":
        p_melanger = melanger(paquet,k)
        p1 = diviser(p_melanger)[0]
        p2 = diviser(p_melanger)[1]
        #print("paquet1 = ",p1)
        #print("paquet2 = ",p2)
        print(partie(p1, p2))
    if choix == "4":
        continuer = False
        print("Au revoir")


