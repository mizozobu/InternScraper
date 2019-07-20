import bs4 as bs
import urllib.request
from datetime import datetime


class job():
    def __init__(self, title="", publishedOn="", wage="", transportation="", location="", link=""):
        self.title = title
        self.publishedOn = publishedOn
        self.wage = wage
        self.transportation = transportation
        self.location = location
        self.link = link

    def get_data(self):
        source = urllib.request.urlopen(self.link).read()
        soup = bs.BeautifulSoup(source, 'lxml')

        details = soup.find_all(class_='intern-detail-others-list-content')
        self.wage = details[0].get_text()
        self.transportation = details[1].get_text()
        self.location = details[2].get_text()
