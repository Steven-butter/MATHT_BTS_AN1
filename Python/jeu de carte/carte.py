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
    print("p1 ", paquet1)
    print("P2 " , paquet2)
    return paquet1, paquet2
    



while continuer:

    ############ MENU ###########

    print("=== Menu moyenne ===")
    print("1. Mélanger paquet")
    print("2. Diviser paquet")
    print("3. ")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 Entrer les notes ############# OK

    if choix == "1":
        print(melanger(paquet,k))
    if choix == "2":
        p_melanger = melanger(paquet,k)
        print(p_melanger)
        print(diviser(p_melanger))


