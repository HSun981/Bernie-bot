##
# This is to get Tweets from a account
##
import tweepy

##
# The key and secret for Bernie-bot2.0
consumer_key = "Ulo6zYN4J6LQu23c3NCoFX0rh"
consumer_secret = "t4ErUnVCsJ6v88vhmB5olHHSUJiC4amYgcCcyxWajyW6ZB3Jlm"
access_token = "1244663487147671559-2TpqoL9UTCqzhLhlSWYIZM9TsW82dF"
access_token_secret = "Ne8rdcEwKOUHNJrz5Fr3uWA6h8qODWENDSPO5fXFQr6aV"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

##
# Get and print all Tweets from the timeline
def getAllTweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

##
# Tweet a message
# @param message the message to be tweeted
def tweet(message):
    api.update_status(message)

#jared
print("Testrun Start")
tweet("Hello World!")
getAllTweets()
print("Testrun Over")
