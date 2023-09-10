from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)
star_data =[]
temp=[]
soup = BeautifulSoup(browser.page_source, "html.parser")
star_table = soup.find_all('table')

rows = star_table[7].find_all('tr')
for tr in rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp.append(row)

Names = []
Distance = []
Mass = []
Radius =[]

for i in range(1,len(list(temp))):
    Names.append(list(temp[i][0]))
    Distance.append(list(temp[i][5]))
    Mass.append(list(temp[i][7]))
    Radius.append(list(temp[i][8]))
print("hello")
df = pd.DataFrame(list(zip(Names,Distance,Mass,Radius)),columns=['id','Names','Distance','Mass','Radius'])
print(df)
df.to_csv('dwarfstars.csv')