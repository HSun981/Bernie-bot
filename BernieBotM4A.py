# key
# 1 = user response to original tweet, 2 = bot response to users response, 3 = user response to bot, 4 = bot response

# medicare for all tweets (5-10)
tweet_pharma = "The giant pharmaceutical and health insurance lobbies have spent billions of dollars over the past " \
               "decades to ensure that their profits come before the health of the American people. We must defeat " \
               "them, together. That means: Joining every other major country on Earth and guaranteeing health care " \
               "to all people as a right, not a privilege, through a Medicare-for-all, single-payer program."

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


# pharmaceutical and insurance companies (pharma)

pharma_1_response_example = "How do we defeat the giant pharmaceutical companies?"
pharma_1_response_example_2 = "What can we do to defeat them?"
pharma_1_response_example_3 = "What are the effects of having a single-payer program?"

pharma_2_response = "We need to restrict the more than $100 billion profit that health insurance and pharmaceutical " \
                    "companies take away every year and spend on lobbying congress to appeal to their interests. Both " \
                    "hospitals and the pharmaceutical industry contribute to the leading lobbyist force in Washington."
pharma_2_response_2 = "A single-payer program would ensure that health care become a human right. Each citizen would " \
                      "pay into this national health insurance program and receive total coverage including dental and " \
                      "visual care. Through a single-payer system, we eliminate administrative costs and financial " \
                      "motives. This would also provide the government considerable drug market power to negotiate" \
                      "lower prices."


pharma_3_response_example = "What legislation will cut this profit?"
pharma_3_response_example_2 = "Are there any drawbacks to a single-payer system?"
pharma_3_response_example_3 = "What countries in the world have single-payer systems?"
pharma_3_response_example_4 = "Would there be optional privatized care for those who could afford it?"

pharma_4_example = "The Medicare Drug Price Negotiation Act, the Affordable and Safe Prescription " \
                   "Drug importation Act, and the Prescription Drug Price Relief Act are three examples " \
                   "of legislation that I am working on to lower the prices of prescription drugs." \

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


# Evaluate response strings
# SEARCH FOR KEYWORDS
def bot_2_response_pharma(user_response):
    user_response.lower()
    if user_response.__contains__("pharmaceutical"):
        return pharma_2_response
    if user_response.__contains__("defeat"):
        return pharma_2_response
    if user_response.__contains__("single-payer"):
        return pharma_2_response_2
    if user_response.__contains__("program"):
        return pharma_2_response_2

# create responses to responses (n=4)

def bot_4_response_pharma(user_response):
    user_response.lower()
    if user_response.__contains__("legislation"):
        return pharma_4_example


# loops to how many levels?
