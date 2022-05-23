#############################
### LinkedIn Data Scraper ###
#############################

### Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
### Classes
import login_details
import connections
import requiredConnections



def main(linkedins):
    driver = loginToLinkedIn()

    # Local storage variables
    result = {}
    industry = []
    country = []
    totalEmployees = []
    allConnections = {}

    # Main Code
    for company in linkedins:  
        if company == "Blank":
            industry.append("No Industry");
            country.append("No Country");
            totalEmployees.append("No Employee Information");
            continue;
        
        driver.get(company)
        start = time.time()
          
        # Scrape the lxml page for the data we need
        src = driver.page_source

        soup = BeautifulSoup(src, 'lxml')

        # Scrape company name
        companyName = soup.find_all('h1', class_ = "t-24 t-black t-bold full-width")[0].get_text().strip();
        print(companyName)

        # Scrape for the industry of the company. If successful, add it to the list
        intro = soup.find('div', {'class': "ph5 pt3"})
        try:  
            items = intro.find_all("div", {'class': 'org-top-card-summary-info-list__info-item'})
            industry.append(items[0].get_text().strip().replace(",", ";"))
        except:
            industry.append("No Industry");

        ## Scrape for the country of the company. If successful, add it to the list
        try:
            country.append(items[1].get_text().strip().replace(",", ";"))
        except:
            country.append("No Country");
        

        ## Scrape the number of employees. If successful, add it to the list
        try:
            totalEmployeesNum = intro.find("span", {'class': "org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state"})
            totalEmployees.append(totalEmployeesNum.get_text().strip().replace(",",""))
        except:
            totalEmployees.append("No Employee Information");

        ## Scrape 1st and 2nd degree connections. If successful, add it to the dictionary
        
        # Find the search link of this company
        
        searchLinkSuffix = soup.find('a', class_= "ember-view org-top-card-secondary-content__see-all-link", href = True)
        # To switch between different LinkedIn formats
        if searchLinkSuffix == None:
            searchLinkSuffix = soup.find('div', class_='display-flex mt2 mb1').find('a', href = True)
        # If the link is present, scrape the profile. Else, return none found
        if searchLinkSuffix:
            searchLink = "https://www.linkedin.com/" + searchLinkSuffix['href']
            connCompany = connections.main(driver, searchLink)
            allConnections[companyName] = connCompany
        else:
            allConnections[companyName] = requiredConnections.returnCompanyConnectionsNotFound();
            

    # Code completed, exit and return
    driver.quit()
    return {"industry" : industry, "country" : country, "totalEmployees" : totalEmployees, "connections" : allConnections}




def loginToLinkedIn():
    # Open the driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://linkedin.com/uas/login")

    try:
        details = login_details.details();
    except:
        driver.quit()
        print("Login Details are unavailable")

    # entering username
    username = driver.find_element(By.ID, "username")

    # Enter Your Email Address
    username.send_keys(details['email'])  
      
    # entering password
    pword = driver.find_element(By.ID,"password")

    # Enter Your Password
    pword.send_keys(details['password'])

    # Clicking on the log in button
    # Format (syntax) of writing XPath --> 
    # //tagname[@attribute='value']
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    return driver
