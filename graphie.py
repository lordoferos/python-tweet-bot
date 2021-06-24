import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("yyyyyyyyyyyyyyyyyyyyyyyyyy", "fffffffffffffffffffffffffffffff")
## the authentification credentials are hidden
auth.set_access_token("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", "jcmktegdhdddddddddddddddddddd")

# Create API Object
api = tweepy.API(auth)

# Create a tweet
api.update_status("https://www.dailyupdates.co.ke/2019/11/who-is-edgar-obare-closer-look-into.html")
