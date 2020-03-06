import crawler


class MynicCrawler(crawler.Crawler):
    def parse_data(self):
        contactboxes = self.soup.find_all("div", {"class": "contactdetails"})
        invoicing_party = contactboxes[0]
        registrant = contactboxes[1]
        administrative_contact = contactboxes[2]
        billing_contact = contactboxes[3]
        technical_contact = contactboxes[4]
        # name_server = contactboxes[5]
        data={
            'invoicing_party_dict': {},
            'registrant_dict': {},
            'administrative_contact_dict': {},
            'billing_contact_dict': {},
            'technical_contact_dict': {},

        }
        # name_server_dict = {}

        def fill_data(node, dict):
            dict.update({
                'name': node.find('li', {'class': 'cname'}).text.strip(),
                'address': node.find('li', {'class': 'caddress'}).text.strip(),
                'email': node.find('span', {'class': 'cemail'}).find_next_sibling('a').text.strip(),
                'phone': node.find('span', {'class': 'cphone'}).find_next_sibling('a').text.strip(),
                'fax': node.find('span', {'class': 'cfax'}) and node.find('span', {'class': 'cfax'}).text.strip() or '',
            })

        fill_data(invoicing_party, data['invoicing_party_dict'])
        fill_data(registrant, data['registrant_dict'])
        fill_data(administrative_contact, data['administrative_contact_dict'])
        fill_data(billing_contact, data['billing_contact_dict'])
        fill_data(technical_contact, data['technical_contact_dict'])
        # fill_data(name_server, name_server_dict)
        return data
tor_proxy = 'socks5://localhost:9050'

from multiprocessing import Pool
import os
if __name__ == '__main__':
    def test(count):
        print(count)
        c = MynicCrawler(proxies={'http': tor_proxy, 'https': tor_proxy})
        c.crawl('https://mynic.my/whois/', {'domain': 'test.my'})
        data = c.parse_data()
        print(data)

    # with Pool(os.cpu_count()) as p:
    #     p.map(test, range(10))
    test(1)

