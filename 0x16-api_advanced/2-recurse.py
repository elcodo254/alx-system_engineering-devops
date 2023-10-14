#!/usr/bin/python3
"""queries Reddit API, returns articles w/titles for subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """prints titles of 10 1st hot posts"""
    if subreddit is None or type(subreddit) is not str:
        return None

    BASE_URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'Mozilla/5.0'}
    par = {'after': after}

    r = requests.get(BASE_URL, params=par, headers=head).json()

    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)

    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))

    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
