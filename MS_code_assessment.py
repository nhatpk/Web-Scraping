''' 
  Web Scraping by Python
  --- MS code assessent
  --- Nhat Pham
  --- 10/22/2020
'''

def crawler_ms():
  # Retrieve the page
  import requests
  url = 'https://en.wikipedia.org/wiki/Microsoft'
  requests.get(url)
  page = requests.get(url)
  #print(page)

  # Parse page's content
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(page.text, 'html.parser')

  # Search the start tag of History section
  startTag = soup.find(id="History").parent
  #print(startTag.name)

  # Loop all p tag until next section's tag 
  content = ""
  for elm in startTag.next_siblings:
    if elm.name == startTag.name:
      # (next section's tag).name == startTag.name
      # break/exit the loop
      break
    if elm.name not in ['div', 'a', 'p']:
      # element is not div/a/p 
      # ignore it, continue the loop
      continue
    content += elm.text.strip("\n") + " "
  #print(content)

  # Tokenize the content
  #from nltk.tokenize import regexp_tokenize
  #tokenizedContent = regexp_tokenize(content, "[\w']+")
  #print(tokenizedContent)

  # Break content into words and display the first n words
  n = 10 # number of words to display
  import pandas as pd
  result = pd.Series(content.split()).value_counts()[:n]
  print(result)