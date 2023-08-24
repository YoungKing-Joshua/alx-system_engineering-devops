#!/usr/bin/python3
"""Function to query subscribers Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    pathU = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    htag = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Use allow_redirects=False to prevent following redirects
    res = requests.get(pathU, headers=htag, allow_redirects=False)
    if res.status_code == 404:
        return 0

    # Parse the JSON response and extract the subscriber count
    results = res.json().get("data")
    return results.get("subscribers")
