import requests
from bs4 import BeautifulSoup


url="http://www.imdb.com/chart/top"
responce=requests.get(url)
#print(responce)
html_icerigi=responce.content
soup=BeautifulSoup(html_icerigi,"html.parser")


#for i in soup.findAll("td",{"class":"titleColumn"}):
 #   print(i.text)
  #  print("*****************************")
basliklar=soup.findAll("td",{"class":"titleColumn"})
ratingler=soup.findAll("td",{"class":"ratingColumn imdbRatingColumn"})
#print(len(basliklar),len(ratingler))
for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text
    rating=rating.text
    baslik=baslik.strip()
    baslik=baslik.replace("\n","")
    print("Başlık",baslik.next)
    rating=rating.strip()
    rating=rating.replace("\n","")
    print("Rating",rating.next)
    a=float(input("Rating'i Giriniz:"))
    if (float(rating>a)):
        print("Film İsmi: {] Filmin Ratingi: {}".format(baslik,rating))
