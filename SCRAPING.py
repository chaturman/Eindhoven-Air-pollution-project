'''
scrape data
save as API

'''

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import cbsodata
import csv
import json
import os


filepath = os.chdir(r'C:\Users\Dell\Desktop\YEAR1\QUARTILE 2\AAEOGD\ASSIGNMENT\SCRIPT\PYTHON')

data=[]
for x in range(1,36):
    url = 'http://data.aireas.com/api/v2/airboxes/history/'+str(x)+'/1420070400/1420156740'
    response = requests.request('GET', url)
    jsonObj2 = json.loads(response.text)
    data.append(jsonObj2)

with open('new.json', 'w') as jsonfile:
    json.dump(jsonObj2, jsonfile)




























