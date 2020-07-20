import tweepy
import time

covid_19 = {'COVID-19', 'COVID', 'coronavirus', 'corona virus', 'corona'}

medicine = {'medicine', 'health', 'hospital', 'patient', 'healthcare', 'medical', 'doctor'}

politics = {'politic', 'democratic', 'republic'}

education = {'education', 'school', 'university'}

united_states = {'US', 'America', 'USA'}

catalog = [covid_19, medicine, politics, education, united_states]

consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)



#for follower in tweepy.Cursor(api.followers).items():
    #follower.follow()
   # print ("Followed everyone that is following " + user.name)

def mainFunction():
    search = "bernieee"
    numberOfTweets = 20
    tweetId = tweet.user.idusername = tweet.user.screen_name
    phrase = "healthcare for all and eat the rich"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id =tweetId)
            print("Replied with " + phrase)
        except tweepy.TweepError as e:\
                print(e.reason)
        except StopIteration:
            break


def findKeyword(message):
    """
    find the keyword in a message
    :param message:
    :param keyword_bank:
    :return: the index of list of keywords in keyword bank
    :return: the first set of keywords in keyword bank that is mentioned
    """
    for category in catalog:
        for word in category:
            if word in message:
                return category
    return {}

FILE_NAME = 'last_seen_id1'
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    twt_healthcare = api.mentions_timeline(last_seen_id)
    for mention in reversed(twt_healthcare):
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

    for s in twt_healthcare:
        tweet1 = (findKeyword(s.text))
        if tweet1 == covid_19:
            sn = s.user.screen_name
            m = '@%s The coronavirus is a global pandemic!' % (sn)
            s = api.update_status(m, s.id)
        elif tweet1 == medicine:
            sn = s.user.screen_name
            m = '@%s free healthcare for all!' % (sn)
            s = api.update_status(m, s.id)
        elif tweet1 == politics:
            sn = s.user.screen_name
            m = '@%s This is my political campaign.' % (sn)
            s = api.update_status(m, s.id)

while True:
    reply_to_tweets()
    time.sleep(15)
