class Könyv:
    def __init__(self,cim,szerzo):
        self.cim = cim
        self.szerzo = szerzo

    def info(self):
        return f"Cím: {self.cim} \nSzerző: {self.szerzo}"
    
konyv1 = Könyv("A Gyűrűk Ura","J.R.R Tolkien")
konyv2 = Könyv("Gazdag Papa Szegény Papa","Robert T. Kiyosaki")

print(konyv1.info())
print(konyv2.info())