#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """return total subscribers for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    u = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
            v1.0.0'}).json()
    subs = u.get("data", {}).get("subscribers", 0)
    return subs
