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
    print(fig)
    collection[fig] += 1

### fonction test achat
### Test le nombre d'achat pour avoir toute la collection

def test(collection):
    col_comp = True
    while col_comp:
        ajoute(collection)
        if collection == [1,1,1,1,1,1,1,1,1,1]:
            col_comp = False
    



while continuer:

    ############ MENU ###########

    print("=== Menu code pin ===")
    print("1. Faire un nouveau tirage")
    print("2. ")
    print("3. ")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 VERIFIER PIN INPUT DIRECT ############# OK

    if choix == "1":
        print("1")

    ########## ################# OK

    #if choix == "2":
       
        

    ########################### OK

    #if choix == "3":


    ###########  Quitter  ##############

    if choix == "4":
        continuer = False