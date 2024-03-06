#!/usr/bin/python3
'''queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit'''

from requests import get


def top_ten(subreddit):
    ''' function queries Reddit API and get titles of first 10 hot posts '''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {"User-Agent": "1-top_ten.py"}
    param = {"limit": 10}
    response = get(url, params=param, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("children")
        for post in data:
            print(post.get("data", {}).get("title", None))
    else:
        print("None")
