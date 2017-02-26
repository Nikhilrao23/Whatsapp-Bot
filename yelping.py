import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Coffee+shop&find_loc=Jersey+City%2C+NJ&ns=1"

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    print ("<a href = %s>%s</a>" %(link.get("href"), link.text))

g_data = soup.find_all("div", {"class": "biz-listing-large"})

for item in g_data:
    print (item.contents[0].find_all("a", {"class": "biz-name js-analytics-click"})[0].text)







