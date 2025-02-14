### matière coef 
matiere = [("Math", 3), ("SISR", 12), ("Cyber" , 14)]
### liste de notes
#notes = []

### i pour séléctionner 1 par 1 les matières
### matiere : liste les matiere /// notes : liste de note
### 

def entrer_notes(matiere):
    note = []
    for i in range (0,len(matiere)):
        #notes.append(input(f'Saisir la note de {matiere[i][0]} : '))
        note = input(f'Saisir la note de {matiere[i][0]} : ')
        return note


entrer_notes()
print(entrer_notes())
