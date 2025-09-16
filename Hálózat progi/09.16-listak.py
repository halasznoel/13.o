ossz = []
for i in range(3):
    osztalyzat = int(input(f"Kérem a(z) {i+1}. osztályzatot: "))
    ossz.append(osztalyzat)

print(f"Összegük: {sum(ossz)}")

szorzat = 0
for i in ossz:
    szorzat += i*i

print(f"Szorzat: {szorzat}")