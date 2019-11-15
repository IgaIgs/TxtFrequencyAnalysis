from bs4 import BeautifulSoup
import requests
import re

# making sure the website will let us access it.
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# using World Rugby as the website to scrape
url = "https://www.rugbyworldcup.com/matches"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'lxml')

# scores = soup.find('div', class_='fixtures__team fixtures__team--a fixtures__team--winner')

def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list

all_results = soup.findAll('a', class_="fixtures__match-link--score")

print(all_results[0].text.split(' '))
print(all_results[1].text.split(' '))

# gives the name of the first team
team1 = str.format(all_results[1].text.split(' ')[0])

# gives the name of the second team


# gives the score of the first team
team1_score = str.format(((all_results[1].text.split(' ')[1])[:6]).strip('Win'))

# gives the score of the second team
team2_score = str.format((all_results[0].text.split(' ')[2]).strip('Win'))


