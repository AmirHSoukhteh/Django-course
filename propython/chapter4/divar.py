from bs4 import BeautifulSoup
import re
import requests

r = requests.get("https://divar.ir/s/tehran")
#for more result try following code
#r = requests.get("https://divar.ir/s/tehran?q=%D8%AA%D9%88%D8%A7%D9%81%D9%82%DB%8C")
soup = BeautifulSoup(r.text, "html.parser")
res = soup.find_all("div", {"class":"kt-post-card__info"})

for thing in res:
    res1 = thing.find_all("div", {"class":"kt-post-card__description"})
    for thing in res:
        res1 = thing.find_all("div", {"class":"kt-post-card__description"})
        l = len(res1)
        for i in range(l):
            if "توافقی" in res1[i].text:
                print(re.search(r"title\">(.*)</h2>", str(thing)).group(1))
                print(res1[i].text)
            