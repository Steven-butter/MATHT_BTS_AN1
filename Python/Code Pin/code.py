code = "1234"
continuer = True

def carnb ():
    if len(code) == 4:
        print("Le code faire bien 4 chiffres")
        continuer = True

def chiffres ():
    if code.isdecimal():
        print("Le code ne contiens que des chiffres")
        continuer = True



carnb()
chiffres()