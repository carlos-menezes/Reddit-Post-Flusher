import praw
from requests_html import HTMLSession
import time

reddit = praw.Reddit('bot1')

subName = "subreddit" # Name of your subreddit
url = "https://old.reddit.com/r/{}/about/moderators"
session = HTMLSession()
r = session.get(url.format(subName))

mods = []

if str(r) == "<Response [403]>":
    print("Subreddit is private. Can't continue.")
    time.sleep(3)
    exit()

if str(r) == "<Response [200]>":
    users = r.html.find('span.user')
    for user in users[1:]:
        moderator = user.text.split("\xa0")[0]
        mods.append(moderator)

    for submission in reddit.subreddit(subName).new(limit=None):
        if submission.author not in mods:
            submission.mod.remove()
