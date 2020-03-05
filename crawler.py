import requests
from bs4 import BeautifulSoup


class Crawler(object):
    def __init__(self, proxies=None):
        self.proxies = proxies or {}
        self.session = requests.Session()
        self.response = None
        self.url = ''
        self.data = {}

    def crawl(self, url, data):
        self.url = url
        self.data = data
        self.response = self._post(url, data=data, proxies=self.proxies)

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
