'''
This is a keyword bank that groups words with similar meanings into the same set.
All words should be recognizable in all Lowercase
Should not cause confusion when the keyword is part of another word,
like "butter" in "butterfly"
Should not be repetitive (e.g. if we already have 'covid', there is no need for 'covid-19' as it
is already captured by a previous key word)
'''

# Jared's keyword category, prioritized
medicare_for_all = {'medicare for all', 'M4A', 'health care'}

# For the demonstration in presentation
sybbure = {'sybbure'}

covid_19 = {'covid', 'corona', 'pandemic', 'SARS-CoV-2'}

medicine = {'medicine', 'health', 'hospital', 'patient', 'medical', 'doctor', 'medicare', 'insurance', 'affordable care act'}

politics = {'politic', 'democratic', 'republic'}

education = {'education', 'school', 'university', 'college', 'tuition', 'student debt', 'degree', 'low income students', 'profession'}

year_2020 = {'this year', '2020'}

united_states = {'the us', 'america', 'usa', 'united states'}

taxes = {'greed', 'revenue', 'income', 'wealth', 'tax brackets', 'tax cuts', 'big corporation'}

climate = {'cap-and-trade', 'carbon', 'emissions', 'energy', 'green new deal', 'fossil fuels', 'renewable', 'oil', 'gas', 'coal', 'climate change'}

campaign = {'campaign', 'election', 'presidential race'}



# When adding a new category, add the category to this list
# Keyword will be checked in order so beware of the order
catalog = [medicare_for_all, sybbure, covid_19, medicine, politics, education, year_2020,
           united_states, taxes, climate, campaign]
