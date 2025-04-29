import random

def TestPresence(numero):
    coureur = [0,0,0,0,0]
    present = False
    n = random.randint(1,50)
    for i in range (0,4):
        if coureur[i] == n:
            present = True
            return coureur, present
        else:
            return coureur, present



def selection():
    numero = random.randint(1,50)
    tab = TestPresence(numero)[0]
    tab[0]=int(input("Donnez le numero du gagnant"))
    k = False
    i = 1
    for a in range (1,5):
        numero = random.randint(1,50)
        k = TestPresence(numero)[1]

        if k == False:
            tab[i]=numero
            i = i+1
    return tab

def total_tableau():
    tab_total = [[],[],[],[],[],[],[],[],[],[]]
    for i in range (10):
        tab_total[i] = selection()
    print(tab_total)
#print(TestPresence()[0])

#selection()
total_tableau()