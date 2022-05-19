### DOCUMENTATION ######################################################################################
##
##1. main(browser, link)
##- Browser is the selenium webdriver with LinkedIn logged in
##- Link is the hyperlink of the company search page, without connections nor page number
##
##2. Requirements
##- If the company linkedin page has no connections to view, this function SHOULD not be called
##- If called, this results in an errorneous delay, kill program and rerun it
##
##3. Output
##- Returns a dictionary of employeeNames and the profile profileLinks
##- If no connections, it returns an empty dictionary
########################################################################################################

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requiredConnections

def main(browser, link):
    requiredSuffix = requiredConnections.returnRequiredConnections(link)

    for person in requiredSuffix:
        link = 
    
    browser.get(link)
    print('\nScraping your connections...\n')

    # Process the first page
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    pageNum = 2

    # Check if there are 1st and 2nd degree connections. Return if none
    totalResults = test(soup)
    if totalResults == False:
        return {"employeeNames" : [], "profileLinks" : []};

    employeeNames = []
    profileLinks = []
    while True:
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for profile in soup.find_all('a', class_='app-aware-link',href=True):
            if 'View' in profile.text:
                name = profile.text.strip().partition("View")[0];
                print(name) # Printing to ensure the function is running correctly
                employeeNames.append(name)
                profileLinks.append(profile['href'])
        
        # Check search has completed, and number of results tally
        if len(employeeNames) == totalResults:
            break
        # Continue the search
        browser.get(link + '&page='+str(pageNum))
        pageNum += 1
        time.sleep(3)
        
        
    return {"employeeNames" : employeeNames, "profileLinks" : profileLinks};

# addConnectionsLevel(link) takes in a link, and appends the 1st and 2nd degree connections suffix
def addConnectionsLevel(link, conn):
    linkUpdated = ""
    for index in range(0, len(link)):
        if (index + 6 < len(link)) and (link[index:index+6] == "poeple"):
            degreeConnections = "/?connectionOf=" + conn + "&"
            linkUpdated = linkUpdated + degreeConnections + link[index]
        else:
            linkUpdated = linkUpdated + link[index]
    return linkUpdated

# test(soup) takes in a soup object, and test if there are any search results
def test(soup):
    try:
        totalResults = int(soup.find("h2", class_ = 'pb2 t-black--light t-14').text.strip().split()[0]);
        return totalResults;
    except:
        return False

    
if __name__ == '__main__':
    html_extract = main(browser, link)
