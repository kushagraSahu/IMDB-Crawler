import requests
import sys
from bs4 import BeautifulSoup

url = 'http://www.imdb.com'
response = requests.get(url)
visited = {}
soup = BeautifulSoup(response.text,'lxml')

m_data = soup.find_all('div',{'class':'title'})

def extract_data(url2):
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text,'lxml')
        try:
            rating = soup2.find('div',{'class':'ratingValue'}).find('span',{'itemprop':'ratingValue'}).text
            if float(rating) > float(5.0) and float(rating) < float(10.0):
                title = soup2.find('div',{'class':'titleBar'}).find('div',{'class':'title_wrapper'}).find('h1',{'itemprop': 'name'}).text
                print(title)
                print('Rating: ',rating)
                director_name = soup2.find('span',{'itemprop':'director'}).find('span',{'itemprop':'name'}).text
                print('Director: ',director_name)
                print('')
        except:
            pass

        foo = soup2.findAll('div',{'class' : 'rec_overview'})
        for i in foo:
            new_key =  i.get('data-tconst')
            if new_key in visited:
                continue
            else:
                visited[new_key] = 1

            new_url = i.find('div',{'class':'rec-title'}).find('a').get('href')
            #print(i.find('div',{'class':'rec-title'}).text)
            extract_data(url + new_url)

for item in m_data:
    link = item.find('a').get('href')
    extract_data(url + link)
    break





