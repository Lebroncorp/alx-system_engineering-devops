#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        'Edg/91.0.864.59'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
