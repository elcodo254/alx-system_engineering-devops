#!/usr/bin/python3
"""function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """Querries and returns total number of subscribers on a subreddit."""
    try:
        rq = requests.get('https://www.reddit.com/r/{}/about.json'.
                          format(subreddit),
                          headers={'User-Agent': 'custom'},
                          allow_redirects=False)
        return rq.json().get('data').get('subscribers')
    except:
        return 0
