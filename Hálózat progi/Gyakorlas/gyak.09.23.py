# Készíts egy függvényt elojel néven, ami bemenetként egy számot kap, a visszatérési
# értéke pedig ’z’, ha a szám nulla, ’p’, ha a szám pozitív és ’n’, ha negatív. Az elkészült
# függvényt hívd meg öt, -20 és 20 közötti véletlenszerűen generált számmal. A
# program írja ki a számot és egy szóközzel elválasztva az előjelét.
# Minta:
# 9 p
# -16 n
# -3 n
# 20 p
# 1 p

import random

def elojel(szam):
    if szam == 0:
        return 'z'
    elif szam > 0:
        return 'p'
    else:
        return 'n'

def main():
    pozitiv_db = 0
    negativ_db = 0
    nulla_db = 0 
    for i in range(5):
        szam = random.randint(-20,20)
        eredmeny = elojel(szam)
        if eredmeny == 'z':
            nulla_db += 1
        elif eredmeny == 'p':
            pozitiv_db += 1
        else:
            negativ_db += 1
        print(f"{szam} {eredmeny}")
    
    print(f'{pozitiv_db} db pozitív szám van')
    print(f'{negativ_db} db negatív szám van')
    print(f'{nulla_db} db nulla van')

if __name__ == "__main__":
    main()
