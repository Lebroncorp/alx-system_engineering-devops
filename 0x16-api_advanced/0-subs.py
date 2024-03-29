#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa)'}, allow_redirects=False).json()

    if r.statusCode == 302:
        return 0

    if r.statusCode == 200:
        subs = r.get("data", {}).get("subscribers", 0)
    return subs
