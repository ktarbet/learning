import os

import requests

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


class NewsApi:

    @staticmethod
    def search_in_title(title_query):
        args = {
            "apikey": os.environ.get("NEWS_API_KEY"),
            "qInTitle": title_query
        }
        response = requests.get(NEWS_ENDPOINT, args)
        response.raise_for_status()
        data = response.json()
        articles = data['articles']
        return articles


