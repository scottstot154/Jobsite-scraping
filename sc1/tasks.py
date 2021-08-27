from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from .models import Jobs

# scraping function
@shared_task
def scrap_jobs1():
    print('fetching..')
    req1 = Request('https://internshala.com/internships/matching-preferences')
    html1 = urlopen(req1).read()
    bs1 = BeautifulSoup(html1,'lxml')
    divs1 = bs1.find_all('div', class_ = 'container-fluid individual_internship')
    for item in divs1:
        task = item.find('a').text.strip()
        company = item.find('div',class_ = 'heading_6 company_name').text.strip()
        location = item.find('div',{'id' : 'location_names'}).text.strip()
        try:
            salary = item.find('span',class_ = 'stipend').text.strip().replace('/month','')
        except:
            salary = ''
        try:
            summary = item.find('div',class_ = 'body-main').text.strip()
        except:
            summary = ''
        begin = item.find('div',{'id':'start-date-first'}).text.strip().replace('immediatelyImmediately','immediately')
        print({'task':task,
            'company':company,
            'details':details,
            'location':location,
            'salary':salary,
            'begin':begin,}
        )

        Jobs.objects.create(
            task=task,
            company=company,
            details=details,
            location=location,
            salary=salary,
            begin=begin
        )
@shared_task
def scrap_jobs2():
    print('fetching.2nd..')
    req2 = Request('https://www.talentrack.in/')
    html2 = urlopen(req2).read()
    bs2 = BeautifulSoup(html2,'lxml')
    divs2 = bs2.find_all('div',class_='job-box')
    for item in divs2:
        task = item.find('span',class_='job-title').text.strip()
        details = item.find('span',class_='job-detail').text.strip().replace('Looking for ','')
        location = item.find('span',class_='job-location').text.strip().replace('location: ','')
        begin = item.find('span',class_='job-date').text.strip().replace('posted on: ','')
        print({'task':task,
            'details':details,
            'location':location,
            'begin':begin,}
        )

        Jobs.objects.create(
            task=task,
            details=details,
            location=location,
            begin=begin
        )

    sleep(5)

scrap_jobs1()
scrap_jobs2()

