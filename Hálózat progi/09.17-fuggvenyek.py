import random
# #1. feladat
# def fuggveny(n):
#     lista = []
#     i = 1
#     for i in range(n):
#         szam = int(input(f"Adja meg a sorozat {i+1}. elemét: "))
#         lista.append(szam)
#         i+=1
#     print(lista)
#     print(f"A számok összege: {sum(lista)}")
#     print(f"A számok átlaga: {sum(lista)/len(lista)}")
# fuggveny(5)





# #2. feladat
# def elojel(szam):
#     if szam == 0:
#         return 'z'
#     elif szam > 0:
#         return 'p'
#     else:
#         return 'n'
# for i in range(5):
#     szam = random.randint(-20,20)
#     print(szam, elojel(szam))
# elojel(random.randint(-20,20))






# #3. feladat
# def paros():
#     for i in range(5):
#         szam = random.randint(1,20)
#         if szam % 2 == 0:
#             print(f"{szam} páros")
#         else:
#             print(f"{szam} páratlan")
# paros()






# #4. feladat
# def inko(a,b):
#     if a == b:
#         return a
#     elif a < b:
#         return inko(a,b-a)
#     else:
#         return inko(a-b,b)
# print(inko(int(input("Kérem az egyik számot: ")),int(input("Kérem a második számot: "))))







# #5. feladat
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(15):
#     print(fibonacci(i))


# Készíts függvényt, ami 1-től összeadja a bemenetként kapott N-ig az egész számokat!
# A függvényt hívd meg öt darab 1 és 20 közötti véletlen számra, a program írja ki a
# számot és az összeget.

# #6. feladat
# def matek(n):
#     for i in range(5):
#         szam = random.randint(1,20)

# matek(random.randit(1,20))
