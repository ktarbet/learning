import os
from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for article in articles:
    txt = article.find("a").getText()
    article_text.append(txt)
    link = article.find("a").get("href")
    article_link.append(link)

article_scores = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_scores = [int(s.split()[0]) for s in article_scores]
print(article_text)
print(article_link)
print(article_scores)

m = max(article_scores)
print(m)
index_of_max = article_scores.index(m)
print(index_of_max)
print(article_text[index_of_max])
print(article_link[index_of_max])
