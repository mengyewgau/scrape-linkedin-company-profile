#############################
### LinkedIn Data Scraper ###
#############################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import login_details
import connections


def main(linkedins):

    # Open the driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://linkedin.com/uas/login")

    # entering username
    username = driver.find_element(By.ID, "username")

    # Enter Your Email Address
    username.send_keys(login_details.email)  
      
    # entering password
    pword = driver.find_element(By.ID,"password")

    # Enter Your Password
    pword.send_keys(login_details.password)

    # Clicking on the log in button
    # Format (syntax) of writing XPath --> 
    # //tagname[@attribute='value']
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

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
        companyName = soup.find('h1', class_ = "t-24 t-black t-bold full-width").get_text().strip();
        print(companyName)

        # Scrape for Industry, Country, and Number of Employees
        intro = soup.find('div', {'class': "ph5 pt3"})
        try:  
            items = intro.find_all("div", {'class': 'org-top-card-summary-info-list__info-item'})
            industry.append(items[0].get_text().strip().replace(",", ";"))
        except:
            industry.append("No Industry");
        try:
            country.append(items[1].get_text().strip().replace(",", ";"))
        except:
            country.append("No Country");
        try:
            totalEmployeesNum = intro.find("span", {'class': "org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state"})
            totalEmployees.append(totalEmployeesNum.get_text().strip().replace(",",""))
        except:
            totalEmployees.append("No Employee Information");

        ## Scrape 1st and 2nd degree connections
        
        # Find the search link of this company
        try:
            searchLinkSuffix = soup.find('a', class_= "ember-view org-top-card-secondary-content__see-all-link", href = True)['href']
            searchLink = "https://www.linkedin.com/" + searchLinkSuffix            
        except:
            allConnections[companyName] = { 'YLM': [],
                                            'arnaud_blandin': [],
                                            'pierre_rico': [],
                                            'etienne_bogaert': [],
                                            'margot': [],
                                            'marwan': [],
                                            'thibaut': []}
        else:
            # Return results
            connCompany = connections.main(driver, searchLink)
            allConnections[companyName] = connCompany

    # Code completed, exit and return
    driver.quit()
    return {"industry" : industry, "country" : country, "totalEmployees" : totalEmployees, "connections" : allConnections}
