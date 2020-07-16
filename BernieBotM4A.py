# TO CODE
#key
# 1 = user response to original tweet, 2 = bot response to users response, 3 = user response to bot, 4 = bot response

# medicare for all tweets (5-10)
tweet_pharma = "The giant pharmaceutical and health insurance lobbies have spent billions of dollars over the past decades " \
                "to ensure that their profits come before the health of the American people. We must defeat them, together. That means: " \
                "Joining every other major country on Earth and guaranteeing health care to all people as a right, not a privilege, " \
                "through a Medicare-for-all, single-payer program."

tweet_human_right = "The disgraceful reality of the U.S healthcare system is that Americans in the richest country in the " \
                    "world must consider their financial situation before attempting to speak to a professional about their " \
                    "poor health. Many times, cost outweighs the health concerns. Something is fundamentally wrong with " \
                    "the statement that \"Americans cannot afford to get sick.\" Health care must be deemed a human right!"

human_1_response_example = "What would you say to those who consider healthcare to be a commodity or luxury?"
human_1_response_example_2 = "How do we ensure healthcare becomes a right?"
human_1_response_example_3 = "Wont healthcare for everyone lower the quality?"

human_2_response = "I understand that the highest quality of care simply cannot be provided to every citizen, but is " \
                   "great care for the rich minority that can afford it worth minimal care for majority that cannot?"
human_2_response_2 = "We ensure healthcare as a human right by effectively ending the private health insurance market."
human_2_response_3 = "By sacrificing some quality, we can maximize universality and cost effectiveness while also " \
                     "decreasing the complexity of the system. The benefits of Medicare for all far outweigh the costs."

human_3_response_example = "Should the wealthy be able to access the highest quality healthcare if they can afford it?"
human_3_response_example_2 = "What are the effects of ending private health insurance?"

human_4_response = ""

pharma_1_response_example = "How do we defeat the giant pharmaceutical companies?"
pharma_1_response_example_2 = "What can we do to defeat them?"
pharma_1_response_example_3 = "How much influence do they have?"
pharma_1_response_example_4 = "What are the effects of having a single-payer program?"

pharma_2_response = "We need to cut the $100 billion profit that health insurance companies take away every year and spend " \
               "on lobbying congress to appeal to their interests."
pharma_2_response_2 = "The leading lobbyist force in Washington is Health care industry. Both hospitals and the pharmaceutical " \
                 "industry both contribute to this lobbying force."


pharma_3_response_example = "What legislation will cut this profit?"

pharma_4_example = "The Medicare Drug Price Negotiation Act, the Affordable and Safe Prescription " \
                   "Drug importation Act, and the Prescription Drug Price Relief Act are three examples " \
                   "of legislation that I am working on to lower the prices of prescription drugs." \



# Evaluate response strings
# SEARCH FOR KEYWORDS
# determine subject of responses
def bot_response(user_response_1):
    user_response_1.lower()
    if user_response_1.__contains__("defeat"):
        return pharma_2_response
    if user_response_1.__contains__("influence"):
        return pharma_2_response_2

# create responses to responses (n=4)

def bot_response_2(user_response_3):
    user_response_3.lower()
    if user_response_3.__contains__("legislation"):
        return pharma_4_example


print(bot_response(pharma_1_response_example_2))
print(bot_response_2(pharma_3_response_example))
# loops to how many levels?
