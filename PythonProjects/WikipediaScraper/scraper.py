import requests
import hashTable as ht
from bs4 import BeautifulSoup

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')
allLinks = soup.find(id="bodyContent").find_all("a")
new_links = []
old_links = ht.hashTable()

for link in allLinks:
    if link['href'].find("/wiki") == -1:
        continue
    new_url = "https://en.wikipedia.org" + link['href']

    if new_url not in new_links:
        new_links.append(new_url)

while new_links != []:
    tmp_new_links = []
    for link in new_links:
        if old_links.contains(link):
            continue
        response = requests.get(
            url=link,
        )
        allLinks = soup.find(id="bodyContent").find_all("a")
        print(f"Scraping {link}")
        for new_link in allLinks:
            if new_link['href'].find("/wiki") == -1:
                continue
            new_url = "https://en.wikipedia.org" + new_link['href']
            if new_url not in tmp_new_links and not old_links.contains(new_url):
                if new_url not in new_links:
                    tmp_new_links.append(new_url)
            if old_links.contains(new_url):
                old_links.insert(new_url)
    new_links = tmp_new_links
        