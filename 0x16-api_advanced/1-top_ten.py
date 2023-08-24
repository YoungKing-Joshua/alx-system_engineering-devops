#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    htag = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # URL for the hot posts API endpoint with a limit of 10
    pathU = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "limit": 10
    }

    # Use allow_redirects=False to prevent following redirects
    res = requests.get(pathU, headers=htag, params=params,
                       allow_redirects=False)

    # Check for a 404 status code to handle invalid subreddits
    if res.status_code == 404:
        print("None")
        return

    # Parse the JSON response and print the titles of the hottest posts
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]


# Test the function
if __name__ == '__main__':
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)
