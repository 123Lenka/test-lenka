import json


with open('alice.txt', mode = "r", encoding = "utf-8") as file:
       text = file.read()
       small_text = text.lower()
       characters = sorted(small_text)

character_count = dict()

for key in characters:
        if key in character_count:
               character_count[key] += 1
        else:
               character_count[key] = 1

del character_count["\n"]
del character_count[" "]

with open('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(character_count, file, indent=4, ensure_ascii=False)