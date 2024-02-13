#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Print the post titles if subreddit is valid"""

    url = "https://www.reddit.com/r/{}/top/.json?limit=10".format(subreddit)
    headers = {
                  "User-Agent": "0x16-api_advanced:project:\
                   v1.0.0"
                    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    ten = response.json().get("data").get("children")
    [print(i.get("data").get("title")) for i in ten]
