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
########################################################################################################

## Libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time
## Classes
import requiredConnections

# Returns a list of dictionaries
def main(browser, link):
    requiredSuffix = requiredConnections.returnRequiredConnections();
    

    # Takes the person's name as the key, list of their connections as the value
    result = {}
    peopleLinks = {}
    
    for person in requiredSuffix:
        # Second, we look at Person Specific connection
##        print(person + " " + requiredSuffix[person]) # Debug
        suffix = requiredSuffix[person]
        peopleLinks[person] = addConnectionsLevel(link, suffix)
    print('\nScraping your connections...\n')
    for person in peopleLinks:
        print(person + "'s connections are:")
        personLink = peopleLinks[person]

        # Store the person's connections in a dictionary - result
        result[person] = scrape(browser, personLink)
        
    return result

# scrape(browser, link) is the main scraper function. It only works for one person in
# the required connection at a time
def scrape(browser, link):
    browser.get(link)
    # Stores employeeNames and profileLinks of connectionsOf person
    connections = []
    
    # Process the first page
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    pageNum = 2

    # Check if there are 1st and 2nd degree connections
    totalResults = test(soup)
    if totalResults == False:
        return connections;
    # If there are, scrape them
    canFindConnection = True
    while True:
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        # If no results found, break
        noFound = soup.find('h2', class_ = 'artdeco-empty-state__headline artdeco-empty-state__headline--mercado-empty-room-small artdeco-empty-state__headline--mercado-spots-small')
        if (noFound) and noFound.text.strip() == "No results found":
            break
        for profile in soup.find_all('a', class_='app-aware-link',href=True):        
            if 'View' in profile.text:
                name = profile.text.strip().partition("View")[0];
                print(name) # Printing to ensure the function is running correctly
                connections.append(name + " - " + profile['href'])
        
        # Check search has completed, and number of results tally
        if len(connections) == totalResults:
            break
        # Continue the search
        browser.get(link + '&page='+str(pageNum))
        pageNum += 1
        time.sleep(3)
    
    return connections



######### Less Important Functions ############################################################################################################################################
# addConnectionsLevel(link) takes in a link, and appends the 1st and 2nd degree connections suffix
def addConnectionsLevel(link, conn):
    linkUpdated = ""
    index = 0
    while index < len(link):
        if (index + 6 < len(link)) and (link[index:index+6] == "people"):
            degreeConnections = "/?connectionOf=" + conn + "&"
            linkUpdated = linkUpdated + link[index:index+6] + degreeConnections
            index += 8

        else:
            linkUpdated = linkUpdated + link[index]
            index += 1
    return linkUpdated

# test(soup) takes in a soup object, and test if there are any search results
def test(soup):
    try:
        totalResults = int(soup.find("h2", class_ = 'pb2 t-black--light t-14').text.strip().split()[0]);
        return totalResults;
    except:
        return False
