# Objective: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# Referen
import requests
from bs4 import BeautifulSoup as soup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

parsed_data = soup(r_html, features="lxml")
article_title = parsed_data.find('span')
print(article_title)

