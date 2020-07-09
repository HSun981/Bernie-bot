# TO CODE
# make medicare for all tweets (5-10)
tweet_pharma = "The giant pharmaceutical and health insurance lobbies have spent billions of dollars over the past decades " \
"to ensure that their profits come before the health of the American people. We must defeat them, together. That means: " \
"Joining every other major country on Earth and guaranteeing health care to all people as a right, not a privilege, " \
"through a Medicare-for-all, single-payer program."

user_response_example = "How do we defeat the giant pharmaceutical companies?"
user_response_example_2 = "What can we do to defeat them?"
user_response_example_3 = "How much influence do they have?"
user_response_example_4 = "What are the effects of having a single-payer program?"

bot_response = "We need to cut the $100 billion profit that health insurance companies take away every year and spend " \
               "on lobbying congress to appeal to their interests."
bot_response_2 = "The leading lobbyist force in Washington is Health care industry. Both hospitals and the pharmaceutical " \
                 "industry both contribute to this lobbying force."


user_response_level_2_example = "What legislation will cut this profit?"

bot_response_level_2_example = "The Medicare Drug Price Negotiation Act, the Affordable and Safe Prescription " \
                               "Drug importation Act, and the Prescription Drug Price Relief Act are three examples " \
                               "of legislation that I am working on to lower the prices of prescription drugs." \


# Evaluate response strings
# SEARCH FOR KEYWORDS
# determine subject of responses
def response_1(user_response):
    user_response.lower()
    if user_response.__contains__("defeat"):
        return bot_response
    if user_response.__contains__("influence"):
        return bot_response_2

# create responses to responses (n=4)

def response_2(user_response_2):
    user_response_2.lower()
    if user_response_2.__contains__("legislation"):
        return bot_response_level_2_example




print(response_1(user_response_example_2))
print(response_2(user_response_level_2_example))
# loops to how many levels?
