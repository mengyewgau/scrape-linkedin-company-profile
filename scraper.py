#############################
### LinkedIn Data Scraper ###
#############################


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import login_details


def main(linkedins):

    # Open the driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://linkedin.com/uas/login")

    # entering username
    username = driver.find_element_by_id("username")

    # Enter Your Email Address
    username.send_keys(login_details.email)  
      
    # entering password
    pword = driver.find_element_by_id("password")

    # Enter Your Password
    pword.send_keys(login_details.password)

    # Clicking on the log in button
    # Format (syntax) of writing XPath --> 
    # //tagname[@attribute='value']
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)
    result = {}
    result["industry"] = []
    result["country"] = []
    result["employees"] = []
    
    for company in linkedins:
        if company == "Blank":
            result["industry"].append("No Industry");
            result["country"].append("No Country");
            result["employees"].append("No Employee Information");
            continue;
        
        driver.get(company)
        start = time.time()
          
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            # this command scrolls the window starting from
            # the pixel value stored in the initialScroll 
            # variable to the pixel value stored at the
            # finalScroll variable
            initialScroll = finalScroll
            finalScroll += 1000
          
            # we will stop the script for 3 seconds so that 
            # the data can load
            time.sleep(3)
            # You can change it as per your needs and internet speed
          
            end = time.time()
            # We will scroll for 20 seconds.
            # You can change it as per your needs and internet speed
            if round(end - start) > 15:
                break
          
        # Scrape the lxml page for the data we need
        src = driver.page_source

        soup = BeautifulSoup(src, 'lxml')
        intro = soup.find('div', {'class': "ph5 pt3"})
        try:  
            items = intro.find_all("div", {'class': 'org-top-card-summary-info-list__info-item'})
            result["industry"].append(items[0].get_text().strip().replace(",", ";"))
        except:
            result["industry"].append("No Industry");
        try:
            result["country"].append(items[1].get_text().strip().replace(",", ";"))
        except:
            result["country"].append("No Country");
        try:
            employees = intro.find("span", {'class': "org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state"})
            result["employees"].append(employees.get_text().strip().replace(",",""))
        except:
            result["employees"].append("No Employee Information");



        
    driver.quit()
    return result
if __name__ == '__main__':
    html_extract = main(link)
