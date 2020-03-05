import crawler


class MynicCrawler(crawler.Crawler):
    def parse_data(self):
        contactboxes = self.soup.find_all("div", {"class": "contactdetails"})
        invoicing_party = contactboxes[0]
        registrant = contactboxes[1]
        administrative_contact = contactboxes[2]
        billing_contact = contactboxes[3]
        technical_contact = contactboxes[4]
        name_server = contactboxes[5]

        invoicing_party_dict = {}
        registrant_dict = {}
        administrative_contact_dict = {}
        billing_contact_dict = {}
        technical_contact_dict = {}
        name_server_dict = {}

        def fill_data(node, dict):
            dict.update({
                'name': node.find('li', {'class': 'cname'}).text.strip(),
                'address': node.find('li', {'class': 'caddress'}).text.strip(),
                'email': node.find('span', {'class': 'cemail'}).find_next_sibling('a').text.strip(),
                'phone': node.find('span', {'class': 'cphone'}).find_next_sibling('a').text.strip(),
                'fax': node.find('span', {'class': 'cfax'}) and node.find('span', {'class': 'cfax'}).text.strip() or '',
            })

        fill_data(invoicing_party, invoicing_party_dict)
        fill_data(registrant, registrant_dict)
        fill_data(administrative_contact, administrative_contact_dict)
        fill_data(billing_contact, billing_contact_dict)
        fill_data(technical_contact, technical_contact_dict)
        fill_data(name_server, name_server_dict)


if __name__ == '__main__':
    c = MynicCrawler()
    c.crawl('https://mynic.my/whois/', {'domain': 'test.my'})
    c.parse_data()
