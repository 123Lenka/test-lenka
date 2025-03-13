seznam = []
with open('vykaz.txt', mode="r", encoding="utf-8") as file:
 
    for line in file:
         line = line.strip()
        #line = line.split("\t")
      
        
         print(line)
         line = int(line)

         seznam.append(line)

print(seznam)


# file = open("vykaz.txt")

# print(file)

# text = file.read()
# print(text)

# lines = []
# with open("vykaz.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         lines.append(int(line.strip()))

# print(lines)

# hodinova_mzda = int(input("Zadejte hodinovou mzdu: "))
# rocni_mzda = sum(lines) * hodinova_mzda
# prumerna_mzda_mesicni = rocni_mzda / len(lines)

# print(prumerna_mzda_mesicni)