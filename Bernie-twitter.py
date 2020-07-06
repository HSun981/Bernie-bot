"""
This is the main function of the Bernie bot.
"""
import random
import tweepy
import config
import time

BERNIE_SCREEN_NAME = '@BernieSanders'
PAST_TWEET_NUM = 50  # The number of twitter that we search thru

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

#generative code from other doc
import re
import random
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from collections import defaultdict, deque
from Berniespeech1 import training_doc1
from Berniespeech2 import training_doc2
from Berniespeech3 import training_doc3


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

#setting up time
while True:
    generated_text = my_markov.generate_text()
    api.update_status(generated_text)
    time.sleep(15)

# user = api.get_user('BernieSanders')
# public_tweets = api.user_timeline('BernieSanders')
# for tweet in public_tweets:
# print(tweet.text)
#print("Testrun Start")
# api.update_status(message)
# getUser()
# getUserTweet(BERNIE_SCREEN_NAME)
#tweetPastSpeech(BERNIE_SCREEN_NAME, 'health')
#print("Testrun Over")
