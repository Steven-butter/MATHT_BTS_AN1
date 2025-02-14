### matière coef 
matiere = [("Math", 3), ("SISR", 12), ("Cyber" , 14)]
### liste de notes
#notes = []

### i pour séléctionner 1 par 1 les matières
### matiere : liste les matiere /// note : liste de note
### 

def entrer_notes(matiere):
    note = []
    for i in range (len(matiere)):
        note.append(input(f'Saisir la note de {matiere[i][0]} : '))
    print(note)
    return note
    


entrer_notes(matiere)

