#!  Code using tweepy follow my followers bot
import tweepy
import logging
from config import create_api
import time
# import the config file
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()
# create a logger object
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
# create a main object
def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()