import json

PRIMARYTITLE = 2
DIRECTOR = 15
CAST = 16
GENRES = 8
STARTYEAR = 5

movies = []
pomocna = [] 
new = []
movie = {}
keys = ['title', 'directors', 'cast', 'genres', 'decade']

with open("netflix_titles.tsv", encoding="utf-8") as file:
    text = file.readlines()

for line in text:
    lines = line.strip().split('\t')
    pomocna.append(lines)
    new = pomocna[1:]
    
for thing in new:
    movie = {}
    movie[keys[0]] = thing[2]
    movie[keys[1]] = thing[15].split(',')
    movie[keys[2]] = thing [16].split(',')
    movie[keys[3]] = thing[8].split(',')
    movie[keys[4]] = thing[5].split(',')
    movies.append(movie)

print(movies[16])

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=4, ensure_ascii=False)

