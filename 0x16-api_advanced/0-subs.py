#!/usr/bin/python3
"""
0-subs module.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function tells us how many people like a certain book (subreddit)
    """
    # The address where we ask about the book.
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
