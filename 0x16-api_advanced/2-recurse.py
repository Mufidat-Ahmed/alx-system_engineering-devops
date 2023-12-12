#!/usr/bin/python3
"""
returns a list containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns list containing the titles if the subreddit is valid"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\ v1.0.0"
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    lists = response.json().get("data")
    after = lists.get("after")
    count += lists.get("dist")
    for i in lists.get("children"):
        hot_list.append(i.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
