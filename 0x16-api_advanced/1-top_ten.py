#!/usr/bin/python3

import json
import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(page, headers=user_agent)
    if response.status_code == 200:
        info = json.loads(response.content)
        count = 0
        for post in info['data']['children']:
            print(post['data']['title'])
            count += 1
            if count >= 10:
                break
    else:
        print(None)
