# pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



# with open('kalendar.txt', mode='w', encoding='utf-8') as output_file:
#     for dny in pocty_dni:
#         print(dny, file=output_file)



file_name = input("Zadejte název souboru: ")
text = input("Zadejte text, který se má uložit: ")

with open(file_name, mode="w", encoding="utf-8") as file:
    print(text, file=file)


    file_name = input("Zadejte název souboru: ")
# text = input("Zadejte text, který se má uložit: ")

# if ".txt" not in file_name:
if not file_name.endswith(".txt"):
    file_name = file_name + ".txt"
    # file_name += ".txt"

print(file_name)

