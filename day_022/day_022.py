import requests
from bs4 import BeautifulSoup
import json

# Question 1: Scrape the following website and store the data as json file
# (url = 'http://www.bu.edu/president/boston-university-facts-stats/').

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
#print(response) #200, their is connection

soup = BeautifulSoup(response.text, 'lxml')
with open('day_022\\bu_facts.json', 'w') as file:
    
    tables = soup.find_all('div', class_='facts-wrapper')
    
    for table in tables:
        result = []
        title = table.h5.text
        row_list = table.find_all('li', class_='list-item')
        store = {}
        var = []
        for row in row_list:
            store['caption'] = row.find('p', class_='text').text
            store['figure'] = row.find('span', class_='value').text
            var.append({store['caption']:store['figure'] })
        json.dump({title:var}, file, indent=4)
            
    print('Question 1, done')
    print()
    
# Question 2: Extract the table in this url 
# (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

url = 'https://archive.ics.uci.edu/datasets'
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text, 'lxml')
with open('day_022\\dataset.json', 'w') as file:
    
    tables = soup.find_all('div', class_= 'rounded-box bg-base-100')
    result = []
    for table in tables:
        dataset_name = table.find('a', class_='link-hover link text-xl font-semibold').text
        database_des = table.find('p', class_='truncate').text.replace('\n', '')
        data_info = table.find_all('span', class_='truncate')
        store = []
        for info in data_info:
            store.append(info.text)
        
        dic = {
            'Dataset name': dataset_name,
            'Dataset Description' : database_des,
            'Problem type': store[0],
            'Data Type': store[1],
            'Number of Sample': store[2],
            'Number of Feature': store[3],    
        }
        result.append(dic)
    json.dump(result, file, indent=4)
    print('Question 2, done')
    print()
    
# Question 3: Scrape the presidents table and store the data as 
# json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
# The table is not very structured and the scrapping may take very long time

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
import re
soup = BeautifulSoup(response.content, "lxml")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")
result = []
for row in rows[1:]:
    store = {}
    cells = row.find_all("td")
    name = re.sub(r'[\n]', ' ', cells[1].text).replace('\u2013', ' -- ')
    term = re.sub(r'[\n]', ' ',cells[2].text).replace('\u2013', ' -- ')
    store = {'name':name, 'Tenure':term}
    result.append(store)
   
# Store the data as a JSON file
with open("day_022\\List of presidents.json", "w") as file:
   json.dump(result, file, indent=4)
   print("Question 3, done")