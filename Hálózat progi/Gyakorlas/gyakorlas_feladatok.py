# #1. feladat
# def egesszam(szam):
#     print(f"A szám kétszerese: {szam*2}")
#     print(f"A szám heted része: {round(szam/7,2)}")
#     print(f"A szám négyzetgyöke: {szam*0.5}")
#     print(f"3-mal osztva az egészrész: {szam//3} maradék: {szam%3}")
#     if szam % 2 == 0:
#         print("A szám páros")
#     else:
#         print("A szám páratlan")

# szam = int(input("Írj be egy pozitív egész számot: "))
# egesszam(szam)






# #2. feladat
# print(type('anya'),type(5),type(3.14),type([1,2,3]))





# #3. feladat

# #for loop
# first = []
# counter = 0
# for i in range(15):
#     counter += 1
#     first.append(str(counter))
# print(', '.join(map(str,first)))

# #while
# second = []
# x = 0
# while True:
#     if x <= 14:
#         x += 1
#         second.append(str(x))
#     else:
#         break
# print(', '.join(map(str,second)))


# #egy soros megoldás
# print('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15')



# #4. feladat

# import math

# def pitagoraszi_szamharmasok():
#     szamharmasok = set()
#     for a in range(1, 10000):
#         for b in range(a, 10000):
#             c_negyzet = a**2 + b**2
#             c = int(math.sqrt(c_negyzet))
#             if c < 10000 and c**2 == c_negyzet:
#                 szamharmasok.add(tuple(sorted((a, b, c))))

#     with open("pita.txt", "w") as fajl:
#         for harmas in sorted(list(szamharmasok)):
#             sor = f"{harmas[0]}, {harmas[1]}, {harmas[2]}"
#             print(sor)
#             fajl.write(sor + "\n")

# if __name__ == "__main__":
#     pitagoraszi_szamharmasok()

# szam = 0
# while True:
#     if szam > 0:
#         szam += 1
#     else:
#         break
# ultimate_crash = szam**2
# with open("crash.txt", "w") as f:
#     def loop(ultimate_crash):
#         while True:
#             f.write(str(ultimate_crash))
#     loop(ultimate_crash)


import time

def traffic_signal():
    while True:
        # Red light
        print("Red light - Stop")
        time.sleep(5)  # 5 seconds for red light
        
        # Green light
        print("Green light - Go")
        time.sleep(5)  # 5 seconds for green light
        
        # Yellow light
        print("Yellow light - Prepare to stop")
        time.sleep(2)  # 2 seconds for yellow light
traffic_signal()
