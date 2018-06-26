#!/usr/bin/env python3
import urllib
import requests

url = "https://api.pexels.com/v1/curated?per_page=15&page=1"
headers = {
    'Authorization': '563492ad6f917000010000018a0936ccd958477ba6102be6f211c599'
}

def execute_wallpaper():
    num = 1
    response = requests.get(url, headers=headers).json()
    photos_url = [obj['src']['original'] for obj in response['photos']]
    for link in photos_url:
        print(link) 
