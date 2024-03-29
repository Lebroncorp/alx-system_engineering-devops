#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of 10 hottest posts on the given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/limit=10.json".format(subreddit)

    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json()
    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            print(post['data']['title'])
