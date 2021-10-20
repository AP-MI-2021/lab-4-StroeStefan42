def citireLista(n):
    l = []
    for i in range (1, n+1):
        l.append(int(input()))
    return l

def pozitieNumar(nmr, p, l):
    nr=0
    for i in l:
        if (i == nmr and nr <= p):
            return True
        nr = nr + 1
    return False

def sumaNumerePare(l):
    s=0
    for i in l:
        if i%2==0:
            s=s+i
    return s

def numerePare(l):
    rezultat=[]
    for i in l:
        if i%2==0:
            rezultat.append(i)
    return rezultat

def tuplu_suma(l):

    for i in l:
        nrpozj=0
        ok=0
        for j in l:
            nrpozk=0
            for k in l:
                if j+k==i and nrpozj!=nrpozk and nrpozj<nrpozk:
                    print(j, k)

                    ok=1
                nrpozk=nrpozk+1
            nrpozj=nrpozj+1
        if ok == 0:
            print(i)

def test_pozitieNumar():
    assert pozitieNumar(12, 3, [2, 32, 122, 12, 1456])==True
def test_sumaNumerePare():
    assert sumaNumerePare([2, 3, 4, 5, 6])==12
    assert sumaNumerePare([2, 3, 4, 5, 8]) == 14
    assert sumaNumerePare([1, 3, 4, 5, 8]) == 12

def test_tuplu_suma():
    assert tuplu_suma([4, 8, 6, 3, 2, 1])==[3, 1, 6, 2, 4, 2, 1, 2, 2, 1]

def main():
    test_pozitieNumar()
    test_sumaNumerePare()
    test_tuplu_suma()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție citită de la tastatură. Dacă se găsește, se va afisa 'DA', dacă nu se găsește atunci se va afișa 'NU'.")
        print("3. Afișați suma tuturor numerelor întregi pare din lista.")
        print("4.Afișați toate numere din lista care sunt pare. Daca se repeta un numar, acesta va apărea înlista rezultat doar o singura data.")
        print("5. Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe poziții distincte din listă care adunate dau acel număr, dacă se poate. Dacă există mai multe soluții, alegeți oricare. Dacă nu se poate, nu înlocuiți numărul.")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            n=int(input("Dati numarul de elemente"))
            print("Dati lista")
            l = citireLista(n)
        elif optiune == "2":
            nmr=int(input("Dati numarul cautat: "))
            q=int(input("Dati pozitia: "))
            if print(pozitieNumar(nmr, q, l))==True:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            sf=sumaNumerePare(l)
            print(sf)
        elif optiune == "4":
            l2=[]
            l2=numerePare(l)
            print(l2)
        elif optiune == "5":
            tuplu_suma(l)

        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

if __name__ == '__main__':
    main()


