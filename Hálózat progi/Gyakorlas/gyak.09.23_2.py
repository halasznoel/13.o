import random

def paros(szam):
    if szam % 2 == 0:
        return True
    else:
        return False

def main():
    for i in range(5):
        szam = random.randint(0,20)
        eredmeny = paros(szam)
        if eredmeny == True:
            dontes = 'páros'
        else:
            dontes = 'páratlan'
        print(f'{szam} {dontes}')

if __name__ == "__main__":
    main()
