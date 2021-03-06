import requests
from quick_search.models import SearchResult
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import timedelta
from django.utils import timezone

base_url = "https://www.google.com/search?q="

def get_search_results(query):

    search_results = get_cached_responses(query)

    if(len(search_results)>0):
        print("returning from cache")
        return search_results

    search_url = base_url
    for word in query.split(" "):
        search_url = search_url + word + "+"
    search_url = search_url[:-1]

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(search_url)

    html = driver.page_source

    soup = bs(html, 'html.parser')

    results = soup.findAll('div', attrs={'class':'rc'})
    print(len(results))

    i = 0

    for result in results:
        search_result = SearchResult.objects.create()
        search_result.query = str(query)
        print(search_result.query)
        try:
            header = result.find('div', attrs={'class':'r'}).find('a')
            header_text = header.find('h3')
            search_result.heading = str(header_text.text)
            link = header['href']
            search_result.url = str(link)
            preview = result.find('div', attrs={'class':'s'}).find('span', attrs={'class':'st'})
            try:
                search_result.text = str(preview.text)
            except:
                pass
            search_results.append(search_result)
            search_result.save()
        except:
            pass
    return search_results

def get_cached_responses(query):
    minus30mins = timedelta(minutes=30)
    filter_time = timezone.now() - minus30mins
    results = SearchResult.objects.filter(time_created__gte=filter_time).filter(query=query)
    return list(results)
