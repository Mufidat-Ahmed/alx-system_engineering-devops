#!/usr/bin/python3
"""contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced:project:\v1.0.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    ten = response.json().get("data")
    [print(i.get("data").get("title")) for i in ten.get("children")]
