import requests
from bs4 import BeautifulSoup

imdburl="https://www.imdb.com/chart/top"

r=requests.get(imdburl)
soup = BeautifulSoup(r.content,"html.parser")

data=soup.find_all("table",{"class":"chart full-width"})

movietable= (data[0].contents) [len(data[0].contents)-2]

movietable=movietable.find_all("tr")

for movie in movietable:
    movietitle = movie.find_all("td",{"class":"titleColumn"})
    rating=movie.find_all("td",{"class":"ratingColumn imdbRating"})
    moviename=movietitle[0].text
    ratings=rating[0].text.replace("\n","-")
    moviename=moviename.replace("\n","")
    print(moviename,ratings)

