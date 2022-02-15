#!/usr/bin/python3
"""Get all articles in a specific subreddit"""
import json
import requests


def recurse(subreddit, hot_list=[], idx=0, response=None, after=''):
    """Recursion with request to each after(page)"""
    if idx == 0:
        user_agent = {'User-agent': 'Mozilla/5.0'}
        page = ("https://www.reddit.com/r/{}/hot.json{}"
                .format(subreddit, after))
        response = requests.get(page, headers=user_agent)
    if response.status_code == 301:
        return None
    elif response.status_code == 200:
        info = json.loads(response.content)
        if idx >= len(info['data']['children']):
            if info['data']['after'] is not None:
                after = '?after=' + info['data']['after']
                idx = 0
                return recurse(subreddit, hot_list, idx, response, after)
            else:
                return hot_list
        hot_list.append(info['data']['children'][idx]['data']['title'])
        idx += 1
        return recurse(subreddit, hot_list, idx, response, after)
    else:
        return None
