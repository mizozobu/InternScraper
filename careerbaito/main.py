import bs4 as bs
import urllib.request
from datetime import datetime
from function import job
import csv

# write csv https://www.craneto.co.jp/archives/1309/
# to csv http://primarytext.jp/blog/1275

# create csv and write header
try:
    f = open('careerbaito/careerbaito-intern.csv', 'w', encoding='UTF-8')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['Today', 'Title', 'Pulilshed On', 'Wage', 'transportation', 'Location', 'Link'])
except csv.Error as e:
    print(e)

for i in range(1, 3):
    url = "https://careerbaito.com/search/3/66?page=1"
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    posts = soup.find_all(class_='l-jobSearch-listArea')

    for post in posts:
        if 'wanted_exit' not in post.get('class'):
            j = job()
            j.title = post.find('h2').get_text()
            j.link = "https://careerbaito.com" + post.find('a').get('href')
            j.publishedOn = ""
            now = datetime.now()
            today = '%s/%s/%s' % (now.month, now.day, now.year)

            details = post.find_all('dl')

            j.wage = details[1].find('dd').get_text()
            j.location = details[2].find('dd').get_text()
            try:
                writer.writerow([today, j.title, j.publishedOn, j.wage, j.transportation, j.location, j.link])
            except csv.Error as e:
                print(e)

    print("page {} done".format(i))
