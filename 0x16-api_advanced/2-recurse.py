#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit """

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that queries Reddit API """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '2-recurse.py'}
    params = {'limit': 100, 'after': after}
    response = get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        after = response.json().get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
