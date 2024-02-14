#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Print titles of 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/lebroncorp_tech_jr)"
    }
    title = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, title=title,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
