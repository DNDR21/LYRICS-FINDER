import requests
from bs4 import BeautifulSoup as bs
import hashlib
import urllib
from urllib.request import urlopen

class Search():
    def __init__(self,name,path):
        self.name=name
        self.path=path
        self.list_searched=[]
        self.version=True
        self.net=True
        
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

        try:
            link="https://genius.com/api/search/multi?per_page=5&q="+word
            r=requests.get(link).json()
            for item in r["response"]["sections"]:
                for subitem in item["hits"]:
                    if "path" in subitem["result"]:
                        searched=(subitem["result"]["path"]).lower()
                        self.list_searched.append(searched[1:-7])
            self.name=self.list_searched
        except:
            pass
                    
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

        try:
            r=requests.get("https://genius.com/"+word+"-lyrics")
            soup=bs(r.content,"html.parser")
            self.open=soup.find("div",{"class":"lyrics"})
            self.open=self.open.get_text()
        except:
            try:
                r=requests.get("https://genius.com/"+word+"-lyrics")
                soup=bs(r.content,"html.parser")
                self.open=soup.find("div",{"class":"lyrics"})
                self.open=self.open.get_text()
            except:
                try:
                    r=requests.get("https://genius.com/"+word+"-lyrics")
                    soup=bs(r.content,"html.parser")
                    self.open=soup.find("div",{"class":"lyrics"})
                    self.open=self.open.get_text()
                except:
                    try:
                        r=requests.get("https://genius.com/"+word+"-lyrics")
                        soup=bs(r.content,"html.parser")
                        self.open=soup.find("div",{"class":"lyrics"})
                        self.open=self.open.get_text()
                    except:
                        try:
                            r=requests.get("https://genius.com/"+word+"-lyrics")
                            soup=bs(r.content,"html.parser")
                            self.open=soup.find("div",{"class":"lyrics"})
                            self.open=self.open.get_text()
                        except:
                            pass

        if (self.open !=None):
            open(self.path+".lyrics.txt","w+", errors='ignore',encoding='ascii').write(self.open)
        else:
            self.name=False


    def check_version(self):
        version=self.path

        try:
            r=requests.get(self.name+"/blob/master/README.md")
            soup=bs(r.content,"html.parser")
            soup=soup.find("div",{"class":"readme"})
            soup=soup.find_all("li")
            soup=soup[5].text
            hash = hashlib.sha256(soup.encode())
            soup=hash.hexdigest()
            if soup==version:
                self.version=True
            else:
                self.version=False
        except:
            pass


