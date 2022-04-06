import requests
from bs4 import BeautifulSoup

from firebase import firebase

headers = {'User-Agent':'Mozilla/5.0'}
all_news_data={}

with requests.Session() as session:
    session.headers = headers
    soup = BeautifulSoup(session.get("https://phys.org/earth-news/").text,"lxml")
    news_list=[]

    for news_div in soup.select(".news-link"):
        news_list.append(news_div.get("href"))

    i = 1
        
    for url in news_list[:5]:
        soup = BeautifulSoup(session.get(url).text,"lxml")
        mydivs = soup.findAll("div",{"class":"mt-4 article-main"})
        
        all_news_data[i] = [url,
                            soup.select_one(".article-img").select_one("img").get("src"),
                            soup.select_one(".article-img").select_one("img").get("alt"),
                            soup.select_one(".article-img").select_one("img").get("title").split("Credit")[0].strip(),
                            (mydivs[0].text).strip().split("\n")[3]]


        i+=1

config = {
    "apiKey":"AIzaSyCxTxf845NCsg3JU9StdlSYC_Rzo-HjCVc",
    "authDomain":"inshorts-290a0.firebaseapp.com",
    "databaseURL":"https://inshorts-290a0.firebaseio.com",
    "storageBucket":"inshorts-290a0.appspot.com"
    }

#create firebase database connection
firebaseconn = firebase.FirebaseApplication(config["databaseURL"],None)

for i in all_news_data:
    data = {"newslink":all_news_data[i][0],
            "imagelink":all_news_data[i][1],
            "head":all_news_data[i][2],
            "title":all_news_data[i][3],
            "desc":all_news_data[i][4]}

    result = firebaseconn.patch("/News/%s"%i,data)
    print(result)














