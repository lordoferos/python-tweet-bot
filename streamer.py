"""Create stream object to follow discussion on "impeachwaiguru", "khalwale" and "kakamega"""""
# import json and tweepy
import json
import tweepy
# create a class to stream tweets
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, on_status):
        print("Error detected")


# Authenticate to Twitter 
auth = tweepy.OAuthHandler("dddddddddddddddddddd", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
auth.set_access_token("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj", "kkkkkkkkkkkkkkkkkkkkkkkkkyfyfuikkkkkkkkkkkk")

# Create API Object to interact with Twitter
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# Create a stream listener using the API object
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track = ["kakamega"])
