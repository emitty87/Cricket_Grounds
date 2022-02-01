import requests
import bs4
import pandas as pd

url = 'https://www.crickety.com/features/world-cricket-grounds.html'
result = requests.get(url)
doc = bs4.BeautifulSoup(result.text, 'lxml')

grounds = doc.find_all('td', colspan='4')

print(grounds)

data = []

for i in grounds:
    td = i.find()
    data.append(i.text)

print(data)

df = pd.DataFrame({"Countries": data})


df.to_csv('Cricket_Grounds1.csv')
