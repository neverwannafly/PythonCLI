#!/usr/bin/env python3
import requests

# This script uses the api from newsapi.org
url = ("https://newsapi.org/v2/top-headlines?country=us&apiKey=4da594962b464023be460b8c5443d776")

article_format = """
------------------------------------------------------------------
\t{article_title}
\t\t\tAuthor: {article_author}
\t\t\tPublished on: {article_publishtime}\n
{article_description}\n
------------------------------------------------------------------
"""

def prettyPrint(response):
    if response.get("status", "bad")=="ok":
        for article in response.get("articles", []):
            article_title = article.get("title", "N/A")
            article_author = article.get("author", "Anonymous")
            article_description = article.get("description", "N/A")
            article_publishtime = article.get("publishedAt", "N/A")
            new_article =article_format.format(
                article_title = article_title,
                article_author = article_author,
                article_description = article_description,
                article_publishtime = article_publishtime,
            )
            print(new_article)
            response = input("Press Enter to read more and X to close")
            if response=='X' or response=='x':
                break
        print("We've reached the end!")
    else:
        print("Snap! Something went wrong!")

def execute_news():
    response = requests.get(url)
    prettyPrint(response.json())