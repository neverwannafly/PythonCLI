#!/usr/bin/env python3
import requests
import sys

url = ('http://quotes.rest/qod.json')

quote_format = """
 ----------------------------------
|         Quote of the day         |
 ----------------------------------
 {quote_body}\n
                    \t\t-by : {quote_author}
                    \t\t©{quote_copyright}
"""

def execute_quote():
    response = requests.get(url)
    quote_object = response.json()
    quote_body = quote_object["contents"]["quotes"][0]["quote"]
    quote_author = quote_object["contents"]["quotes"][0]["author"]
    quote_copyright = quote_object["contents"]["copyright"]
    print(quote_format.format(
        quote_body=quote_body,
        quote_author=quote_author,
        quote_copyright=quote_copyright,
    ))