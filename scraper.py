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
    result = {}
    industry = []
    country = []
    totalEmployees = []
    
    for company in linkedins:  
        if company == "Blank":
            industry.append("No Industry");
            country.append("No Country");
            totalEmployees.append("No Employee Information");
            continue;
        
        driver.get(company)
        start = time.time()
          
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

##        while True:
##            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
##            # this command scrolls the window starting from
##            # the pixel value stored in the initialScroll 
##            # variable to the pixel value stored at the
##            # finalScroll variable
##            initialScroll = finalScroll
##            finalScroll += 1000
##          
##            # we will stop the script for 3 seconds so that 
##            # the data can load
##            time.sleep(3)
##            # You can change it as per your needs and internet speed
##          
##            end = time.time()
##            # We will scroll for 20 seconds.
##            # You can change it as per your needs and internet speed
##            if round(end - start) > 15:
##                break
          
        # Scrape the lxml page for the data we need
        src = driver.page_source

        soup = BeautifulSoup(src, 'lxml')

        # Scrape company name
        companyName = soup.find('h1', class_ = "t-24 t-black t-bold full-width").get_text().strip();

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
            totalEmployees = intro.find("span", {'class': "org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state"})
            totalEmployees.append(totalEmployees.get_text().strip().replace(",",""))
        except:
            totalEmployees.append("No Employee Information");

        # Scrape 1st and 2nd degree connections
        allCompanyConnections = {}
        
        # Find the search link of this company
        try:
            searchLinkSuffix = soup.find('a', class_= "ember-view org-top-card-secondary-content__see-all-link", href = True)['href']
            searchLink = "https://www.linkedin.com/" + searchLinkSuffix
            # Return results
            connCompany = connections.main(driver, searchLink)
            allCompanyConnections[companyName] = connCompany
        except:
            allCompanyConnections[companyName] = {"employeeNames" : [], "profileLinks" : []};

    driver.quit()
    return {"industry" : industry, "country" : country, "totalEmployees" : totalEmployees, "connections" : allCompanyConnections}

if __name__ == '__main__':
    html_extract = main(link)
