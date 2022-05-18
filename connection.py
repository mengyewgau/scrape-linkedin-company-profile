from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import login_details

def main(browser, link):
    browser.get(link)
    
    print('\nScraping your connections...\n')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    pageNum = 2
    totalResults = int(soup.find("h2", class_ = 'pb2 t-black--light t-14').text.strip().split()[0])
    print(totalResults)
    names = []
    links = []
    while True:
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for profile in soup.find_all('a', class_='app-aware-link',href=True):
            if 'View' in profile.text:
                name = profile.text.strip().partition("View")[0];
                print(name)
                names.append(name)
                links.append(profile['href'])
        if len(names) == totalResults:
            break
        browser.get(link + '&page='+str(pageNum))
        pageNum += 1
        time.sleep(3)
        
        
    return {"names" : names, "links" : links};


if __name__ == '__main__':
    html_extract = main(browser, link)
