import praw
from selenium import webdriver
from loginfunc import openLogin
from mainvideofunc import createVideo

username = "bot_username"
password = "bot_password"

driver = webdriver.Chrome()

openLogin(driver, password, username)

reddit = praw.Reddit(
    client_id="T8E4zePolqmX00d4jTEN0A",
    client_secret="C4UDTaG5J4iK-1POcRWogUC_fvY-Fg",
    password="teo123meansgood",
    user_agent="auto_insta_bot",
    username="reddit_bot_masti",
)

print("Login successful")



#########################################################################################################################
"""
    important commands : 
    https://praw.readthedocs.io/en/latest/code_overview/models/submission.html#praw.models.Submission    
"""
########################################################################################################################


bgcount = 1

listsub = []
n = int(input("Number of Subreddits : "))
for i in range(n):
    a = input("name of subreddit : ")
    listsub.append(a)

for sub in listsub:
    createVideo(reddit, driver, sub, bgcount)
