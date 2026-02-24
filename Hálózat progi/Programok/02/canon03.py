from tkinter import *
from math import sin, cos, pi
from random import randrange

class Canon:
      #Ágyúrajz
    def __init__(self, boss, id, x, y, irany, szin):
          self.boss = boss # vászon hivatkozása
          self.appli = boss.master # alkalmazásablak hivatkozása
          self.id = id # ágyú azonosítója (chaîne)
          self.szin = szin # ágyú szín
          self.x1, self.y1 = x, y # ágyú forgástengelye
          self.irany = irany # lövés iránya (-1:balra, +1:jobbra)
          self.lagyucso = 25 # ágyúcső hossza
          self.angle = 0 # alapértelm. dőlésszög(lövés szöge)
          # vászon magasságának és széleségének meghatározása :
          self.xMax = int(boss.cget('width'))
          self.yMax = int(boss.cget('height'))         
          # ágyúcső rajzolása (vízszintes) :         
          self.x2, self.y2 = x + self.lagyucso * irany, y
          self.cso = boss.create_line(self.x1, self.y1, self.x2, self.y2, width =10)
          # ágyútest rajzolásan (színes kör) :
          self.rc = 15 # kör sugara
          self.test = boss.create_oval(x -self.rc, y -self.rc, x +self.rc, y +self.rc, fill =szin)
          # rejtett lövedék előrajzolása (pont a vásznon kívül) :
          self.lovedek = boss.create_oval(-10, -10, -10, -10, fill='red')
          self.anim = False # animáció indikátor
          self.explo = False # robbanás indikátor

    def iranyzas(self, angle):
         # megjegyzés: az <angle> paramétert stringként kapja meg.
         # valós értékké, majd radiánná kell alakítani :
         self.angle = float(angle)*pi/180
         # rem: inkább a coords metódust használjuk egészekkel :
         self.x2 = int(self.x1 + self.lagyucso * cos(self.angle) * self.irany)
         self.y2 = int(self.y1 - self.lagyucso * sin(self.angle))
         self.boss.coords(self.cso, self.x1, self.y1, self.x2, self.y2)

    def elmozdit(self, x, y):
         dx, dy = x -self.x1, y -self.y1 # elmozdulás értéke
         self.boss.move(self.cso, dx, dy)
         self.boss.move(self.test, dx, dy)
         self.x1 += dx
         self.y1 += dy
         self.x2 += dx
         self.y2 += dy

    def tuz(self):
        if not (self.anim or self.explo):
             self.anim =True
             # a jelenlévő összes ágyú leírásának összegyűjtése :
             self.guns = self.appli.dictionnaireCanons()
             # a lövedék kiindulási pozíciója (ez az ágyú torka) :
             self.boss.coords(self.lovedek, self.x2 -3, self.y2 -3, self.x2 +3, self.y2 +3)
             v = 15 # kezdősebesség
             # kezdősebesség vízszintes és függőleges komponense :
             self.vy = -v *sin(self.angle)
             self.vx = v *cos(self.angle) *self.irany
             self.animal_lovedek()
             return True # => jelzi, hogy elindult a lövedék
        else:
            return False # => nem lehetett kilőni a lövedéket

    def animal_lovedek(self):
        #lövedék animációja (ballisztikus pálya)
        if self.anim:
            self.boss.move(self.lovedek, int(self.vx), int(self.vy))
            c = self.boss.coords(self.lovedek) # úk koordináták
            xo, yo = c[0] +3, c[1] +3 # lövedék közepének koord.-ja
            self.test_akadaly(xo, yo) # elértünk egy akadályt ?
            self.vy += .4 # függőleges gyorsulás
            self.boss.after(20, self.animal_lovedek)
        else:
            # animáció vége lövedék elrejtése és ágyúk elmozdulása :
            self.animacio_vege()

    def test_akadaly(self, xo, yo):
        #teszteljük, hogy a lövedék elért- egy célt, vagy a játék határát
        if yo >self.yMax or xo <0 or xo >self.xMax:
            self.anim =False
            return
        # megvizsgáljuk az ágyúk szótárát annak eldöntésére, hogy
        # valamelyik ágyú nincs-e közel a lövedékhez :
        for id in self.guns: # id = kulcs a szótárban.
            gun = self.guns[id] # megfelelő érték
            if xo < gun.x1 +self.rc and xo > gun.x1 -self.rc and yo < gun.y1 +self.rc and yo > gun.y1 -self.rc :
                self.anim =False
                # lövedék robbanását rajzolja (sárga ) :
                self.explo = self.boss.create_oval(xo -12, yo -12,
                xo +12, yo +12, fill ='yellow', width =0)
                self.hit =id # eltalált céltárgy referenciája
                self.boss.after(150, self.robbanas_vege)
                break

    def robbanas_vege(self):
        #robbanás törlése ; lövedék újrainicializálása ; pontszám kezelése
        self.boss.delete(self.explo) # robbanás törlése
        self.explo =False # új lövés engedélyezése
        # jelzi a sikert a master-ablaknak :
        self.appli.goal(self.id, self.hit)

    def animacio_vege(self):
        #végrehajtandó akciók, amikor a lövedék elérte a röppályája végét
        self.appli.agyuk_szetszorasa () # az ágyúk elmozdítása
        # lövedék elrejtése (a vásznon kívülre küldve) :
        self.boss.coords(self.lovedek, -10, -10, -10, -10)

class VezerloPult(Frame):
    def __init__(self, boss, canon):
        Frame.__init__(self, bd =3, relief =GROOVE)
        self.score =0
        self.appli =boss # az alkalmazás hivatkozása
        self.canon =canon # az asszociált ágyú hivatkozása
        # A lövés szögét vezérlő rendszer :
        self.beallitas =Scale(self, from_ =75, to =-15,
        troughcolor= canon.szin, command =self.iranyzas)
        self.beallitas.set(45) # a lövés kezdő szöge
        self.beallitas.pack(side =LEFT)
        # Az ágyút azonosító címke :
        Label(self, text =canon.id).pack(side =TOP, anchor =W, pady =5)
        # Tűzgomb :
        self.bTuz =Button(self, text ='Tűz !', command =self.tuzel)
        self.bTuz.pack(side =BOTTOM, padx =5, pady =5)
        Label(self, text ="pont").pack()
        self.pontok =Label(self, text=' 0 ', bg ='white')
        self.pontok.pack()
        # az ágyú irányának megfelelően balra vagy jobbra pozícionálni :
        if canon.irany == -1:
            self.pack(padx =5, pady =5, side =RIGHT)
        else:
            self.pack(padx =5, pady =5, side =LEFT)

    def tuzel(self):
        self.canon.tuz()

    def iranyzas(self, angle):
        self.canon.iranyzas(angle)

    def pontHozzaadasa(self, p):
        #a pontszám növelése vagy csökkentése
        self.score += p
        self.pontok.config(text = ' %s ' % self.score)

class Application(Frame):
#Az alkalmazás főablaka
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Bum ')
        self.pack()
        self.jatek = Canvas(self, width =400, height =250, bg ='ivory', bd =3, relief =SUNKEN)
        self.jatek.pack(padx =8, pady =8, side =TOP)
        self.guns ={} # a jelen levő ágyúk szótára
        self.pult ={} # a jelen levő vezérlőpultok szótára
        # 2 ágyú-objektum létrehozása (+1, -1 = ellentétes irányok) :
        self.guns["Billy"] = Canon(self.jatek, "Billy", 30, 200, 1, "yellow")
        self.guns["Linus"] = Canon(self.jatek, "Linus", 370,200,-1, "blue")
        self.guns["Laci"] = Canon(self.jatek, "Laci", 30, 400, 1, "green")
        self.guns["Dóra"] = Canon(self.jatek, "Dóra", 370 ,400,-1, "orange")
        # Ezekkel az ágyúkkal asszociált 2 vezérlőpult létrehozása :
        self.pult["Billy"] = VezerloPult(self, self.guns["Billy"])
        self.pult["Linus"] = VezerloPult(self, self.guns["Linus"])
        self.pult["Laci"] = VezerloPult(self, self.guns["Laci"])
        self.pult["Dóra"] = VezerloPult(self, self.guns["Dóra"])

    def agyuk_szetszorasa(self):
        #az ágyúk véletlenszerű elmozdítása
        for id in self.guns:
            gun =self.guns[id]
            # az ágyú irányától függően balra vagy jobbra mozdítás :
            if gun.irany == -1 :
                x = randrange(320,380)
            else:
                x = randrange(20,80)
                # a tulajdonképpeni elmozdítás :
                gun.elmozdit(x, randrange(150,240))

    def goal(self, i, j):
        #az <i> ágyú jelzi, hogy eltalálta a <j> ellenfelet
        if i != j:
            self.pult[i].pontHozzaadasa(1)
        else:
            self.pult[i].pontHozzaadasa(-1)

    def dictionnaireCanons(self):
        #a jelen levő ágyúkat leíró szótárat adja meg
        return self.guns

if __name__ =='__main__':
    Application().mainloop()