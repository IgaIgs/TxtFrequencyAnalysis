from bs4 import BeautifulSoup
import requests

ratings = []


def imdb_search():
    r = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')

    Soup = BeautifulSoup(r.text, 'html.parser')

    for item in Soup.find_all(class_='ratingColumn imdbRating'):
        ratings.append(item.text.strip())
        '''print("IMDb rank & Title", item.text.strip())'''

    for index, item in enumerate(Soup.find_all(class_='titleColumn')):
        print("IMDb Rating", item.text.strip() + "\n")
        print("Ratings: " + ratings[index])


imdb_search()
