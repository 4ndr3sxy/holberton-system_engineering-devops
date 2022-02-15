#!/usr/bin/python3
"""Get subcribes in an specific sudreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """Structure using module requests"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(page, headers=user_agent)
    if response.status_code == 200:
        info = json.loads(response.content)
        return info['data']['subscribers']
    return 0
