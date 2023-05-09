#!/usr/bin/python3
'''function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
'''

import requests


def top_ten(subreddit):
    '''prints the top ten hot posts'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "chuks agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.ok:
        data = response.json().get("data", 0).get('children', 0)
        for post in data[:10]:
            post = post.get("data", None)
            print(post.get('title', None))
    else:
        print(None)
