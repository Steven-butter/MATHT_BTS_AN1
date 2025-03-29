continuer = True
### Voir Symetrie ###

### Tableau avec l'image ###
Tab = [(0,1,1,1,1,1,1,1,1,0),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,1,1,0,0,1,1,0,1),
       (1,0,1,1,0,0,1,1,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,1,0,0,0,0,1,0,1),
       (1,0,0,1,1,1,1,0,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (0,1,1,1,1,1,1,1,1,0)]

Tab2 = [(0,1,1,1,1,1,1,1,1,0),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,1,1,0,0,1,1,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (1,0,1,0,0,0,0,1,0,1),
       (1,0,0,1,1,1,1,0,0,1),
       (1,0,0,0,0,0,0,0,0,1),
       (0,1,1,1,1,1,1,1,1,0)]

Tab3 = [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]

### Fonction Mystere du sujet
### Verification de la symetrie d'une image
### I pour le n° de colonne
### J pour la position sur la ligne

def symetrie(Tab):
    i = int(0)
    j = int(0)
    sym = 0
    for i in range(0,10,1):
        for j in range(0,5,1):
            if Tab[i][j] != Tab[i][9-j]:
                sym += 1

    if sym == 0:
        print("Image Symetrique")
        return True
    else:
        print("Image NON Symetrique")
        return False
    

### Fonction de superposition
### de deux images
### Verifie si les deux images sont identiques
### si elles ne le sont pas elle compare les valeurs et affecte la valeur au tableau 3
### en fonction de la valeur de Tab et Tab2

def superpose (Tab,Tab2,Tab3):
    i = int(0)
    j = int(0)
    for i in range(0,10,1):
        for j in range(0,10,1):
            if Tab[i][j] != Tab2[i][j] and Tab[i][j] == 1 or Tab2[i][j] == 1:
                Tab3[i][j] = 0
            if Tab[i][j] != Tab2[i][j] and Tab[i][j] == 0 or Tab2[i][j] == 0:
                Tab3[i][j] = 1
            if Tab[i][j] == Tab2[i][j] and Tab[i][j] == 1:
                Tab3[i][j] = 0
            if Tab[i][j] == Tab2[i][j] and Tab[i][j] == 0:
                Tab3[i][j] = 1
    print("Voila l'image superposee :")
    AfficheImage(Tab3)


### Fonction d'affichage de l'image
### pour chaque case du tableau verufie si elle est vide ou non
### et affiche un espace ou un X

def AfficheImage(Tab):
    i = int(0)
    j = int(0)
    ligne = [(""),("\n"),("\n"),("\n"),("\n"),("\n"),("\n"),("\n"),("\n"),("\n")]
    for i in range(0,10,1):
        for j in range(0,10,1):
            if Tab[i][j] == 0:
                ligne[i] += "  "
            elif Tab[i][j] == 1:
                ligne[i] += "X "
    print(ligne[0],ligne[1],ligne[2],ligne[3],ligne[4],ligne[5],ligne[6],ligne[7],ligne[8],ligne[9])
    

############ MENU ###########
while continuer:
    print("=== Menu image ===")
    print("1. Afficher l'image")
    print("2. Afficher l'image 2")
    print("3. Verifier Symetrie")
    print("4. Verifier Symetrie 2")
    print("5. Superposer les deux images")
    print("6. Quitter")
    choix = input("\nVotre choix : ")

    ##########  #############

    if choix == "1":
        AfficheImage(Tab)
    if choix == "2":
        AfficheImage(Tab2)
    if choix == "3":
        symetrie(Tab)
    if choix == "4":
        symetrie(Tab2)
    if choix == "5":
        if symetrie(Tab) == True and symetrie(Tab2) == True:
            superpose(Tab,Tab2,Tab3)
    if choix == "6":
        continuer = False

        