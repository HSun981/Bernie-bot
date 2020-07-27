'''
This is a keyword bank that groups words with similar meanings into the same set.
All words should be recognizable in all Lowercase
Should not cause confusion when the keyword is part of another word,
like "butter" in "butterfly"
'''

# Jared's keyword category, prioritized
medicare_for_all = {'medicare for all', 'M4A'}

# For the demonstration in presentation
sybbure = {'sybbure'}

covid_19 = {'covid-19', 'covid', 'corona'}

medicine = {'medicine', 'health', 'hospital', 'patient', 'health care', 'medical', 'doctor'}

politics = {'politic', 'democratic', 'republic'}

education = {'education', 'school', 'university', 'college'}

year_2020 = {'this year', '2020'}

united_states = {'the us', 'america', 'usa'}



# When adding a new category, add the category to this list
# Keyword will be checked in order so beware of the order
catalog = [medicare_for_all, sybbure, covid_19, medicine, politics, education, year_2020,
           united_states]
