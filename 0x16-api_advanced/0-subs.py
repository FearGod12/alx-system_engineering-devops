#!/usr/bin/python3
''' function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit'''

import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers in a given sureddit'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "chuks agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.ok:
        data = response.json().get("data", 0)
        return data.get('subscribers', 0)
    return 0
