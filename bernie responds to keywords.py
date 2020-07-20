import tweepy

consumer_key = "XXXX"
consumer_secret = "XXXX"
access_token = "1XXXX"
access_token_secret = "XXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)

twt_healthcare = api.search(q="Bernie Sanders healthcare")

#list of specific strings we want to check for in Tweets
t = ['bernie sanders' and 'healthcare',
    'bernie sanders and healthcare']

for s in twt_healthcare:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s free healthcare for all!! :)" % (sn)
            s = api.update_status(m, s.id)

twt_taxes = api.search(q="Bernie Sanders taxes")

#list of specific strings we want to check for in Tweets
t = ['bernie sanders' and 'taxes',
    'what does bernie sanders think about taxes']

for s in twt_taxes:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Eat the rich..." % (sn)
            s = api.update_status(m, s.id)

twt_greeting = api.search(q="hey Bernie Sanders")

#list of specific strings we want to check for in Tweets
t = ['bernie sanders' and 'greetings',
    'hey bernie sanders!']

for s in twt_greeting:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hey! Do you want to hear about my campaign?" % (sn)
            s = api.update_status(m, s.id)

twt_replyhealthcare = api.search(q="replies")

#list of specific strings we want to check for in Tweets
t = ['what about free birth control?']

for s in twt_replyhealthcare:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s yes, birth control is free" % (sn)
            s = api.update_status(m, s.id)