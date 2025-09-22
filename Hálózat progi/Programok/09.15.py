# # #1. feladat
# szamlalo = int(input("Kérem adja meg a számláló értékét: "))
# nevezo = int(input("Kérem adja meg a nevező értékét: "))
# if szamlalo % nevezo == 0:
#     print("Egész")
# else:
#     print("Nem egész")

# #2. feladat
# n = 1
# szamok = []
# while n**2 <= 100000:
#     szamok.append(str(n**2))
#     n+=1
# print(', '.join(szamok))

# #3. feladat
# beker = input("Kérem adjon meg 5 számot szóközzel elválasztva: ").split(' ')
# lista = [1 for i in beker if 1 <= int(i) <= 10]
# print(sum(lista),' van 1 és 10 között')

# #4. feladat
# c = int(input("Kérem adjon meg egy 100-nál kisebb számot: "))
# prim = True
# for i in range(2,c):
#     if c % i == 0:
#         prim = False
# print('Prím' if prim else 'Nem prím')

# #5. feladat
# a = int(input("Kérem adja meg az a értékét: "))
# b = int(input("Kérem adja meg az b értékét: "))
# if a % b == 0:
#     print("Egész",a/b)
# else:
#     print("Nem egész",round(a/b,2))
# if b % a == 0:
#     print("Egész",b/a)
# else:
#     print("Nem egész: ",round(b/a,2))

# #6. feladat

szam1 = "110a101001"
szam2 = "223313020003"
