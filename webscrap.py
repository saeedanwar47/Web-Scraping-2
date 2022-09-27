from itertools import product
from urllib import response
from bs4 import BeautifulSoup
import requests
url = "https://www.flipkart.com/search?q=camera&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&as-pos=3&as-type=RECENT&suggestionId=camera%7CDSLR+%26+Mirrorless&requestId=e6899f59-8b40-4908-afa4-33afca0b5be9&as-searchtext=camera"
response =requests.get(url)
#print(response.content) 
htmlcontent = response.content
bs =BeautifulSoup(htmlcontent, 'html.parser')
#print(bs.prettify())
#print(bs.title)
#print(bs.title.name)
#print(bs.title.string)
#print(bs.find_all('a'))
#print(bs.find(id='next-page-link-tag'))
#for link in bs.find_all('a'):
#print(link.get('href'))

#for image in bs.find_all('img'):
    #print(image.get('src'))
product = bs.find_all('div',attrs={'class':'_396cs4 _3exPp9'})
print(product)

