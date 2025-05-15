import json


with open('alice.txt', mode="r", encoding="utf-8") as input_file:
    text = input_file.read()

characters = sorted(text.lower())

character_count = dict()
unwanted_chars = (" ", "\n")

for key in characters:
    if key not in unwanted_chars:
        character_count[key] = character_count.get(key, 0) + 1
     
with open('hw01_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(character_count, output_file, indent=4, ensure_ascii=False)


