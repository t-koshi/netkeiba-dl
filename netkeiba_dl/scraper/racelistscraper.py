import urllib
import re
from itertools import chain
from bs4 import BeautifulSoup

class RaceListScraper:
    @classmethod
    def scrape(self):
        base_url = 'http://db.netkeiba.com/?pid=race_top'
        race_page_urls = [self.__extract_race(url) for url in self.__extract_race_list(base_url)]
        race_url_list = list(chain.from_iterable(race_page_urls))
        file = "race_list.csv"
        with open(file, "w", encoding = "utf_8") as fileobj:
            for race_url in race_url_list:
                fileobj.write(race_url + "\n")

    @classmethod
    def __extract_race_list(self, base_url):
        html = urllib.request.urlopen(base_url)
        soup = BeautifulSoup(html, 'html.parser')
        return ["http://db.netkeiba.com" + anchor_tag["href"] for anchor_tag in soup.find_all("a", href=re.compile(r"/race/list/\d"))]

    @classmethod
    def __extract_race(self, base_url):
        html = urllib.request.urlopen(base_url)
        soup = BeautifulSoup(html, 'html.parser')
        return ["http://db.netkeiba.com" + anchor_tag["href"] for anchor_tag in soup.find_all("a", href=re.compile(r"/race/\d"))]


