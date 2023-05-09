#!/usr/bin/python3
""" a function that queries number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """ a fucntion that queries Reddit API and return number
    of subscriber """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': "Google Chrome version 112.0.5615.121"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    result = response.json()

    try:
        return result.get('data').get('subscribers')
    except Exception:
        return 0
