import praw
import re
import requests
import datetime

reddit = praw.Reddit('hardwareswapstats')
subreddit = reddit.subreddit("funny")

def email_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/HWS_notification_gmail/with/key/cZeYR3pOgWj7CZMa5gQT5J", data=report)


for post in subreddit.stream.submissions(): #check new posts:
	if re.search("the", post.title, re.IGNORECASE):
		print("Title: ", post.title)
		print(datetime.datetime.now())
		print("---------------------------------\n")
		#email_alert(post.title, "foo", "foo")
	else:
		continue
