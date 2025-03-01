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

def calcul_bonus(bonus):
    if bonus < 10:
        bonus = 0 or bonus > 20 or bonus < 0
        return bonus
    else:
        bonus = bonus - 10
        bonus = bonus * 2
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

### A3 : Calcul de la moyenne
### note : liste des notes /// matiere [i][1] : coef de la matière

def calcul_moyenne(notes, matiere, bonus):
    moyenne = 0
    coef = 0
    for i in range (len(notes)):
        moyenne += int(notes[i]) * matiere[i][1]
    moyenne = moyenne + bonus
    for i in range (len(matiere)):
        coef = coef + matiere[i][1]
    moyenne = moyenne // coef
    return moyenne

#############################################
###         Programme Principale          ###
#############################################


while continuer:

    ############ MENU ###########

    print("=== Menu moyenne ===")
    print("1. Entrer les notes")
    print("2. Points bonus")
    print("3. Calculer la moyenne")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 Entrer les notes ############# OK

    if choix == "1":
        notes = entrer_notes(matiere)
        for i in range (len(matiere)):
            print(f'Voici le tableau de note : {matiere[i][0], notes[i]}')
    if choix == "2":
        print("Entrer vos points sur la matière facultative")
        bonus = int(input("Points : "))
        bonus = calcul_bonus(bonus)
        print(f'Vous avez {bonus} points bonus')
    if choix == "3":
        moyenne = calcul_moyenne(notes, matiere, bonus)
        print(f'Votre moyenne est de : {moyenne}')
