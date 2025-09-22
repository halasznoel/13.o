# #1. feladat
# ossz = []
# for i in range(8):
#     osztalyzat = int(input(f"Kérem a(z) {i+1}. osztályzatot: "))
#     ossz.append(osztalyzat)

# print(*ossz[:8], sep=',')
# print(f"Összegük: {sum(ossz)}")
# print(f"Szorzatuk: {ossz[0]*ossz[1]*ossz[2]*ossz[3]*ossz[4]*ossz[5]*ossz[6]*ossz[7]}")
# print(f"Átlaguk: {sum(ossz)/len(ossz)}")



# #2. feladat
# eredmenyek = []
# def beker():
#     pontok = 0
#     for i in range(11):
#         dontes = input(f"Kérem a(z) {i+1}. eredményt: ")
#         eredmenyek.append(dontes)
#         if dontes == 'ny':
#             pontok += 3
#         elif dontes == 'd':
#             pontok += 1
#     print(f"Pontszám: {pontok}")
# beker()


# #3. feladat
# term = []
# def szamolas():
#     for i in range(1, N+1):
#         term.append(i)
#     print(f"A számok összege: {sum(term)}")
#     paros = []
#     paratlan = []
#     for szam in term:
#         if szam % 2 == 0:
#             paros.append(szam)
#         else:
#             paratlan.append(szam)
#     print(f"A páratlanok száma: {len(paratlan)} összege: {sum(paratlan)} a páros számok összege: {sum(paros)}")
#     fakt = 1
#     for i in range(1, N+1):
#         fakt *= i
#     print(f"{N}! = {fakt}")
#     if sum(paratlan) != 0:
#         szazalek = (sum(paros) / sum(paratlan)) * 100
#         print(f"A páros számok összege {szazalek:.1f}%-a a páratlan számok összegének.")
#     else:
#         print("A páratlan számok összege 0, így százalékos arány nem értelmezhető.")
# N = int(input("Kérem N értékét: "))
# szamolas()

    
