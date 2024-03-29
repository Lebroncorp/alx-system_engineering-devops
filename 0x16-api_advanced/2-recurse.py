#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit or None
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves titles of hot articles for a given subreddit."""
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa)'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check for redirection manually
        if response.status_code == 302:
            print(f"Redirected. Handle it accordingly.")
            return None

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            titles = [child.get(
                "data", {}
            ).get(
                "title", ""
            ) for child in children]
            hot_list.extend(titles)

            # Recursive call for the next page
            after = data.get("after")
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        return None
