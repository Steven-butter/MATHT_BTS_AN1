continuer = True

def carnb(code):
    if len(code) == 4:
        print("Le code a 4 chiffres.")
        return True
    else :
        print("Le code a pas 4 chiffres.")
        return False

def chiffres(code):
    if code.isdecimal():
        print("Le code a des chiffres")
        return True
    else :
        print("le code a pas de chiffres")
        return False

def verifier_code(code):
    return carnb(code) and chiffres(code)

while continuer:
    code = input("Entrez un code à 4 chiffres : ")
    if verifier_code(code):
        print(f"Code valide : {code}")
        continuer = True
    else:
        print("Code invalide")
