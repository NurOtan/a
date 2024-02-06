movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#single movie and returns True if its IMDB score is above 5.5
def is_goodmovie(movie):
    return movie.get('imdb') > 5.5

print(is_goodmovie(movies[7]))

# returns a sublist of movies with an IMDB score above 5.5.
def goodmovies(movie):
    return [movie for movie in movies if is_goodmovie(movie)]

print(goodmovies(movies))

# category name and returns just those movies under that category.
def same_genre(movie, name):
    return [movie for movie in movies if movie.get("category") == name]

print(same_genre(movies, "Action"))

# movies and computes the average IMDB score.
def avg_imdb(movie):
    summa = sum(mv.get('imdb') for mv in movies)
    result = summa/ len(movie)
    return result

print(avg_imdb(movies))

#category the average IMDB score.
def avg_imdb_by_genre(movie, name):
    result = sum(i.get('imdb') for i in same_genre(movie,name))
    return result/ len(same_genre(movie,name))

print(avg_imdb_by_genre(movies, "Thriller"))