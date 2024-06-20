#!/usr/bin/python3
"""0-subs module."""
import requests


def number_of_subscribers(subreddit):
    """
    This function tells us how many people like a certain book (subreddit)
    """
    # The address where we ask about the book.
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Our introduction to Reddit so they know who's calling.
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # We make the call to Reddit.
        reponse = requests.get(url, headers=headers, allow_redirrects=False)

        # If Reddit says "I know this book":
        if reponse.status_code == 200:
            data = reponse.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
