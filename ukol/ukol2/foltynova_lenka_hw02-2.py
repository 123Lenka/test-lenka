import json

INDEX_PRIMARYTITLE = 2
INDEX_DIRECTOR = 15
INDEX_CAST = 16
INDEX_GENRES = 8
INDEX_STARTYEAR = 5


movies = []


with open("netflix_titles.tsv", encoding="utf-8") as file:
    text = file.readlines()

for line in text[1:]:
    items = line.strip().split('\t')
    movie = {}
    movie['title'] = items[INDEX_PRIMARYTITLE]
    if not items [INDEX_DIRECTOR]:   
        movie['director'] = []        
    else:
       movie['director'] = items[INDEX_DIRECTOR].split(', ')
    
    if not items [INDEX_CAST]:   
        movie['cast'] = []        
    else:
       movie['cast'] = items[INDEX_CAST].split(', ')

    movie['genres'] = items[INDEX_GENRES].split(',')
    movie['decade'] = int(items[INDEX_STARTYEAR]) //10 * 10
    movies.append(movie)

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=4, ensure_ascii=False)


