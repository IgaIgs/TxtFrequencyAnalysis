from bs4 import BeautifulSoup
import requests

# making sure the website will let us access it.
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# using BBC Sport as the website to scrape
url = "https://www.rugbyworldcup.com/matches"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'lxml')

#scores = soup.find('div', class_='fixtures__team fixtures__team--a fixtures__team--winner')

match_dates = []
counter = 0

all_results = soup.findAll('a', class_="fixtures__match-link--score")
print(all_results)
