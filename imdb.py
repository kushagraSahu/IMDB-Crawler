import requests
from bs4 import BeautifulSoup

j = 1
home_url = 'http://www.imdb.com'
print("Enter minimum rating")
minm = input()
print("Enter maximum rating")
maxm = input()
print("Enter total no. of movies you want search for ")
num_movies = input()
i = 0
while i < int(num_movies):
    # print('Page: ' + str(j))
    url = home_url + '/list/ls057823854/?start=' + str(j)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content,'lxml')
    g_data = soup.find_all('div',{'class':'info'})

    for item in g_data:
        rating = item.find('span',{'class':'rating-rating'}).find('span',{'class':'value'}).text
        if float(rating) > float(minm) and float(rating) < float(maxm):
            i = i + 1
            if i > int(num_movies):
                break

            print(str(i)+'.' + item.find('b').find('a').text)
            print('Rating: ' + rating)
            print('Director: ' + item.find('div',{'class':'secondary'}).text)
            print('IMDB page: ' + home_url + item.find('b').find('a')['href'])
            print('')

    j = j + 100


    
