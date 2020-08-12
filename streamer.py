"""Create stream object to follow discussion on "impeachwaiguru", "khalwale" and "kakamega"""""
import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, on_status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("dddddddddddddddddddd", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
auth.set_access_token("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

# Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track = ["kakamega"])
