''' 
  Web Scraping by Python
  --- MS code assessent
  --- Nhat Pham
  --- 10/22/2020
'''
import requests
from bs4 import BeautifulSoup
from lxml import html

def crawler_69shu():
  # Retrieve the page
  url = 'https://www.69shu.com/30568/'
  page = requests.get(url)
  #print(page)

  # Parse page's content
  soup = BeautifulSoup(page.text, 'html.parser')

  # Find the mulu_list
  mulu = soup.find_all("ul", class_="mulu_list")[1]
  #print(mulu)

  # Get list of url
  listUrl = []
  for elm in mulu.find_all('a'):
    listUrl.append(elm.get('href'))
  #print(listUrl)

  # 
  content = ""
  for link in listUrl:
    content += getContent(link) + "\n-------------------------------------------------------------------------------------------------\n"
  #print(content)

  file = open("txt.txt","a")
  file.write(content) 
  file.close() 

def getContent(link):
  page = requests.get(link)
  soup = BeautifulSoup(page.content, 'lxml')
  
  content = str(soup.find_all("div", class_="yd_text2")[0].get_text())

  return content