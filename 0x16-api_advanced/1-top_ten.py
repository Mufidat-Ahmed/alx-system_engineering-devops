#!usr/bin/python3
"""Queries the reddit api and return the top 10 hot post"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts in the given subreddit."""

    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "TopTenHotPosts/1.0.0 (by /u/0x16-api_advanced:project)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    else:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
