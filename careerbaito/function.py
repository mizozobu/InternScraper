import bs4 as bs
import urllib.request


class job():
    def __init__(self, title="", publishedOn="", wage="", transportation="", location="", link=""):
        self.title = title
        self.publishedOn = publishedOn
        self.wage = wage
        self.transportation = transportation
        self.location = location
        self.link = link
