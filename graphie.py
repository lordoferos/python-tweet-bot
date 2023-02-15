import tweepy

# Authenticate to Twitter using the credentials provided in the twitter developer account
auth = tweepy.OAuthHandler("yyyyyyyyyyyyyyyyyyyyyyyyyy", "fffffffffffffffffffffffffffffff")
## the authentification credentials are hidden for security reasons
auth.set_access_token("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", "jcmktegdhdddddddddddddddddddd")

# Create API Object to interact with Twitter
api = tweepy.API(auth)

# Create a tweet using the API object
api.update_status("https://www.dailyupdates.co.ke/2019/11/who-is-edgar-obare-closer-look-into.html")
