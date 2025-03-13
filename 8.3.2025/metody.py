# array = [0, 1, 2, 3]

# for item in array:
#     print(item)
#     print(item + 1)

# if len(array) > 4:
#     print("Toto je dlouhy seznam")

# print("Toto uz neni cyklus")



# TASK 01

# les = [23, 4, -8, 16, 15, -42]

# kosik = 0

# for houba in les:
#     kosik += houba

# print(kosik)


# TASK 02

# coffee_list = [
#     ["Espresso", 63],
#     ["Americano", 95],
#     ["Latte", 75],
#     ["Cold Brew", 200],
#     ["Cappuccino", 80]
# ]

# for coffee in coffee_list:
#     if coffee[1] < 90:
#         print(coffee[0])


# TASK 03

# numbers = [23, 4, -8, 16, 15, -42]

# kosik = []

# for number in numbers:
#     if number % 2 == 0:
#         # print(number)
#         kosik.append(number)

# print(kosik)
# print(len(kosik))
# print(sum(kosik))

# kosik[0]


venecky = [1, 2, 4, 1, 6, 0, 1]

# print(venecky[0])
# venecky[5] = 12
# print(venecky[5])

# work_days = venecky[:5]               # < 0 ; 5 )
# print(work_days)

# weekend = venecky[5:]
# print(weekend)

# venecky_copy = venecky[:]
# print(venecky_copy)

# print(sorted(venecky, reverse=True))


# jmeno = "Leontýna Bierská"

# name = jmeno[:8]
# surname = jmeno[9:]

# # print(surname)

# print(sorted(jmeno))

# inzerat = "Na této pracovní pozici budete využívat Python a SQL"
# if "Python" in inzerat:
#     print("Je to pro mě!")


# pohyby = [1200, -250, -800, 540, 721, -613, -222]

# print(pohyby[2])
# print(pohyby[2:])
# print(len(pohyby))
# print(f"Nejnizsi: {min(pohyby)} Nejvyssi: {max(pohyby)}")
# print(sum(pohyby))

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# vysledek = sum(seznam) / len(seznam)

# print(vysledek)

# rozpeti = max(seznam) - min(seznam)
# print(rozpeti)

jmeno = " adela bierska  "

spz = "6ma 9364"

week = "po ut st     ct pa so ne"
names = ["Marek", "Adam", "Bronislava", "Roman"]

# print(spz.upper())
# print(f"'{jmeno.strip().title()}'")
# print(week.split())
# print(week.split(" "))
# print(";".join(names))

# print(jmeno.replace("adela", "leontyna"))


hodnoty = ['12', '1', '7', '-11']

treti_hodnota = hodnoty[2]

treti_hodnota = int(treti_hodnota)

vysledek = treti_hodnota + 4

vysledek = str(vysledek)

hodnoty[2] = vysledek

print(hodnoty)


hodnoty = '12.1 1.68 7.45 -11.51'

list_hodnoty = hodnoty.split()

posledni_hodnota = list_hodnoty[-1]
posledni_hodnota = float(posledni_hodnota)
vysledek = posledni_hodnota + 0.25
print(vysledek)
vysledek = str(vysledek)
list_hodnoty[-1] = vysledek

vysledek_hodnoty = " ".join(list_hodnoty)

print(vysledek_hodnoty)

