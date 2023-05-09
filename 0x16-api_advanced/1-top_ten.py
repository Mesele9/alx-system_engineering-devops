#!/usr/bin/python3
"""Title of top 10 hot post"""

from requests import get


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': "Google Chrome version 112.0.5615.121"}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    
    response = get(url, headers=user_agent, params=params)
    result = response.json()

    try:
        datas = result.get('data').get('children')
        for i in datas:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
