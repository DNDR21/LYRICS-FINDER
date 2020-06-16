import requests
from bs4 import BeautifulSoup as bs

class Search():
    def __init__(self,name):
        self.name=name

    def search_lyrics(self):
        word=""
        name=self.name
        for i in range(len(self.name)):
            if i==0:
                word=name[0].upper()
            elif name[i]==" ":
                word+="-"
            else:
                word+=name[i].lower()
                
        link="https://search.azlyrics.com/search.php?q="+word+"&w=songs&p=1"
        r=requests.get(link)
        soup=bs(r.content,"html.parser")
        self.search=soup.find("div",{"class":"container main-page"})
        self.search=self.search.find_all("a")
        self.name=self.search

    def open_lyrics(self):
        word=""
        name=self.name
        for i in range(len(self.name)):
            if i==0:
                word=name[0].upper()
            elif name[i]==" ":
                word+="-"
            else:
                word+=name[i].lower()

        r=requests.get("https://genius.com/"+word+"-lyrics")
        soup=bs(r.content,"html.parser")
        self.open=soup.find("div",{"class":"lyrics"})
        self.open=self.open.get_text()
        self.name=self.open
        



    
