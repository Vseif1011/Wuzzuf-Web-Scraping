import requests 
from bs4 import BeautifulSoup
import math
import pandas as pd 

def find_no_pages(search):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get('https://wuzzuf.net/search/jobs/?a=hpb&q='+search.replace(' ','%20'), headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    jobsQ = soup.find('span',{'class':'css-xkh9ud'})
    if jobsQ is not None and jobsQ.strong is not None:
        Jobs = int(jobsQ.strong.text.replace(',', ''))
    else:
        Jobs = 0
    no_pages = math.ceil(Jobs/15) if Jobs > 0 else 0
    return no_pages

def scrap(query):
    number_of_pages = find_no_pages(query)
    query = query.replace(' ','%20')
    
    Job_titles,Links,descriptions,Occupations,Locations,Companies=[],[],[],[],[],[]
    for page in range(number_of_pages):
        page = requests.get('https://wuzzuf.net/search/jobs/?a=hpb&q=' + query + '&start=' + str(page))
        soup = BeautifulSoup(page.content,'lxml')

        TitlesQ = soup.find_all('h2',{'class': 'css-m604qf'})
        Job_titles += [title.a.text for title in TitlesQ]
        LinksQ = []
        for title in TitlesQ:
            href = title.a['href']
            if href.startswith('http'):
                LinksQ.append(href)
            else:
                LinksQ.append('https://wuzzuf.net' + href)
        Links += LinksQ

        DescriptionsQ = soup.find_all('div', {'class': 'css-y4udm8'})
        descriptions += [Description.text for Description in DescriptionsQ]

        OccupationsQ = soup.find_all("div", {'class': 'css-1lh32fc'})
        Occupations += [Occupation.text for Occupation in OccupationsQ]

        LocationsQ = soup.find_all('span',{'class':'css-5wys0k'})
        Locations += [Location.text for Location in LocationsQ]

        CompaniesQ = soup.find_all("a", {'class': 'css-17s97q8'})
        Companies += [Company.text for Company in CompaniesQ]

    Scraped_Data = {}
    Scraped_Data['Titles'] = Job_titles
    Scraped_Data['Occupation'] = Occupations
    Scraped_Data['Description'] = descriptions
    Scraped_Data['Company']= Companies
    Scraped_Data['Location']=Locations
    Scraped_Data['Link']= Links

    df = pd.DataFrame(Scraped_Data)
    print(df)
    return Scraped_Data,df


def combine_data_frames(dfs):
    combined_df=pd.concat(dfs)
    combined_df.drop_duplicates()
    return combined_df

def combine_dicts(dicts):
    combined_dict = {}
    for key in dicts[0].keys():
        combined_dict[key] = []
        for dict in dicts:
            combined_dict[key] += dict[key]
    return combined_dict  



