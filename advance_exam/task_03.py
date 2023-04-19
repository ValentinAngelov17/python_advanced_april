def movie_organizer(*movies):
    finnal_dict = {}
    for movies, gen in movies:
        if gen in finnal_dict:
            finnal_dict[gen].append(movies)
        else:
            finnal_dict[gen] = [movies]

    genres = sorted(finnal_dict.keys(), key=lambda z: (-len(finnal_dict[z]), z))
    final = ""
    for genre in genres:
        final += f"{genre} - {len(finnal_dict[genre])}\n"
        for movie in sorted(finnal_dict[genre]):
            final += f"* {movie}\n"

    return final.strip()


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