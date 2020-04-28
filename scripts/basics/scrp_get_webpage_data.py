import requests
from bs4 import BeautifulSoup
page = requests.get('https://finviz.com/forex_performance.ashx')
soup = BeautifulSoup(page.content, 'html.parser')
#forex = soup.find_all("span")
#tr_elements = soup.find_all("tr")
dat = soup.find_all("span")
print(dat)