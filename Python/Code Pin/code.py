#######################################
###           Variables             ###
#######################################

continuer = True
chiffre = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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
####################################################

def verifier_code(code):
    return carnb(code) and chiffres(code)

###########################################
### Lettre de A à F max : 1 = A puis C avec +2      /////     4 = D puis F avec +2
### code_cr vas contenir le résultat de fonction avec 1er cryptage ex 1234 contenu var == BCDE
### code_crf vas contenir le résultat avec 2eme cryptage ex BCDE == DEFG
### definir la lettre grace a la position du chiffre dans la liste puis +2
### Operation a faire : 0 qui est pos 1 donc == A puis A +2 == C

def crypter(code):
    for i in range(len(code)):
        id_c = code[i].index(chiffre)
        id_l = id_c + 2
        


while continuer:

    ############ MENU ###########

    print("=== Menu code pin ===")
    print("1. Verifier un code pin")
    print("2. Crypter un code pin")
    print("3. Decrypter un code pin et le vérifier")
    print("4. Quitter")
    choix = input("\nVotre choix : ")

    ########## C1 VERIFIER PIN INPUT DIRECT ############# OK

    if choix == "1":
        code = str(input("Entrez un code à 4 chiffres : "))
        if verifier_code(code):
            print(f"Code valide : {code}")
            continuer = True
        else:
            print("Code invalide")

    ########## C2 CRYPTER PIN ET STOCKER #################

    if choix == "2":
        code = str(input("Entrez un code à 4 chiffres pour le crypter : "))
        code_cr = code
        if verifier_code(code):
            print(f"Code valide : {code}")

            continuer = True
        else:
            print("Code a crypter invalide")

    ########### C3 DECRYPTER ET VERIFIER PIN ##############

    if choix == "3":
        code = str(input("Entrez un code à 4 chiffres : "))
        if verifier_code(code):
            print(f"Code valide : {code}")
            continuer = True
        else:
            print("Code invalide")