import pandas as pd

# Note . Download directly from website instead

""" GDP data"""
# source : https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD

df = pd.read_csv('PPPGDP.csv')
# filter GDP data. 
# For country ISO code and latest GDP
filtered_gdp = pd.read_csv('PPPGDP.csv', 
                    usecols=[
                    'Country Name',
                    'Country Code',
                    '2020 [YR2020]'
                    ])

# Turn missing 2020 values ('..') into NaN
filtered_gdp = filtered_gdp[filtered_gdp != '..']

# remove previous, including the ones that was default NaN
new_gdp = filtered_gdp.dropna(how='any')

#### print(filtered_gdp.to_string())

"""Vaccination Data"""



# Filter Vaccination data
# for ISO code and fully_vacinated
filtered_vaccin = pd.read_csv('vaccinations.csv', 
                    usecols= [
                    'date',
                    'iso_code',
                    'people_fully_vaccinated_per_hundred'
                    ])

# Sort by latest date and remove dublicates
sorted_filtered_vaccin = filtered_vaccin.sort_values(by='date')
sorted_filtered_vaccin = sorted_filtered_vaccin.drop_duplicates('iso_code',keep='last')

# remove rows missing vaccination data
new_vaccin = sorted_filtered_vaccin.dropna(how='any')


""" Merge data to one dataframe"""

dataset = new_gdp.merge(new_vaccin, 
                how='inner',
                left_on='Country Code',
                right_on='iso_code')


"""Save as new CSV file"""
dataset.to_csv('dataset.csv', encoding='utf-8', index=False)
