#!/usr/bin/python3
"""Function that queries the Reddit API
prints a sorted count of given keywords from title of all hot articles"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Prints sorted counts of given words
    found in hot posts of a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {
            "limit": 100,
            }

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/Various_Ad_2057)"
        }

    if counts is None:
        counts = {}

    if after is None:
        # convert word_list to lowercase and remove duplicates
        word_list = list(set([word.lower() for word in word_list]))
    else:
        params['after'] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    after = response.json().get('data').get('after')

    data = response.json().get('data').get('children')
    titles = [post.get('data').get('title').lower() for post in data]

    for title in titles:
        for word in title.split():
            if word.lower() in word_list:
                key = word.lower()
                counts[key] = counts.get(key, 0) + 1

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
    else:
        return count_words(subreddit, word_list, counts, after)
