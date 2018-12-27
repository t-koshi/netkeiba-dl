import urllib
import re
from bs4 import BeautifulSoup

class RaceScraper:
    @classmethod
    def scrape(self):
        file = "race_list.csv"
        with open(file, "r", encoding = "utf_8") as fileobj:
            for line in fileobj:
                race_id = re.match(".*?/race/(\d*).*", line).group(1)
                print("race_id: " + race_id)
                html = urllib.request.urlopen(line)
                soup = BeautifulSoup(html, 'html.parser')
                output_file = "html/" + race_id + ".html"
                with open(output_file, "w", encoding = "utf_8") as output_fileobj:
                    output_fileobj.write(soup.prettify())

    @classmethod
    def extract(self):
        file = "race_list.csv"
        with open(file, "r", encoding = "utf_8") as fileobj:
            for line in fileobj:
                race_id = re.match(".*?/race/(\d*).*", line).group(1)
                print("race_id: " + race_id)
                html_file = "html/" + race_id + ".html"
                with open(html_file, "r", encoding = "utf_8") as html_fileobj:
                    soup = BeautifulSoup(html_fileobj, 'html.parser')
                    print(soup)



