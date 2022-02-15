#!/usr/bin/python3
"""Get top 10 articles in a specific sudreddit"""
import json
import requests


def top_ten(subreddit):
    """Get first 10 articles using requests"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(page, headers=user_agent,
                            allow_redirects=False)
    if response.status_code == 404:
        print(None)
    else:
        info = response.json()
        count = 0
        for post in info.get('data').get('children'):
            print(post.get('data').get('title'))
            count += 1
            if count >= 10:
                break
