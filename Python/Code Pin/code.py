#######################################
###           Variables             ###
#######################################

continuer = True
chiffre = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#######################################
### Verifier la longueur de l'entré ###
### code = variable d'entré du code ###
## retourne true si condition valide ##
#######################################

def carnb(code):
    if len(code) == 4:
        print("Le code a 4 chiffres.")
        return True
    else :
        print("Le code a pas 4 chiffres.")
        return False

#######################################
# Verifier si c'est que des chiffres ##
### code = variable d'entré du code | num-ok valeur boucle
## retourne true si condition valide ##
#######################################

def chiffres(code):
    if all(caractere in chiffre for caractere in code):
        print("Le code n'est composer que de chiffres chiffres")
        return True
    else:
        print("Le code n'est pas composer que des chiffres")
        return False
    
#########################################
### Verifier si les deux condition sont valides
### Demande au fonction quelle valeur est retourner
### Si les deux valeur

def verifier_code(code):
    return carnb(code) and chiffres(code)

while continuer:
    print("=== Menu code pin ===")
    print("1. Verifier un code pin")
    print("2. Crypter un code pin")
    print("4. Decrypter un code pin et le vérifier")
    print("3. Quitter")
    choix = input("\nVotre choix : ")
    if choix == "1":
        code = str(input("Entrez un code à 4 chiffres : "))
        if verifier_code(code):
            print(f"Code valide : {code}")
            continuer = True
        else:
            print("Code invalide")
    if choix == "2":
        continuer = False
    else :
        continuer = False