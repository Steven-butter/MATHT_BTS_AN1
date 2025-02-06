chiffre = [str(i) for i in range(10)]
lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


code = str(1854)
def crypter(code):
    code_cr = ""
    for i in range(len(code)):
        id_c = chiffre.index(code[i])
        id_l = id_c + 2
        print("id_c : ", id_c)
        print("id_l : ", id_l)
        #lettrefin = str(id_l).index(lettres)
        lettrefin = lettres[id_l - 1]
        print("Lettre de fin : ", lettrefin)
        code_cr += lettres[id_l - 1]
        print("Resultat : ", code_cr)
        

crypter(code)