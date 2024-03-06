#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

from requests import get


def number_of_subscribers(subreddit):
    '''function that queries REDDIT API and returns number of subscribers'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Uko Uwatt"}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
