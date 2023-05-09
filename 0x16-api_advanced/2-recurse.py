#!/usr/bin/python3
""" Recursive function that query Reddit API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    global after
    user_agent = {'User-agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    result = requests.get(url, params=parameters, headers=user_agent,
                          allow_redirects=False)
    if result.status_code == 200:
        next_data = result.json().get("data").get("after")
        if next_data is not None:
            after = next_data
            recurse(subreddit, hot_list)
        all_titles = result.json().get("data").get("children")
        for title in all_titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
