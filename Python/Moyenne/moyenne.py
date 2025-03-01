##########################################
###             Variable               ###
##########################################


### matière coef 
matiere = [("Math", 3), ("LV1", 2), ("LV2" , 1)]
### Boucle
continuer = True

############################################
###             Fonctions                ###
############################################

############################################
### A1 : Calcul points bonus

def calcul_bonus():
    print("Entrer les points bonus")
    bonus = int(input("Points bonus : "))
    if bonus < 10:
        bonus = 0
        return bonus
    else:
        bonus = bonus - 10
        bonus = bonus * 2
        print(f'Vous avez {bonus} points bonus')
        return bonus


### A2 : Entrer les notes
### i pour séléctionner 1 par 1 les matières
### matiere : liste les matiere /// note : liste de note
### sort une liste de note

def entrer_notes(matiere):
    note = []
    for i in range (len(matiere)):
        note.append(input(f'Saisir la note de {matiere[i][0]} : '))
    return note

#############################################
###         Programme Principale          ###
#############################################


while continuer:

    ############ MENU ###########

    print("=== Menu moyenne ===")
    print("1. Entrer les notes")
    print("2. ")
    print("3. ")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 Entrer les notes ############# OK

    if choix == "1":
        notes = entrer_notes(matiere)
        for i in range (len(matiere)):
            print(f'Voici le tableau de note : {matiere[i][0], notes[i]}')
