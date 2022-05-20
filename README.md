# scrape-linkedin-company-for-connections

## Libraries Used
1. Selenium 
2. Webdriver_manager.chrome
3. Beautiful Soup
4. Time
5. csv


## Data Requirements
Company linkedin profile should minimally be valid with Industry, Country, Num of Employees, and connections


## Supported functionalities
1. Industry appears in industry.csv - None types appear as No Industry Found
2. Same for country - country.csv
3. Same for Num of employees - employees.csv
4. Connections of desired employees - connections.csv


## User Guide
1. Store your linkedin profiles in a linkedins.csv file
2. Save it in the same directory as all the program files
3. The output csv files will be found in the results folder
4. Fill in your linkedin login details in login_details.py

## FAQ
**Q:** I would like to change the names of the connections whom I want to scrape


**Answer:** 
- Create an csv file called reqCon.csv. Under the 2 columns names and url_code, append respectively. Make sure there are **_no commas_**.
- Google how to check url_code for connection of a person


**Q:** What program to run to update the code


**Answer:**   Main.py




### Screenshots
<img src='screenshots/reqconexample.png' >
<img src='screenshots/logindetailsformat.png' >