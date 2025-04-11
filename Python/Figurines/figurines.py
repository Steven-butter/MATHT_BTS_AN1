import random

continuer = True
collection = [0,0,0,0,0,0,0,0,0,0]

### Verifi si il a obtenu la figurine

def deja_obtenu(collection):
    res = True
    for i in range(1,10):
        if collection[i] == 0:
            res = 0
    return res

### fonction ajoute
### choisi un random entre 0 et 9 et met a jour la valeur dans le tableau collection

def ajoute(collection):
    fig = random.randint(0,9)
    collection[fig] += 1

### fonction test achat
### Test le nombre d'achat pour avoir toute la collection

def test(collection):
    nb_achat = 0
    col_comp = True
    while col_comp:
        if all(val != 0 for val in collection):
            col_comp = False
        ajoute(collection)
        nb_achat += 1
    return nb_achat
    



while continuer:

    ############ MENU ###########

    print("=== Menu code pin ===")
    print("1. Faire un nouveau tirage")
    #print("2. Tirage")
    print("3. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 VERIFIER PIN INPUT DIRECT ############# OK

    if choix == "1":
        print(collection)
        achat = test(collection)
        print(achat)


    ########## ################# OK

    #if choix == "2":

    ###########  Quitter  ##############

    if choix == "3":
        continuer = False