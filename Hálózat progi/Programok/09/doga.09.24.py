import random
# #1. feladat
# szamlalo = 0
# for i in range(3):
#     szam = int(input("Adj meg egy számot: "))
#     if szam >= 1 and szam <= 10:
#         szamlalo += 1
# print(f'Ennyi számot adtál meg 1 és 10 között: {szamlalo}')



# #2. feladat
# veletlen = random.randint(1,20)
# while True:
#     tipp = int(input("Találd ki a számot: "))
#     if tipp > veletlen:
#         tipp = int(input("Írj kisebb számot: "))
#     elif tipp < veletlen:
#         tipp = int(input("Írj nagyobb számot: "))
#     else:
#         print("Szuper, eltaláltad")
#         break



#3. feladat
# lista = []
# def fugg(n):
#     for i in range(1,n):
#         n += n
#     lista.append(n)
#     print(f"Szám: {i}")
#     print(f'Összeg: {sum(lista)}')
# fugg(random.randint(1,20))


#4. feladat
# def bekeres():
#     szam = int(input("Írj be egy pozitív egész számot: "))
#     print(f'A szám kétszerese: {szam*2}')
#     print(f'A szám heted része: {round(szam/7,2)}')
#     print(f'A négyzetgyöke: {round(szam*0.5)}')
#     print(f'3-mal osztva az egészrész: {szam//3} maradék: {szam%3}')
#     if szam % 2 == 0:
#         print('A szám páros')
#     else:
#         print("A szám páratlan")
# bekeres()