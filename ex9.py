import requests
from bs4 import BeautifulSoup

def fn():
  url = "https://www.nytimes.com"
  r = requests.get(url)
  raw_html = r.text
  soup = BeautifulSoup(raw_html, features="html.parser")
  titles = soup.find_all("h3")
  file = open("titles.txt", "w")
  for title in titles:
    file.write(f"{title.string}\n")
  file.close() 