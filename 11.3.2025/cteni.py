# file = open("mereni.txt")

# print(file)

# text = file.read()
# print(text)

# file.close()


# with open('mereni.txt') as file:
#     text = file.read()

# print(text)


ines = []
with open('mereni.txt', mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        line = line.split("\t")
        day = line[0]
        temp = float(line[1])
        # print(line)
        lines.append([day, temp])

print(lines)