# medicare for all tweets (5-10)
tweet_pharma = "The giant pharmaceutical and health insurance lobbies spend billions to ensure that their profits " \
               "come before the health of the American people. We must defeat them by guaranteeing health care to " \
               "all people through a Medicare-for-all, single-payer program. @ me with \"M4A\" and I'll reply!"

pharma_words = ["pharmaceutical", "drug", "lobbyists", "pharma", "big pharma", "companies"]

pharma_reply_example = "What will cut this profit?"
pharma_reply_example_2 = "Would there be optional privatized care for those who could afford it?"
pharma_reply_example_3 = "What other countries in the world have single-payer systems?"

pharma_response = "We need to restrict the more than $100 billion profit that health insurance and pharmaceutical " \
                  "companies take away every year and spend on lobbying congress to appeal to their interests. For " \
                  "every Congressman and woman, this lobbyist force controls 500 lobbyists."

pharma_response_2 = "A single-payer program would ensure that health care become a human right. Each citizen would " \
                      "pay into this program and receive total coverage including dental and visual care. Through a " \
                      "single-payer system, we eliminate administrative costs and financial motives."

pharma_response_3 = "Strengthening antitrust measures against big pharma will decrease their profit. A single-payer " \
                    "system will also provide the government considerable drug market power to negotiate lower prices."

# "Just north of us, every Canadian citizen is guaranteed healthcare and astonishingly, " \
# "Canada spends less per capita on healthcare than the United States. It's a problem that " \
# "diabetic families need to cross to border to get insulin because it is 10x the price here."

pharma_response_4 = "Private insurers will not be able to offer coverage that duplicates benefits covered by " \
                      "Medicare For All. We all have to buy in and trust the process if we want to ensure healthcare " \
                      "as a human right!"

retry_message = "I didn't understand. Restate your tweet and ask me about Medicare For All!"

# Evaluate response strings
# SEARCH FOR KEYWORDS
# subject = ""
# response = tweet.full_text.lower()
#
# for words in pharma_words:
#     if response.__contains__(words):
#         if response.__contains__("influence") or response.__contains__("power"):
#             message = pharma_response
#         elif response.__contains__("single-payer"):
#             message = pharma_response_2
#         elif response.__contains__("fight") or response.__contains__("defeat"):
#             message = pharma_response_3
#         elif response.__contains__("private") or response.__contains__("optional"):
#             message = pharma_response_4
#         else:
#             message = retry_message

tweet_moral = "The disgraceful reality of the U.S healthcare system is that Americans in the richest country in the " \
              "world must consider their financial situation before attempting to speak to a professional about their " \
              "poor health. Many times, cost outweighs the health concerns. Something is fundamentally wrong with " \
              "the statement that \"Americans cannot afford to get sick.\""

tweet_current = "Today, more than 30 million Americans still don’t have health insurance and even more are " \
                "underinsured. Even for those with insurance, costs are so high that medical bills are the " \
                "number one cause of bankruptcy in the United States. Incredibly, we spend significantly more " \
                "of our national GDP on this inadequate health care system—far more per person than any other " \
                "major country. And despite doing so, Americans have worse health outcomes and a higher infant " \
                "mortality rate than countries that spend much less on health care. Our people deserve better."

tweet_cost = "Over the next ten years, national health expenditures are projected to total approximately $52 trillion " \
             "if we keep our current dysfunctional system. Numerous studies have shown that implementing Medicare For " \
             "All will save $5 trillion during that same time period. The Medicare For all bill proposes a plethora of " \
             "financing options that would exceed the cost of implementation. Ask me how we would pay for it!"

tweet_covid = "This global pandemic has exposed the weaknesses in the United States healthcare system. The biggest " \
              "problem face so far has to do with costs. Cost-related barriers to receiving medical care more " \
              "prevalent in the U.S than any other country delay care when it is urgently needed. On top of this, " \
              "capacity shortages put the U.S at a further disadvantage when dealing with this pandemic. "

moral_1_response_example = "What would you say to those who consider healthcare to be a commodity or luxury?"
moral_1_response_example_2 = "How do we ensure healthcare becomes a right?"
moral_1_response_example_3 = "Wont healthcare for everyone lower the quality?"

moral_2_response = "I understand that the highest quality of care simply cannot be provided to every citizen, but is " \
                   "great care for the rich minority that can afford it worth minimal care for majority that cannot?"
moral_2_response_2 = "We ensure healthcare as a human right by effectively ending the private health insurance market."
moral_2_response_3 = "By sacrificing some quality, we can maximize universality and cost effectiveness while also " \
                     "decreasing the complexity of the system. The benefits of Medicare for all far outweigh the costs."

moral_3_response_example = "Should the wealthy be able to access the highest quality healthcare if they can afford it?"
moral_3_response_example_2 = "What are the effects of ending private health insurance?"

moral_4_response = ""

#
# # responding to users
# toReply = "someonesTwitterName" #user to get most recent tweet
# # api = tweepy.API(auth)
#
# #get the most recent tweet from the user
# tweets = api.user_timeline(screen_name = toReply, count=1)
#
# for tweet in tweets:
#     api.update_status("@" + toReply + " This is what I'm replying with", in_reply_to_status_id = tweet.id)


