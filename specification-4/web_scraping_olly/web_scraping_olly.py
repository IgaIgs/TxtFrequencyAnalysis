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

def display():
    print()

def menu(choice):

    switcher = {
        1: scores(),
        2: matchwins()

    }
    return switcher.get(choice, "nothing")

def matchwins():
    print('yes')

def scores():
    count = 0
    team1_ar, team1_score_ar, team2_score_ar = [47]
    while count < 48:
        for i in range(47):
            team1_ar[i] = str.format(all_results[1].text.split(' ')[0])
            team1_score_ar[i] = str.format(((all_results[1].text.split(' ')[1])[:6]).strip('Win'))
            team2_score_ar[i] = str.format((all_results[0].text.split(' ')[2]).strip('Win'))
    display()

all_results = soup.findAll('a', class_="fixtures__match-link--score")
quitter = 0
while quitter < 1:
    print('1. Get Rugby Results')
    print('2. How many matches did a team win.')
    print('3. Who won the world cup?')
    print('4. Quit')
    choice = input('Please enter the number of the option of your choosing:')
    if choice == 4:
        quitter = 1
    else:
        menu(choice)
