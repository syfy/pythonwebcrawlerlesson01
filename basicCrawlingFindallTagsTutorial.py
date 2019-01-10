from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
#nameList = bsObj.findAll("span", {"class":"green","class":"red"})
#for name in nameList:
#    print(name.get_text())
    
    
nameList = bsObj.findAll(text="I think,")
##print(len(nameList))    


allText = bsObj.findAll(id="text")
#search for pa specific attriute

allText = bsObj.findAll("",{"id":"text"});
#same as above
print(allText[0].get_text())
