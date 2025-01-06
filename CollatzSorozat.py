kiinduloSzam = int(input ("Kérem a kiinduló számot: "))
szam = kiinduloSzam
szamlalo = 0
maximumErtek = szam


while szam > 1:
    if szam % 2 == 0:
        szam = int(szam / 2)
        print(szam)
        szamlalo = szamlalo + 1
    else:
        szam = int((szam * 3) + 1)
        print (szam)
        szamlalo = szamlalo + 1
        
        if szam > maximumErtek:
            maximumErtek = szam

print("A kiindulo szam:", kiinduloSzam)
print("Az elért legnagyobb számérték:", maximumErtek)
print("A végrehajtott lépések száma:", szamlalo)

     