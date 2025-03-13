jmeno = "lenka foltynova"

print(jmeno.upper())
print(jmeno.lower())


hodnoty = ['12', '1', '7', '-11']

# # Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:


treti_hodnota = hodnoty[2]
treti_hodnota = int(treti_hodnota)
vysledek = treti_hodnota + 4
vysledek = str(vysledek)
hodnoty[2] = vysledek
print(hodnoty)


hodnoty2 = '12.1 1.68 7.45 -11.51'

rozdelene = hodnoty2.split()
print(rozdelene)


nova_hodnota = rozdelene[-1]
nova_hodnota = float(nova_hodnota)
zmena = nova_hodnota + 0.25
print(zmena)

zmena = str(zmena)
rozdelene[3] = zmena
print(rozdelene)


