#############################
### LinkedIn Data Scraper ###
#############################

### Libraries
from bs4 import BeautifulSoup
import time
### Classes
import login
import connections
import requiredConnections;
import country;
import industry;
import numEmployees;

def main(linkedins):
    driver = login.loginToLinkedIn()

    # Local storage variables
    verticals = []
    countries = []
    totalEmployees = []
    allConnections = {}

    def failedConnections(companyLinkedIn): #Helper function
        industry.append("Failed");
        countries.append("Failed");
        totalEmployees.append("Failed");
        allConnections[companyLinkedIn] = requiredConnections.returnCompanyConnectionsNotFound();

    # Main Code
    for company in linkedins:
        if company == "Blank":
            failedConnections(company);
            continue;
        
        driver.get(company)
        time.sleep(5)
        
        # Scrape the lxml page for the data we need
        src = driver.page_source

        soup = BeautifulSoup(src, 'lxml')

        # Scrape company name, this is the first check to ensure the scraping is correct
        try:
            companyName = soup.select('h1', class_ = "t-24 t-black t-bold full-width")[0].get_text().strip();
            print("\n" + companyName)
        except:
            failedConnections(company);
            continue;


        # Scrape for the industry of the company. If successful, add it to the list
        intro = soup.find('div', {'class': "ph5 pt3"})
        items = intro.find_all("div", {'class': 'org-top-card-summary-info-list__info-item'})
        
        ## Scrape for the country of the company. If successful, add it to the list
        verticals = industry.getVertical(items, verticals);
        ## Scrape for the country of the company. If successful, add it to the list
        countries = country.getCountry(items, countries);
        ## Scrape the number of employees. If successful, add it to the list
        totalEmployees =  numEmployees.getNumEmployees(intro, totalEmployees)

        ## Scrape 1st and 2nd degree connections. If successful, add it to the dictionary
        
        # Find the search link of this company
        searchLinkSuffix = soup.find('a', class_= "ember-view org-top-card-secondary-content__see-all-link", href = True)
        # To switch between different LinkedIn formats
        if searchLinkSuffix == None:
            try:
                searchLinkSuffix = soup.find('div', class_='display-flex mt2 mb1').find('a', href = True)
            except:
                allConnections[companyName] = requiredConnections.returnCompanyConnectionsNotFound();
            else:
                allConnections[companyName] = useConnectionsScraper(driver, searchLinkSuffix);
        else:
            allConnections[companyName] = useConnectionsScraper(driver, searchLinkSuffix);
            

    # Code completed, exit and return
    driver.quit()
    return {"industry" : verticals, "country" : countries, "totalEmployees" : totalEmployees, "connections" : allConnections}

def useConnectionsScraper(driver, searchLinkSuffix):
    searchLink = "https://www.linkedin.com/" + searchLinkSuffix['href']
    return connections.main(driver, searchLink)


