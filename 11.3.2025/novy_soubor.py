# text = "Tento text bude zapsán do souboru."

# with open('soubor.txt', mode='w', encoding='utf-8') as output_file:
#     print(text, file=output_file)

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('vykaz.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)



# text = "Tento text bude zapsán do souboru."

# # with open('soubor.txt', mode='x', encoding='utf-8') as output_file:
# #     print(text, file=output_file)

# names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

# with open('soubor.txt', mode='w', encoding='utf-8') as output_file:
#     for name in names:
#         print(name, file=output_file)