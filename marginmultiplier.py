#Scrap the list of stock names,multipliers from zerodha .com/margin-calculator/Equity/
import urllib2
import requests
from bs4 import BeautifulSoup
import pandas as pd

quote_page = 'https://zerodha.com/margin-calculator/Equity/'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
page = requests.get(quote_page, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
#name_box1 = soup.find('table', attrs={'class': 'data equity'})
name_box = soup.find('tbody')
name = name_box.text.strip()
table = name_box
new_table = pd.DataFrame(columns=range(1,4), index = [0]) # I know the size
row_marker = 0
file = open('margin.txt', 'w')
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for i in range(1,4):
        new_table.iat[row_marker,column_marker] = columns[i].get_text().strip()
        file.write(columns[i].get_text().strip()+" ")
        column_marker += 1
    file.write("\n")
    print new_table.head()
file.close()

