# import math

# cislo = int(input( "zadej cislo"))

# if cislo > 0 :
#     faktorial = math.factorial(cislo)
#     print (f"{cislo:>05} ! = {faktorial:>05}")

# else:
#     print("spatne cislo")



# odpoved = int(input("ucis se? Zadej 0 nebo 1"))

# if odpoved in range(0,5):
#     odpoved= bool(odpoved)
#     if odpoved:
#         print("jsi dobra")
#     else:
#         print("jsi lina")

# else:
#     print("spatna odpoved")

import math


cislo = int(input("napis cislo"))
volba = int(input("zadej \n 1 pro mocninu, \n 2 pro odmocninu,  \n 3 pro faktorial"))

if volba == 1:
    cislo = pow(cislo, 2)
    print(cislo)
else:
    if volba == 2:
        cislo = math.sqrt(cislo)
        print(cislo)
    else:
        if volba == 3:
            cislo = math.factorial(cislo)
            print(cislo)
        else: print("spatny vyber")