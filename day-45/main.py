from bs4 import BeautifulSoup
import requests
import math

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

response.raise_for_status()

soup = BeautifulSoup(response.text,'html.parser')

movies_titles = [item.get_text() for item in soup.select('div.gallery section > div.article-title-description h3')]

movies_titles.reverse()

str_titles = ''

for movie in movies_titles:
    str_titles += movie + '\n'

with open('day-45/movies.txt','w') as file:
    file.write(str_titles)