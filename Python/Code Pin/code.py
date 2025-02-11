#######################################
###           Variables             ###
#######################################

continuer = True
chiffre = [str(i) for i in range(10)]
lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#code_cr = ""
code_crypter = ""

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
### code = variable d'entré du code  ##
## retourne true si condition valide ##
#######################################

def chiffres(code):
    if all(caractere in chiffre for caractere in code):
        print("Le code n'est composer que de chiffres")
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
### id_c position chiffre dans la liste
### id_l prend la position du chiffre 2 places au dessus de lui donc la position de la bonne lettre
### code_cr : résultat du code crypter
        
def crypter(code):
    code_cr = ""
    for i in range(len(code)):
        id_c = chiffre.index(code[i])
        id_l = (id_c + cle_crypter) %10
        code_cr += lettres[id_l]
    #print(code_cr)
    return code_cr

#######################################################
# FONCTION DECRYPTAGE
#######################################################

def decrypter(code_cr):
    code_dcr = ""
    for i in range(len(code_cr)):
        id_lc = lettres.index(code_cr[i])
        id_cc = (id_lc - cle_decrypter) %10
        code_dcr += chiffre[id_cc]
    #print(code_dcr)
    return code_dcr
        


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

    ########## C2 CRYPTER PIN ET STOCKER ################# OK

    if choix == "2":
        code = str(input("Entrez un code à 4 chiffres pour le crypter : "))
        code2 = str(input("Veuillez saisire le code a nouveau : "))
        if code == code2:
            cle_crypter = int(input("Entrez la clé de cryptage : "))
            if verifier_code(code):
                crypter(code)
                continuer = True
            else:
                print("Code a crypter invalide")
        else:
                print("Les codes ne sont pas identique.")
        

    ########## C3 DECRYPTER PIN ET VALIDER ################# OK

    if choix == "3":
        code_crypter = crypter(code)
        cle_decrypter = int(input("Entrez la clé de décryptage : "))
        code_dcrypt = decrypter(code_crypter)
        #print(code_dcrypt)
        if crypter != "":
                if cle_decrypter == cle_crypter:
                    if code == code_dcrypt :
                        print("Code décrypter ")
                        continuer = True
                    else:
                        print("Le code n'est pas le code précedent.")
                else:
                    print("Clé de décryptage éronnée")
        else:
            print("Code non décrypter")

    ########### C4 QUITTER ##############

    if choix == "4":
        continuer = False
