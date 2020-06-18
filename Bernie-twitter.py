##
# This is to get Tweets from a account
##
import tweepy

import config
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
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
