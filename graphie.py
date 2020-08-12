import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("d4Jl6eH8AiYcXkuAwrgkM6gJ3", "Z5bhyKoDiOiKU9Uu9zPoxnKdAKShONdgsTkcKXeJLhuaJtqkSJ")
auth.set_access_token("892981240667807744-rfF45SbCK9Yu0byTPoVLxQTyEDMvg2g", "Mx67izXSpNVkhc4wHvwEAn90dknkHoq7dv0W9RRTf28di")

# Create API Object
api = tweepy.API(auth)

# Create a tweet
api.update_status("https://www.dailyupdates.co.ke/2019/11/who-is-edgar-obare-closer-look-into.html")