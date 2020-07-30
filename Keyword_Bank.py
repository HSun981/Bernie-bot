'''
This is a keyword bank that groups words with similar meanings into the same set.
All words should be recognizable in all Lowercase
Should not cause confusion when the keyword is part of another word,
like "butter" in "butterfly"
'''

# Jared's keyword category, prioritized
medicare_for_all = {'medicare for all', 'M4A', 'health care'}

# For the demonstration in presentation
sybbure = {'sybbure'}

covid_19 = {'covid-19', 'covid', 'corona', 'coronavirus', 'pandemic', 'coronavirus disease', 'SARS-CoV-2'}

medicine = {'medicine', 'health', 'hospital', 'patient', 'health care', 'medical', 'doctor', 'medicare', 'medical debt', 'health', 'insurance', 'affordable care act'}

politics = {'political', 'democratic', 'republic', 'politics', 'political climate'}

education = {'education', 'school', 'university', 'college', 'tuition', 'tuition-free', 'student debt', 'public schools', 'degree', 'low income students', 'profession'}

year_2020 = {'this year', '2020'}

united_states = {'the us', 'america', 'usa', 'united states of america', 'united states'}

taxes = {'greed', 'revenue', 'income', 'wealth', 'tax brackets', 'tax cuts', 'big corporation'}

climate = {'cap-and-trade', 'carbon', 'emissions', 'energy', 'green new deal', 'fossil fuels', 'renewable', 'oil', 'gas', 'coal', 'climate change'}

campaign = {'campaign', 'election', 'presidential race'}



# When adding a new category, add the category to this list
# Keyword will be checked in order so beware of the order
catalog = [medicare_for_all, sybbure, covid_19, medicine, politics, education, year_2020,
           united_states, taxes, climate, campaign]
