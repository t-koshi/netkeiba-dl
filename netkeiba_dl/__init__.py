from .scraper import (RaceListScraper, RaceScraper)

def _real_main(argv=None):
    RaceListScraper.scrape()
    RaceScraper.scrape()


def main(argv=None):
    print('start scrape netkeiba !')
    _real_main(argv)

__all__ = ['main']
