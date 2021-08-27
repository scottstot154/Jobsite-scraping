import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract1(page):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    url1 = f'https://internshala.com/internships/matching-preferences={page}'
    r = requests.get(url1, headers)
    soup1 = BeautifulSoup(r.content,'html.parser')
    return soup1

def transform1(soup1):
    divs1 = soup1.find_all('div', class_ = 'container-fluid individual_internship')
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

        job1 = {
            'task':task,
            'company':company,
            'details':summary,
            'location':location,
            'salary':salary,
            'begin':begin,
        }
        joblist.append(job1)
    return

def extract2(page):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    url2 = f'https://www.talentrack.in/{page}'
    r2 = requests.get(url2, headers)
    soup2 = BeautifulSoup(r2.content,'html.parser')
    return soup2

def transform2(soup2):
    divs2 = soup2.find_all('div',class_='job-box')
    for item in divs2:
        task = item.find('span',class_='job-title').text.strip()
        print(task)
        details = item.find('span',class_='job-detail').text.strip().replace('Looking for ','')
        location = item.find('span',class_='job-location').text.strip().replace('location: ','')
        date = item.find('span',class_='job-date').text.strip().replace('posted on: ','')
        print(details)
        print(location)
        print(date)
    
        job2 = {
            'task':task,
            'company':'talent track',
            'details':details,
            'location':location,
            'salary':'',
            'begin':date,
            }
        joblist.append(job2)
    return

joblist = []

c = extract1(0)
transform1(c)
d = extract2(0)
transform2(d)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
