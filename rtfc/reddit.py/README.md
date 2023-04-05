reddit.py -- View reddit's RSS feed from your terminal.
=======================================================

[0.0] Change Log
----------------

* 1.0 -- Project started. May update soon if I find something that could work better.

[0.1] Table of Contents
-----------------------

* [0.0] -- Change Log
* [0.1] -- Table of Contents
* [1.0] -- What is reddit.py?
* [2.0] -- Installing reddit.py
* [3.0] -- Using reddit.py

[1.0] What is reddit.py?
------------------------

`reddit.py` provides an easy, conventient terminal command that will parse and print the RSS feed for the reddit front page, or any of reddit's subreddits.

[2.0] Installing reddit.py
--------------------------

Installing `reddit.py` couldn't be easier. Using Python's Distutils module allows you to install `reddit.py` by simply typing `python setup.py install` into the command line. (1)

(1) Some people may find that they need to run `sudo python setup.py install` instead.

[3.0] Using reddit.py
---------------------

Just like installing `reddit.py`, running it couldn't be simpler. 

There are four ways to run `reddit.py`:

* `reddit` -- Displays the RSS feed for the front page.
* `reddit [option]` -- Displays the RSS feed corresponding to [option].
* `reddit [subreddit]` -- Displays the RSS feed corresponding to [subreddit].
* `reddit [option] [subreddit]` -- Displayers the RSS feed corresponding to both [option] and [subreddit].

Valid [subreddit] values include:

* Any existing subreddit.

Valid [option] values include:

* controversial
* new
* rising
* top
