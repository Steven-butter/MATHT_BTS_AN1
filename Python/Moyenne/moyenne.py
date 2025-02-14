##########################################
###             Variable               ###
##########################################


        ### matière coef 
matiere = [("Math", 3), ("SISR", 12), ("Cyber" , 14)]
        ### Boucle
continuer = True

############################################
###             Fonctions                ###
############################################


### i pour séléctionner 1 par 1 les matières
### matiere : liste les matiere /// note : liste de note
### sort une liste de note


def entrer_notes(matiere):
    note = []
    for i in range (len(matiere)):
        note.append(input(f'Saisir la note de {matiere[i][0]} : '))
    print(note)
    return note
    

while continuer:

    ############ MENU ###########

    print("=== Menu moyenne ===")
    print("1. Entrer les notes")
    print("2. ")
    print("3. ")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 VERIFIER PIN INPUT DIRECT ############# OK

    if choix == "1":
        entrer_notes(matiere)
