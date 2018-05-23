# Reddit Post Flusher
#### A bot that delete all submissions except mod posts.

Posted by [GBWI](https://www.reddit.com/user/GBWI) in [/r/RequestABot](https://www.reddit.com/r/RequestABot):

> Hello.
> I am looking for bot who can delete all submissions every week (every monday) except mod posts.
> Can anyone help me regarding this topic?

***

## How to run Reddit Post Flusher
**0.** Install [Python](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe).

**1.** Go to [Reddit Apps](https://www.reddit.com/prefs/apps/) and register a new application. Give it a `name`, select `script`, give it a `description` and finally, set the `redirect uri` to **https://127.0.0.1**.

**2.** Clone this repository.

  `$ git clone https://github.com/crlsmnzs/Reddit-Post-Flusher` or download as a ZIP.

**3.** Open a terminal window in the location you cloned/extracted the repository to and install the modules in `requirements.txt`.

  `pip install -U -r requirements.txt`

**4.** Open `main.py` and edit the value of the variable `subName` to be the name of your subreddit (e.g: BlackPeopleTwitter, AskReddit, EarthPorn). You may close the file afterwards.

**5.** Open `praw.ini` and edit the values at the bottom.

***

## How to run Reddit Post Flusher... scheduled.

I added a `main_schedule.py` file which can be run once and then left open. It will then run every Monday at midnight. This would make more sense if you are running the script from a VPS — if you decide to run this script from home, just manually run `main.py` when needed.