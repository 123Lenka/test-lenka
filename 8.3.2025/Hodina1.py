
# print ("Hello World!")

# play = "Kazdy ma svou pravdu"

# number_oftickets = 10
# price_per_ticket = 190
# total_price = number_oftickets * price_per_ticket


# if total_price >=1500:
#    total_price = total_price * 0.8
#    print("Ziskavate slevu 20%")
# elif total_price >= 500:
#    total_price = total_price * 0.9 
#    print("Ziskavate slevu 10%")


# else:
#    print("Bohuzel neziskavate slevu")


# print(f"Cena za {number_oftickets} listku na hru {play} je {int(total_price)} Kc")

# flight_number = "BA 853"

# Napr. cislo letu
# RETEZEC:  "BA 853"
# POZICE:    123456
# INDEX:     012345
# print(flight_number[0])
# print(flight_number[1])
# print(flight_number[5])

# print(flight_number[-1])
# print(flight_number[2])

# flight_number = "BA 853"
# prefix = flight_number[0] + flight_number[1]

# print(prefix)

# if prefix == "BA":
#    company = "British Airways"
# elif prefix == "LH":
#    company = "Lufthansa"
# else:
#    company = "Neznámá společnost"

# print(f"Letíte se společností {company}")

# Seznam:
# guest_list = ["Jirka", "Klára", "Natálie"]
# POZICE:       1.        2.        3.
# INDEX:        0         1         2

# print(guest_list[1])

# Seznam seznamů:
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

print(school_marks[1][0][-1])

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 2],
    ["Chemie", 4],
]


for subject in school_report:
    print(f"Název předmětu: {subject[0]}. Známka: {subject[1]}.")



print ("pouzivam github")
