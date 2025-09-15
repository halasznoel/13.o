# 1. feladat: dolgozat
doga_pontszam = int(input("Add meg a dolgozat pontszámát: "))

if doga_pontszam >= 0 and doga_pontszam <= 9:
    print(f"Ez sajnos egyes lett, ennyi pont kell a jobb eredményhez: {9-doga_pontszam} pont")
elif doga_pontszam >= 10 and doga_pontszam <= 19:
    print(f"Ez sajnos kettes lett, ennyi pont kell a jobb eredményhez: {19-doga_pontszam} pont")
elif doga_pontszam >= 20 and doga_pontszam <= 29:
    print(f"Ez sajnos hármas lett, ennyi pont kell a jobb eredményhez: {29-doga_pontszam} pont")
elif doga_pontszam >= 30 and doga_pontszam <= 39:
    print(f"Ez sajnos négyes lett, ennyi pont kell a jobb eredményhez: {39-doga_pontszam} pont")
elif doga_pontszam >= 40 and doga_pontszam <= 50:
    print(f"Ez ötös lett, ennyi kellett volna a max ponthoz: {50-doga_pontszam} pont")
else:
    print("Hibás pontszámot adtál meg.")





#2. feladat: gyümölcsök
class Gyumolcsok:
    def __init__(self, gyum, ar, hazai):
        self.gyum = gyum
        self.ar = ar
        self.hazai = hazai
    
    def szarmazas(self):
        if self.hazai == "i":
            return "Ez a gyümölcs hazai."
        else:
            return "Ez a gyümölcs külföldi."
    
    def kiir(self):
        print(f"A {self.hazai,self.gyum} 1 kg {self.ar} Ft-ba kerül.")

Gyumik=[]
for i in range(2):
    gy = input("Add meg a gyümölcs nevét: ")
    a = input("Add meg a gyümölcs árát: ")
    h = input("Hazai-e (i/n): ")
    Gyumik.append(Gyumolcsok(gy,a,h))

for i in Gyumik:
    print(i.gyum,i.ar,i.hazai)






# #3. feladat: háromszög
def szerkharsz(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("Szerkeszthető")
    else:
        print("Nem szerkeszthető")

a = int(input("Add meg az a értékét: "))
b = int(input("Add meg az b értékét: "))
c = int(input("Add meg az c értékét: "))
print(szerkharsz(a,b,c))