import bs4 as bs
import urllib.request
from datetime import datetime
from function import job
import csv

# write csv https://www.craneto.co.jp/archives/1309/
# to csv http://primarytext.jp/blog/1275

# create csv and write header
try:
    f = open('01intern/01intern-intern.csv', 'w', encoding='UTF-8')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['Today', 'Title', 'Pulilshed On', 'Wage', 'transportation', 'Location', 'Link'])
except csv.Error as e:
    print(e)

for i in range(1, 9):
    url = "https://01intern.com/job/list.html?page=" + str(i) + "&jobTypes=2&stickingConditions=8"
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    posts = soup.find_all(class_='l-common-joblistBox')

    for post in posts:
        j = job()
        content = post.find(class_='l-common-joblist_text')
        j.title = content.find('h4').get_text()
        j.link = "https://01intern.com" + content.find('a').get('href')
        j.publishedOn = ""
        now = datetime.now()
        today = '%s/%s/%s' % (now.month, now.day, now.year)

        details = post.find_all('dl')

        j.wage = details[0].find('dd').get_text()
        j.transportation = details[0].find('dd').get_text()
        j.location = details[3].find('dd').get_text()
        try:
            writer.writerow([today, j.title, j.publishedOn, j.wage, j.transportation, j.location, j.link])
        except csv.Error as e:
            print(e)

    print("page {} done".format(i))
