"""
This is the main function of the Bernie bot.
"""
import random
import tweepy
import config
import time
import re
import random
import Keyword_Bank
import BernieBotM4A

from nltk.tokenize import word_tokenize
from collections import defaultdict, deque
from Berniespeech1 import training_doc1
from Berniespeech2 import training_doc2
from Berniespeech3 import training_doc3

BERNIE_SCREEN_NAME = '@BernieSanders'       # Bernie's twitter screen name
FILE_FOR_LAST_ID = 'last_seen_id1'     # last tweet id that we processed
REPLY_INTERVAL = 60                     # the interval to reply
TWEET_LIMIT = 280                       # the number of characters allowed in a tweet

# Api set up: this should go in main if we have one, or make it global constant? --Heng
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


def searchApiTweet(keyword, count):
    """
    Modified based on https://stackoverflow.com/questions/49098726/extract-tweets-with-some
    -special-keywords-from-twitter-using-tweepy-in-python
    not tested yet

    :param keyword:
    :param count:
    :return:
    """
    # empty list to store parsed tweets
    tweets = []
    target = io.open("mytweets.txt", 'w', encoding='utf-8')
    # call twitter api to fetch tweets
    fetched_tweets = api.search(keyword, count=count)
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:
        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line + "\n")
    return tweet


def praseTweet(original):
    """
    Take out the http part of a tweet list. Adapted from online.
    :param original: the original
    :return: prased tweet with no http part.
    """
    prased = []
    for status in original:
        parsed.append(status.full_text)
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line + "\n")

    return prased


def searchUserTweet(userName, category, num_tweets):
    """
    Search for a number of past tweets about a specific key word from a user (
    and store in a file).

    @param userName: the user name of the target account
    @param category: the set of keyword to be included in every tweet
    @param num_tweets: the number of tweets to get
    @return: a list of tweets on this matter
    """
    tweets = []
    count = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=userName,
                                tweet_mode="extended").items():
        if not status.retweeted:
            for keyword in category:
                if keyword.lower() in status.full_text.lower():
                    # The commented out part is for generating a file to debug and take record,
                    # un-comment it as you need
                    # Have not debugged after switching from single keyword to category

                    # with open(userName + "_on_" + keyword + '.txt', 'a+') as f:
                    #     f.write(status.full_text + "\n\n")
                    tweets.append(status)
                    count += 1
        if count >= num_tweets:
            break

    return tweets


def getRandomPastSpeech(userName, category, num_tweets=30):
    """
    Get a random past speech on a topic. Being updated to search for a set of keywords. -Heng

    @param userName: the user name of the target account
    @param category: the set of keywords to be included in the tweet of interest.
    @return: the random speech on a topic or a message indicating not found.
    """
    pool = searchUserTweet(userName, category, num_tweets)
    if len(pool) != 0:
        message = pool[random.randint(0, len(pool))].full_text
    else:
        message = "Huh, Bernie has never mentioned anything about " + random.sample(category, 1) \
                  + ". Didn't know that."

    return message


def findKeyword(message):
    """
    find the keyword in a message
    :param message:
    :return: the first set of keywords in keyword bank that is mentioned; returns an empty set if no
     existing set matches
    """
    for category in Keyword_Bank.catalog:
        for word in category:
            if word.lower() in message.lower():
                return category
    return {}


def GenerateReply(tweet):
    """
    Generate a reply to a twitter
    :param tweet: The twitter to reply to, must be a tweet object
    :return: The message to reply with
    """
    # Will need to throw an exception here if tweet is not a tweet object
    category = findKeyword(tweet.full_text)

    # General element in all replies
    message = "@%s " % tweet.user.screen_name
    message = message + "Hello " + tweet.user.name + "!\n"

    # No Keyword Found
    if category == {}:
        message = message + "I didn't understand what you were trying to say."

    # Found Jared's Keyword
    elif category == Keyword_Bank.medicare_for_all:
        message = "@%s " % tweet.user.screen_name + medicare_for_all(tweet) # call Jared's function here to
        # generate new reply; might need to also track the thread

    # Found Keyword for SyBBURE presentation demo
    elif category == Keyword_Bank.sybbure:
        if 'answer' in tweet.full_text:       # answer keyword to a random riddle
            message = message + "That is correct, congrats!\nTeam Bernie bot loves you!"
        else:
            message = message + "Wrong answer. Try again!"

    # Found any other keywords
    else:
        message = message + "As Bernie once said: \n"
        message = message + getRandomPastSpeech(BERNIE_SCREEN_NAME, category)

    return message[:TWEET_LIMIT]

def retrieve_last_seen_id():
    """
    to retrieve last seen tweet id so it doesn't try to reply to the same tweet twice
    This function is adapted from Bernie-reply-code.
    :return: the id of last twitter processed
    """
    f_read = open(FILE_FOR_LAST_ID, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id):
    """
    to store last seen tweet id so it doesn't try to reply to the same tweet twice
    This function is adapted from Bernie-reply-code.
    """
    f_write = open(FILE_FOR_LAST_ID, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()


def reply_to_tweets(last_seen_id):
    """
    gets all tweets that @ the bernie bot, searches the keyword bank agaisnt them, and replies
    based on keyword category
    This function is adapted from Bernie-reply-code.
    """
    twt_to_reply = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    new_last_id = -1     # no change happened
    for mention in reversed(twt_to_reply):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        api.update_status(GenerateReply(mention), mention.id)
        new_last_id = mention.id
    return new_last_id


def delete_tweets_about(keyword):
    """
    A convenient function to delete all tweets that the bot produced having a certain keyword.
    :param keyword: the keyword with which the tweet shall be deleted
    :return: the number of tweets deleted
    """
    num_deleted = 0
    for tweet in api.home_timeline():
        if keyword in tweet.text:
            api.destroy_status(tweet.id)
            num_deleted = num_deleted + 1
    for tweet in api.mentions_timeline():
        if keyword in tweet.text:
            api.destroy_status(tweet.id)
            num_deleted = num_deleted + 1


def medicare_for_all(tweet):
    '''
    determines tweet subject and replies with relevant response
    :param tweet: the user tweet that you reply to
    :return: the message to be included in the reply tweet
    '''
   
    subject = ""
    response = tweet.full_text.lower()

    for words in BernieBotM4A.pharma_words:
        if response.__contains__(words):
            if response.__contains__("influence") or response.__contains__("power"):
                return BernieBotM4A.pharma_response
            elif response.__contains__("single-payer"):
                return BernieBotM4A.pharma_response_2
            elif response.__contains__("fight") or response.__contains__("defeat"):
                return BernieBotM4A.pharma_response_3
            elif response.__contains__("private") or response.__contains__("optional"):
                return BernieBotM4A.pharma_response_4
            else:
                return BernieBotM4A.retry_message
 


# The real main function
# Get the last seen id from last run
last_seen_id = retrieve_last_seen_id()

#generative portion of code


class MarkovChain:
    def __init__(self):
        self.lookup_dict = defaultdict(list)
        self._seeded = False
        self.__seed_me()

    def __seed_me(self, rand_seed=None):
        if self._seeded is not True:
            try:
                if rand_seed is not None:
                    random.seed(rand_seed)
                else:
                    random.seed()
                self._seeded = True
            except NotImplementedError:
                self._seeded = False

    def add_document(self, str):
        preprocessed_list = self._preprocess(str)
        pairs = self.__generate_tuple_keys(preprocessed_list)
        for pair in pairs:
            self.lookup_dict[pair[0]].append(pair[1])

    def _preprocess(self, str):
        cleaned = re.sub(r'\W+', ' ', str).lower()
        tokenized = word_tokenize(cleaned)
        return tokenized

    def __generate_tuple_keys(self, data):
        if len(data) < 1:
            return

        for i in range(len(data) - 1):
            yield [data[i], data[i + 1]]

    def generate_text(self, max_length=280):
        context = deque()
        output = []
        if len(self.lookup_dict) > 0:
            self.__seed_me(rand_seed=len(self.lookup_dict))
            chain_head = [list(self.lookup_dict)[0]]
            context.extend(chain_head)

            while len(str(output)) < (max_length - 1):
                next_choices = self.lookup_dict[context[-1]]
                if len(next_choices) > 0:
                    next_word = random.choice(next_choices)
                    context.append(next_word)
                    output.append(context.popleft())
                else:
                    break
            output.extend(list(context))
        return " ".join(output)




my_markov = MarkovChain()
my_markov.add_document(training_doc1)
my_markov.add_document(training_doc2)
my_markov.add_document(training_doc3)

# iterates through the search for keyword and reply process every REPLY_INTERVAL of seconds
while True:
    new_id = reply_to_tweets(last_seen_id)
    if new_id != -1:        #if is change where at least a new tweet was replied
        last_seen_id = new_id
        store_last_seen_id(last_seen_id)
    generated_text = my_markov.generate_text()
    api.update_status(generated_text)
    time.sleep(REPLY_INTERVAL)





# user = api.get_user('BernieSanders')
# public_tweets = api.user_timeline('BernieSanders')
# for tweet in public_tweets:
# print(tweet.text)
# print("Testrun Start")
# api.update_status(message)
# getUser()
# getUserTweet(BERNIE_SCREEN_NAME)
# tweetPastSpeech(BERNIE_SCREEN_NAME, 'health')
# print("Testrun Over")


# Test creating a Markov from twitter
with open('Bernie-twitter.py', 'r') as file:
    content = file.read().replace('\n', '')
tweet_markov = MarkovChain()
tweet_markov.add_document(content)
generated_text = my_markov.generate_text()
api.update_status(generated_text)

# Jared says hi
