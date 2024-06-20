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
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
