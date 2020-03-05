import requests
from bs4 import BeautifulSoup


class Crawler(object):
    def __init__(self, proxy):
        self.proxy = proxy

    def get_soup(self, url, values):
        data = requests.post(url, data=values)
        soup = BeautifulSoup(data.text, 'lxml')
        return soup

    def post(self):
        pass


crawler = Crawler(None)
