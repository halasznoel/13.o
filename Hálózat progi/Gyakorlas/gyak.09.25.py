# #1. Könyves feladat OOP
# class Könyv:
#     def __init__(self,cim,szerzo):
#         self.cim = cim
#         self.szerzo = szerzo

#     def info(self):
#         return f"Cím: {self.cim} \nSzerző: {self.szerzo}"
    
# konyv1 = Könyv("A Gyűrűk Ura","J.R.R Tolkien")
# konyv2 = Könyv("Gazdag Papa Szegény Papa","Robert T. Kiyosaki")

# print(konyv1.info())
# print(konyv2.info())



# 2. Bankszámlás feladat OOP
class Bankszámla:
    def __init__(self,nev,egyenleg):
        self.nev = nev
        self.egyenleg = egyenleg

    def befizetes(self,osszeg):
        if osszeg > 0:
            self.egyenleg += osszeg
            print(f"Sikeres befizetés! Új egyenleg: {self.egyenleg} Ft")
        else:
            print("A befizetés csak pozitív összeg lehet.")
    
    def kivetel(self,osszeg):
        if osszeg > 0 and self.egyenleg >= osszeg:
            self.egyenleg -= osszeg
            print(f"Sikeres kivétel! Új egyenleg: {self.egyenleg} Ft")
        else:
            print("Sajnos nincs elég fedezet a tranzakcióhoz.")
    
    def egyenleg_lekerdezes(self):
        print(f"Jelenleg ennyi forint van a számládon: {self.egyenleg} Ft")

szamla1 = Bankszámla('Halász István',25000000)

print("Üdv a Halászos Bankban \n Írd le, hogy mit szeretnél csinálni")

while True:
    muvelet = input("(egyenleg)\n(befizetés)\n(kivétel)\n(kilépés)\nAdd meg a műveletet: ")
    if muvelet == "egyenleg":
        szamla1.egyenleg_lekerdezes()
    elif muvelet == "befizetés":
        try:
            osszeg = int(input("Add meg az összeget amit be szeretnél fizetni: "))
            szamla1.befizetes(osszeg)
        except ValueError:
            print("Hiba: Kérlek, számot adj meg!")
    elif muvelet == "kivétel":
        try:
            osszeg = int(input("Add meg az összeget amit fel szeretnél venni: "))
            szamla1.kivetel(osszeg)
        except ValueError:
            print("Hiba: Kérlek, számot adj meg!")
    elif muvelet == "kilépés":
        print("Viszlát!")
        break
    else:
        print("Ismeretlen művelet. Kérlek, próbáld újra!")