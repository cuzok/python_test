import praw
import config

def bot_login():
    r = praw.Reddit(
        username = "cuzok",
        password = "reddit",
        client_id = "yl8xU18CjRzF5w",
        client_secret = "U4svRaf5cd8lOe6p92aX6MAvNaA",
        user_agent = "cuzoks first reddit bot v1.0")
    return r

r = bot_login()
print r
