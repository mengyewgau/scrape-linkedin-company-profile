### Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
### Classes
import login_details

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