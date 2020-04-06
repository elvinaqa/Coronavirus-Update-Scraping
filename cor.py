import pandas as pd
import numpy as np
import dateutil
import time
import copy
import requests
from datetime import datetime, timedelta, date

countries_fixes_dict = {'CAR': 'Central African Republic',
                        'Congo': 'Congo (Brazzaville)',
                        'DRC': 'Congo (Kinshasa)',
                        'Diamond Princess': 'Cruise Ship',
                        'Ivory Coast': 'Cote d\'Ivoire',
                        'S. Korea': 'Korea, South',
                        'St. Vincent Grenadines': 'Saint Vincent and the Grenadines',
                        'Taiwan': 'Taiwan*',
                        'UAE': 'United Arab Emirates',
                        'UK': 'United Kingdom',
                        'USA': 'US',
                        'Vatican City': 'Holy See',
                        'Aruba': 'Netherlands',
                        'Bermuda': 'United Kingdom',
                        'Cayman Islands': 'United Kingdom',
                        'Channel Islands': 'United Kingdom',
                        'Curaçao': 'Netherlands',
                        'Faeroe Islands': 'Denmark',
                        'French Polynesia': 'France',
                        'French Guiana': 'France',
                        'Gibraltar': 'United Kingdom',
                        'Greenland': 'Denmark',
                        'Guadeloupe': 'France',
                        'Guam': 'US',
                        'Hong Kong': 'China',
                        'Isle of Man': 'United Kingdom',
                        'Macao': 'China',
                        'Martinique': 'France',
                        'Mayotte': 'France',
                        'Montserrat': 'United Kingdom',
                        'New Caledonia': 'France',
                        'Puerto Rico': 'US',
                        'Réunion': 'France',
                        'Saint Martin': 'France',
                        'Sint Maarten': 'Netherlands',
                        'St. Barth': 'France',
                        'Turks and Caicos': 'United Kingdom',
                        'U.S. Virgin Islands': 'US',
                        'Bahamas': 'Bahamas, The',
                        'Gambia': 'Gambia, The'
                        }

url = 'https://www.worldometers.info/coronavirus/'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

worldometer_stats_today_orig_DF = pd.read_html(r.text, header=[0], index_col=0)[0].iloc[:-1]
worldometer_stats_yesterday_orig_DF = pd.read_html(r.text, header=[0], index_col=0)[1].iloc[:-1]

now = datetime.now()
yesterday = date.today() - timedelta(days=1)

date_time_trailer = now.strftime("%Y_%m_%d")

date_time_columnname = yesterday.strftime("%m/%d/%Y")
#date_time_columnname = yesterday.strftime("%m/%d/%Y")



worldometer_stats_today_orig_DF.index.names = ['Country/Region']
worldometer_stats_yesterday_orig_DF.index.names = ['Country/Region']

worldometer_recovered_orig_DF = worldometer_stats_today_orig_DF['TotalRecovered'].copy().to_frame()
worldometer_recovered_orig_DF['TotalRecovered'] = worldometer_recovered_orig_DF['TotalRecovered'].fillna(0).astype(np.int64)
worldometer_recovered_orig_DF = worldometer_recovered_orig_DF.rename(columns={'TotalRecovered': date_time_columnname})
worldometer_recovered_orig_DF = worldometer_recovered_orig_DF.rename(index = countries_fixes_dict)
worldometer_recovered_DF = worldometer_recovered_orig_DF.groupby(['Country/Region']).sum()
worldometer_recovered_DF.to_csv(r'./worldometer_recovered_' + date_time_trailer + '.csv', index = True)
print(worldometer_recovered_DF.head())
