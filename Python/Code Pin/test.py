chiffre = [str(i) for i in range(10)]
lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


code = "9999"
#-------------------------------------
def crypter(code):
    code_cr = ""
    cle = int(input("Entrez la clé : "))
    for i in range(len(code)):
        id_c = chiffre.index(code[i])
        #print(id_c)
        id_l = (id_c + cle) %10
        #print(id_l)
        code_cr += lettres[id_l]
        #code_cr += 
        print(code_cr)
#-------------------------------------
        

crypter(code)