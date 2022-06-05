
import requests
from bs4 import BeautifulSoup
import pandas as pd


res = requests.get('https://en.wikipedia.org/wiki/nfl')
src = res.content
html = BeautifulSoup(src, 'lxml')
results = html.findAll(f'table')
tables = pd.read_html(str(results), encoding=f'{res.encoding}')
count = 0
for table in tables: # loop through the tables list write it to a file
        with open(f'file_{count}.xlsx', 'w') as file:
            file.write(str(table))
        count += 1
        