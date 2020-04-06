from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook
import re
website_url = requests.get('https://www.worldometers.info/coronavirus/').text

# soup = BeautifulSoup(website_url, 'lxml')
# # print(soup.prettify())
#
# table = soup.find('table', {'id':'main_table_countries_today'})
# # print(table)
# links = table.findAll('a')
# # print(links[0].text)
#
# countries = []
# for link in links:
#     countries.append(link.text)
# # print(countries)
#
# df = pd.DataFrame()
# df['Country'] = countries
#
# # print(df.head())
#
# da = table.findAll('tr')
# # for tr in da:
# #     for td in tr:
# #         print(td)

country = []
total_cases = []
new_cases = []
total_deaths = []
new_deaths = []
total_recovered = []
active_cases = []
serious_critical = []
total_cases_million = []
deaths_million = []
total_tests = []
total_tests_million = []
data = pd.DataFrame()

bs = BeautifulSoup(website_url, 'lxml')
table_body=bs.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    country.append(cols[0])
    total_cases.append(cols[1])
    new_cases.append(cols[2])
    total_deaths.append(cols[3])
    new_deaths.append(cols[4])
    total_recovered.append(cols[5])
    active_cases.append(cols[6])
    serious_critical.append(cols[7])
    total_cases_million.append(cols[8])
    deaths_million.append(cols[9])
    total_tests.append(cols[10])
    total_tests_million.append(cols[11])

# print(country)
# print(total_cases_million)
data['country'] = country
data['total_cases'] = total_cases
data['new_cases'] = new_cases
data['total_deaths'] = total_deaths
data['new_deaths'] = new_deaths
data['total_recovered'] = total_recovered
data['active_cases'] = active_cases
data['serious_critical'] = serious_critical
data['total_cases_million'] = total_cases_million
data['deaths_million'] = deaths_million
data['total_tests'] = total_tests
data['total_tests_million'] = total_tests_million

data['new_cases'] = data['new_cases'].astype(str)
# data['new_cases'] = data['new_cases'].replace('+', '', regex=True)

data['new_cases'] = data['new_cases'].str.replace(r'\D', '')
data['new_deaths'] = data['new_deaths'].str.replace(r'\D', '')

print(data.head())
data.to_excel("corono_data_my_own.xlsx")
# data.to_excel(r'Path where you want to store the exported excel file\File Name.xlsx', sheet_name='Your sheet name', index = False)
data_main = pd.DataFrame()
data_main = data
