#!/usr/bin/env python

import argparse, feedparser, sys

def reddit(option=None, subreddit=None):
    """
    Parses and prints the RSS feed for the reddit front page. If a subreddit
    is provided then the RSS feed for that subreddit will be printed instead.
    """
    url = "http://www.reddit.com/"
    suffix = ".rss"

    if subreddit and is_valid_subreddit(subreddit):
        url = append(url, subreddit)
    if option and is_valid_option: 
        url = append(url, option)

    rss = feedparser.parse(url + suffix)

    COLOR_OFF = '\033[0m'
    COLOR_RED = '\033[31m'
    COLOR_CYAN = '\033[36m'

    for post in rss["items"]:
        print "%s%s\n%s%s\n%s" % (COLOR_RED, post["title"], COLOR_CYAN, post["link"], COLOR_OFF)


def is_valid_subreddit(subreddit):
    """
    Returns true if the given subreddit is valid, false otherwise."

    If the feed returned by feedparser.parse has a key named "bozo_exception",
    then we've accessed a subreddit that does not exist.
    """

    subreddit_url = "http://www.reddit.com/" + subreddit + "/.rss"

    return not feedparser.parse(subreddit_url).has_key("bozo_exception")


def is_valid_option(option):
    """
    Returns true if the given option is valid, false otherwise.
    """

    return option in ['controversial', 'new', 'rising', 'top']


def append(url, s):
    """
    Returns the url appended with s (either an option or a subreddit).
    """
    return url + s + "/"


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--o', help="Options flag.")
    parser.add_argument('-sub', '--sub', help="Subreddit flag.")

    p = parser.parse_args(sys.argv[1:])
    v = vars(p)
    
    reddit(option=v["o"], subreddit=v["sub"])
