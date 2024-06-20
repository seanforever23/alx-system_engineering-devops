#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
  """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

  Args:
    subreddit: The name of the subreddit to query.

  Returns:
    None
  """
  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  headers = {'User-agent': 'your_user_agent'} # Replace with your user agent

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Raise an exception for bad status codes

    data = response.json()
    posts = data['data']['children']
    
    if len(posts) >= 10:
      for i in range(10):
        print(posts[i]['data']['title'])
    else:
      print("Subreddit does not have enough posts.")

  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print("None")

# Example usage
top_ten("python")
