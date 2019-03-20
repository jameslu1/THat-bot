import praw
import pdb
import re
import os

def main():
    #initialize bots
    r = praw.Reddit('bot1')
    subreddit = r.subreddit("hiphopcirclejerk")

    for comment in subreddit.stream.comments(skip_existing=True):
        if re.search("!hoovaq", comment.body, re.IGNORECASE):
            reply = ""
            if comment.is_root:
                reply = comment.parent().title + " | " + comment.parent().title.replace("h","H")
            else:
                reply = comment.parent().body + " | " + comment.parent().body.replace("h","H")
            comment.reply(reply)
            print("Comment: " + comment.body)


if __name__=="__main__":
    main()
