def movie_organizer(*movies):
    movies_dictionary = {}
    for movie in movies:
        if movie[1] in movies_dictionary:
            movies_dictionary[movie[1]].append(movie[0])
        else:
            movies_dictionary[movie[1]] = [movie[0]]

    genres = sorted(movies_dictionary.keys(), key=lambda x: (-len(movies_dictionary[x]), x))
    result = ""
    for genre in genres:
        result += f"{genre} - {len(movies_dictionary[genre])}\n"
        for movie in sorted(movies_dictionary[genre]):
            result += f"* {movie}\n"

    return result.strip()

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

