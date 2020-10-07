"""
Ogrenmek icin yazilmis bir kodtur.
Imdb sitesine gidip oradan filmlerin isimlerini var ratinglerini cektim.
Daha sonra bunlari dosya icerisine yazdirdim.

"""

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content,"html.parser")

names = soup.find_all("td", {"class":"titleColumn"})
ratings = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for name,rating in zip(names,ratings):

    cname = name.text.replace("\n","")
    cname = cname.strip()

    crating = rating.text.replace("\n","")
    crating=crating.strip()
    birlesik = cname+"     Rating:"+crating+"\n"

    dosya = open("top250.txt","a")
    dosya.write(birlesik)
    dosya.close()
