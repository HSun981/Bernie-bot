'''
This is a keyword bank that groups words with similar meanings into the same set.
'''

# Jared's keyword category, prioritized
medicare_for_all = {'medicare for all'}

covid_19 = {'COVID-19', 'COVID', 'coronavirus', 'corona virus', 'corona'}

medicine = {'medicine', 'health', 'hospital', 'patient', 'health care', 'medical', 'doctor'}

politics = {'politic', 'democratic', 'republic'}

education = {'education', 'school', 'university'}

united_states = {'US', 'America', 'USA'}

# When adding a new category, add the category to this list
# Keyword will be checked in order so beware of the order
catalog = [medicare_for_all, covid_19, medicine, politics, education, united_states]
