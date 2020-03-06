import requests
from bs4 import BeautifulSoup


class Crawler(object):
    def __init__(self, proxies=None):
        self.session = requests.Session()
        self.session.proxies = proxies
        self.response = None

    def crawl(self, url, data):
        self.response = self._post(url, data=data)

    def _post(self, *args, **kwargs):
        response = self.session.post(*args, **kwargs)
        return response

    def _get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        return response

    @property
    def soup(self):
        soup = BeautifulSoup(self.response.text, 'lxml')
        return soup

    @property
    def raw(self):
        return self.response.text

    def parse_data(self):
        raise Exception("You need to implement this method")
