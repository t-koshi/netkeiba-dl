import urllib
import re
from bs4 import BeautifulSoup

class RaceScraper:
    @classmethod
    def scrape(self):
        file = "race_list.csv"
        with open(file, "r", encoding = "utf_8") as fileobj:
            for line in fileobj:
                html = urllib.request.urlopen(line)
                soup = BeautifulSoup(html, 'html.parser')
                print(soup)



