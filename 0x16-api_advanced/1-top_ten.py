#!/usr/bin/python3
"""Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """10 reddit apI
    """
    if subreddit is None or type(subreddit) != str:
        print('None')
        return
    params = {'limit': 10}
    headers = {'User-Agent': 'Reddit apI'}
    url = "http://www.reddit.com/r/{}/top/.json".format(subreddit)
    res = requests.get(url, params=params,
                       headers=headers)
    if res.status_code != 200:
        print('None')
        return
    resp = res.json().get('data').get('children')
    for child in resp:
        print(child.get('data').get('title'))
