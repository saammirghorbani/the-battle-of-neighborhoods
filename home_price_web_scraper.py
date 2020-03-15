import pandas as pd
import requests
#!conda install -c conda-forge beautifulsoup4 --yes
from bs4 import BeautifulSoup

data = []
for pages in range(0, 42):
    try:
        if(pages == 0):
            URL = 'http://house.speakingsame.com/suburbtop.php?sta=nsw&cat=HomePrice&name'
        else:
            URL = 'http://house.speakingsame.com/suburbtop.php?sta=nsw&cat=HomePrice&name=&page=' + str(pages)
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find_all('table')[6].find_all('tr')[2].find('td').find('table')
        new_table = pd.DataFrame(columns=range(0,3), index = [0])


        # skip header
        rows = table.find_all('tr')[1:]
        for row in rows:
          cols = row.find_all('td')
          row = [row.text for row in cols]
          data.append(row)
    except:
        print('Error on page '+str(pages)+': webpage has probably changed, change BeautifulSoup expression accordingly!')
        break

df = pd.DataFrame(data, columns=['rank', 'suburb', 'median_value_aud'])
df.to_csv('sydney_houses_median_value.csv',index=False)