"""
This is the main function of the Bernie bot.
"""
import random
import tweepy
import config

BERNIE_SCREEN_NAME = '@BernieSanders'
PAST_TWEET_NUM = 50  # The number of twitter that we search thru

# Api set up: this should go in main as soon as we have one, or make it global constant --Heng
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


def getAllTweets():
    """
     Get and print all Tweets from the bot timeline.
    @return: no return
    """
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def getUserTweet(userName):
    """
    Get the complete timeline from a user and store in a file.
    @param userName: the user name of the target account
    @return: no return
    """
    for status in tweepy.Cursor(api.user_timeline, screen_name=userName,
                                tweet_mode="extended").items():
        with open(userName + '.txt', 'a+') as f:
            f.write(status.full_text)


def searchUserTweet(userName, keyword):
    """
    Search for a number of (PAST_TWEET_NUM) past tweets about a specific key word from a user (
    and store in a file).
    @param userName: the user name of the target account
    @param keyword: the keyword to be included in every tweet
    @return: a list of tweets on this matter
    """
    tweets = []
    # Next time: fix this with JSON?
    # This can be made easier with Tweepy's own search commands.
    # Also next time: fix upper/ lower case problems.
    for status in tweepy.Cursor(api.user_timeline, screen_name=userName,
                                tweet_mode="extended").items():
        if keyword in str(status):  # str is not working. try JSON next time
            with open(userName + "_on_" + keyword + '.txt', 'a+') as f:
                f.write(status.full_text + "\n\n")
            tweets.append(status)

    return tweets


def getRandomPastSpeech(userName, keyword):
    """
    Get a random past speech on a topic. Need to be tested next time. --Heng
    @param userName: the user name of the target account
    @param keyword: the keyword to be included in the tweet of interest.
    @return: the random speech on a topic or a message indicating not found.
    """
    pool = searchUserTweet(userName, keyword)  # might use a search past 100 User Tweet function
    if len(pool) != 0:
        message = pool[random.randint(0, len(pool))]
    else:
        message = "Huh, Bernie has never ever mentioned " + keyword + ". Didn't know about that."

    return message


# user = api.get_user('BernieSanders')
# public_tweets = api.user_timeline('BernieSanders')
# for tweet in public_tweets:
# print(tweet.text)
print("Testrun Start")
# api.update_status(message)
# getUser()
# getUserTweet(BERNIE_SCREEN_NAME)
tweetPastSpeech(BERNIE_SCREEN_NAME, 'health')
print("Testrun Over")
