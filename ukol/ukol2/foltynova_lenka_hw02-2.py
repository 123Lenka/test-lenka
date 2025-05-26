import json

INDEX_PRIMARYTITLE = 2
INDEX_DIRECTOR = 15
INDEX_CAST = 16
INDEX_GENRES = 8
INDEX_STARTYEAR = 5


movies = []
data_rows = []
movie = {}

with open("netflix_titles.tsv", encoding="utf-8") as file:
    text = file.readlines()

for line in text:
    lines = line.strip().split('\t')
    data_rows.append(lines)       
    for row in data_rows[1:]:
        movie['title'] = row[INDEX_PRIMARYTITLE]
        movie['directors'] = row[INDEX_DIRECTOR].split(',')
        if movie['directors'] == [""]:
            movie['directors'] = []
        else:
            movie['directors'] = movie['directors']
            
        movie['cast'] = row [INDEX_CAST].split(',')
        if movie['cast'] == [""]:
            movie['cast'] = []
        else:
            movie['cast'] = movie['cast']

        movie['genres'] = row[INDEX_GENRES].split(',')
        movie['decade'] = int(row[INDEX_STARTYEAR]) //10 * 10
        movies.append(movie)

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=4, ensure_ascii=False)