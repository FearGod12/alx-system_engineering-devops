#!/usr/bin/python3
'''ecursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''returns a list containing the titles of all hot posts'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "custom agent"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.ok:
        data = response.json().get("data").get("children")
        for post in data:
            hot_list.append(post.get("title"))
        if response.json().get("data").get("after"):
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
    else:
        return None
