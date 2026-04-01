import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")

cursor.execute("""
    CREATE TABLE movies (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        title    TEXT    NOT NULL,
        genre    TEXT    NOT NULL,
        year     INTEGER NOT NULL,
        rating   REAL    NOT NULL,
        director TEXT    NOT NULL,
        duration INTEGER NOT NULL,
        country  TEXT    NOT NULL,
        language TEXT    NOT NULL
    )
""")

movies = [
    # title,                          genre,       year, rating, director,                 dur, country,   language
    ("The Shawshank Redemption",      "Drama",     1994,  9.3,  "Frank Darabont",          142, "USA",     "English"),
    ("The Godfather",                 "Crime",     1972,  9.2,  "Francis Ford Coppola",    175, "USA",     "English"),
    ("The Dark Knight",               "Action",    2008,  9.0,  "Christopher Nolan",       152, "USA",     "English"),
    ("Schindler's List",              "Drama",     1993,  9.0,  "Steven Spielberg",        195, "USA",     "English"),
    ("Pulp Fiction",                  "Crime",     1994,  8.9,  "Quentin Tarantino",       154, "USA",     "English"),
    ("Inception",                     "Sci-Fi",    2010,  8.8,  "Christopher Nolan",       148, "USA",     "English"),
    ("Forrest Gump",                  "Drama",     1994,  8.8,  "Robert Zemeckis",         142, "USA",     "English"),
    ("Interstellar",                  "Sci-Fi",    2014,  8.7,  "Christopher Nolan",       169, "USA",     "English"),
    ("The Matrix",                    "Sci-Fi",    1999,  8.7,  "The Wachowskis",          136, "USA",     "English"),
    ("Goodfellas",                    "Crime",     1990,  8.7,  "Martin Scorsese",         146, "USA",     "English"),
    ("Parasite",                      "Thriller",  2019,  8.6,  "Bong Joon-ho",            132, "Korea",   "Korean"),
    ("Whiplash",                      "Drama",     2014,  8.5,  "Damien Chazelle",         107, "USA",     "English"),
    ("The Silence of the Lambs",      "Thriller",  1991,  8.6,  "Jonathan Demme",          118, "USA",     "English"),
    ("Spirited Away",                 "Animation", 2001,  8.6,  "Hayao Miyazaki",          125, "Japan",   "Japanese"),
    ("City of God",                   "Crime",     2002,  8.6,  "Fernando Meirelles",      130, "Brazil",  "Portuguese"),
    ("Joker",                         "Drama",     2019,  8.4,  "Todd Phillips",           122, "USA",     "English"),
    ("Avengers: Endgame",             "Action",    2019,  8.4,  "The Russo Brothers",      181, "USA",     "English"),
    ("Coco",                          "Animation", 2017,  8.4,  "Lee Unkrich",             105, "USA",     "English"),
    ("The Grand Budapest Hotel",      "Comedy",    2014,  8.1,  "Wes Anderson",            100, "Germany", "English"),
    ("Mad Max: Fury Road",            "Action",    2015,  8.1,  "George Miller",           120, "Australia","English"),
    ("La La Land",                    "Romance",   2016,  8.0,  "Damien Chazelle",         128, "USA",     "English"),
    ("Knives Out",                    "Thriller",  2019,  7.9,  "Rian Johnson",            130, "USA",     "English"),
    ("Get Out",                       "Horror",    2017,  7.7,  "Jordan Peele",            104, "USA",     "English"),
    ("Everything Everywhere",         "Sci-Fi",    2022,  7.8,  "The Daniels",             139, "USA",     "English"),
    ("Oppenheimer",                   "Drama",     2023,  8.3,  "Christopher Nolan",       180, "USA",     "English"),
    ("Barbie",                        "Comedy",    2023,  6.9,  "Greta Gerwig",            114, "USA",     "English"),
    ("Past Lives",                    "Romance",   2023,  7.9,  "Celine Song",             106, "USA",     "English"),
    ("Tár",                           "Drama",     2022,  7.5,  "Todd Field",              158, "USA",     "English"),
    ("RRR",                           "Action",    2022,  7.8,  "S. S. Rajamouli",         187, "India",   "Telugu"),
    ("The Zone of Interest",          "Drama",     2023,  7.4,  "Jonathan Glazer",         105, "UK",      "German"),
    ("Alien: Romulus",                "Horror",    2024,  7.2,  "Fede Álvarez",            119, "USA",     "English"),
    ("Drive",                         "Crime",     2011,  7.8,  "Nicolas Winding Refn",    100, "USA",     "English"),
    ("Prisoners",                     "Thriller",  2013,  8.1,  "Denis Villeneuve",        153, "USA",     "English"),
    ("Arrival",                       "Sci-Fi",    2016,  7.9,  "Denis Villeneuve",        116, "USA",     "English"),
    ("Hereditary",                    "Horror",    2018,  7.3,  "Ari Aster",               127, "USA",     "English"),
    ("Midsommar",                     "Horror",    2019,  7.1,  "Ari Aster",               148, "USA",     "English"),
    ("Portrait of a Lady on Fire",    "Romance",   2019,  8.1,  "Céline Sciamma",          122, "France",  "French"),
    ("Amélie",                        "Romance",   2001,  8.3,  "Jean-Pierre Jeunet",      122, "France",  "French"),
    ("Pan's Labyrinth",               "Fantasy",   2006,  8.2,  "Guillermo del Toro",      118, "Spain",   "Spanish"),
    ("Dune: Part Two",                "Sci-Fi",    2024,  8.5,  "Denis Villeneuve",        166, "USA",     "English"),
]

cursor.executemany("""
    INSERT INTO movies (title, genre, year, rating, director, duration, country, language)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", movies)

conn.commit()
conn.close()
print(f"✅ Database ready — {len(movies)} movies inserted into movies.db")
