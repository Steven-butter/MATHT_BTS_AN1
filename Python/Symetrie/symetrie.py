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
       (0,1,1,1,1,1,1,1,0,0)]

### Fonction Mystere du sujet
### Verification de la symetrie d'une image
### I pour le n° de colonne
### J pour la position sur la ligne

def symetrie (Tab):
    i = int(0)
    j = int(0)
    sym = 0
    for i in range(0,10,1):
        for j in range(0,5,1):
            if Tab[i][j] != Tab[i][9-j]:
                sym += 1

    if sym == 0:
        print("Image Symetrique")
    else:
        print("Image NON Symetrique")

### Fonction d'affichage de l'image
###
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
    print("2. Verifier Symetrie")
    print("3. ")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 Entrer les notes ############# OK

    if choix == "1":
        AfficheImage(Tab)
    if choix == "2":
        symetrie(Tab)
    if choix == "4":
        continuer = False
    #if choix == "3":

        