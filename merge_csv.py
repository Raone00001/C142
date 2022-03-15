# Import all modueles
import csv

# Open the csv file and store data and header into the vars
with open('movies.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

# Append poster_link column
headers.append("poster_link")

# Create new csv file with the new header
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

# Open the csv file and read the data
with open("movie_links.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

# Merge the poster link according to the movie name
for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)