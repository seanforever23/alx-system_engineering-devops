#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    url = f"https://oauth.reddit.com/r/{subreddit}/hot"
    headers = {"User-Agent": "my-reddit-bot/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        print(None)
