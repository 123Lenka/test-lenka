venecky = [1, 2, 4, 1, 6, 0, 1]

print(venecky[0])
venecky[5] = 12

print(venecky[5])

work_days = venecky[0:5] # <0 ; 5) petka uz se tam nezapocita, da se zapsat jako [:5] bez te nuly
print(work_days)

weekend = venecky [5:7] #da se zapsat jako [5:] bez toho koneceneho prvku
print(weekend)


jmeno = " aadela bierska"

name = jmeno [:5]
surname = jmeno [6:]

print(surname)