import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
content= requests.get(URL).text

soup = BeautifulSoup(content,"html.parser")

items = soup.find_all(name="h3", class_="title")
items.reverse()

with open("movies.txt", "w", encoding="utf-8") as f:
    for movie in items:
        print(movie.getText())
        f.write(movie.getText())
        f.write("\n")
