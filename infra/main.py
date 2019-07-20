import bs4 as bs
import urllib.request
from datetime import datetime
from function import job
import csv

# write csv https://www.craneto.co.jp/archives/1309/
# to csv http://primarytext.jp/blog/1275

# create csv and write header
try:
    f = open('infra/infra-intern.csv', 'w', encoding='UTF-8')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['Today', 'Title', 'Pulilshed On', 'Wage', 'transportation', 'Location', 'Link'])
except csv.Error as e:
    print(e)

for i in range(1, 9):
    url = 'https://www.in-fra.jp/intern-list/occupations/1?page=' + str(i)
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    posts = soup.find_all(class_='card-wrapper')

    for post in posts:
        j = job()
        atag = post.find(class_='intern-title').find('a')
        j.title = atag.get_text()
        j.link = "https://www.in-fra.jp" + atag.get('href')
        j.publishedOn = post.find(class_='publish-date').get_text()
        now = datetime.now()
        today = '%s/%s/%s' % (now.month, now.day, now.year)
        try:
            j.get_data()
        except Exception as e:
            print("Cannot open: " + j.link)

        try:
            writer.writerow([today, j.title, j.publishedOn, j.wage, j.transportation, j.location, j.link])
        except csv.Error as e:
            print(e)

    print("page {} done".format(i))
