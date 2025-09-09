# 1. feladat: dolgozat
ötös = 50
négyes = 39
hármas = 29
kettes = 19
egyes = 9
doga_pontszam = int(input("Add meg a dolgozat pontszámát: "))

if doga_pontszam >= 0 and doga_pontszam <= 9:
    print(f"Ez sajnos egyes lett, ennyi pont kell a jobb eredményhez: {egyes-doga_pontszam}")
elif doga_pontszam >= 10 and doga_pontszam <= 19:
    print(f"Ez sajnos kettes lett, ennyi pont kell a jobb eredményhez: {kettes-doga_pontszam}")
elif doga_pontszam >= 20 and doga_pontszam <= 29:
    print(f"Ez sajnos hármas lett, ennyi pont kell a jobb eredményhez: {hármas-doga_pontszam}")
elif doga_pontszam >= 30 and doga_pontszam <= 39:
    print(f"Ez sajnos négyes lett, ennyi pont kell a jobb eredményhez: {négyes-doga_pontszam}")
elif doga_pontszam >= 40 and doga_pontszam <= 50:
    print(f"Ez ötös lett, ennyi kellett volna a max ponthoz: {ötös-doga_pontszam} ")

#2. feladat: gyümölcsök

class Gyümölcsök:
    def __init__(self, gyum, ar, hazai, kulfoldi):
        self.gyum = gyum
        self.ar = ar
        self.hazai = hazai
        self.kulfoldi = kulfoldi
    
    def származás(hazai, kulfoldi):
        hazai = 1
        kulfoldi = 0
    
    def kiíratás(származás):
        if gyum == származás.hazai:
            print("Ez a gyümölcs hazai.")
        else:
            print("Ez a gyümölcs külföldi.")