from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import login_details

def enabled(soup):
    nextButtonName = "artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"
    nextButton = soup.find_all('class', nextButtonName)[0]
    print(nextButton)
    if 'disabled' in nextButton:
        return False;
    return True;
    
def main(browser, link):
    browser.get(link)
    

    print('\nScraping your connections...\n')
    i = 2
    connections = {}
    connections["names"] = []
    connections["links"] = []
    while True:
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        if enabled(soup):
            for profile in soup.find_all('a', class_='app-aware-link',href=True):
                if 'View' in profile.text:
                    name = profile.text.strip().partition("View")[0];
                    print(name)
                    connections["names"].append(name)
                    connections["links"].append(profile['href'])
            browser.get(link + '&page='+str(i))
            i+=1
            time.sleep(3)
        else:
            break
        
    return connections


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com/uas/login")
# entering username
username = driver.find_element(By.ID, "username")

# Enter Your Email Address
username.send_keys(login_details.email)  
  
# entering password
pword = driver.find_element(By.ID, "password")

# Enter Your Password
pword.send_keys(login_details.password)

# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

link = "https://www.linkedin.com/search/results/people/?currentCompany=%5B%223807149%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=%3A!-"

item = main(driver, link)

print(item)
##if __name__ == '__main__':
##    html_extract = main(browser)
