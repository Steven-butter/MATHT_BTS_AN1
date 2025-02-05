chiffre = [str(i) for i in range(10)]
lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

code = str(1234)
def crypter(code):
    for i in range(len(code)):
        id_c = chiffre.index(code[i])
        id_l = id_c + 2
        print("id_c : ", id_c)
        print("id_l : ", id_l)
        

crypter(code)