# import math

# cislo = math.pi
# print(cislo)
# print(round (cislo, 2))



# a = 123456.784

# print(round(a, 2))
# print (round(a, -2))



# print (math. ceil (a))
# print(math.floor(a))


# print(pow(2,4))
# print(math.sqrt(16))

# import math

# uhel = float (input("zadej uhel"))

# uhel = math.radians(uhel)

# print(uhel)

# sinus = math.sin(uhel)
# cosinus = math.cos(uhel)

# print (round(sinus, 2),round(cosinus, 2),)


import math


cislo = float(input("vloz cislo"))

cisloDesetinne, cisloCele = math.modf(cislo)

print(cisloCele, round(cisloDesetinne, 2))