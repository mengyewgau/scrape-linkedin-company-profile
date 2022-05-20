# scrape-linkedin-company-for-connections

## Currently, the program only supports the retrieval of Industry and Home Country

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
4. Connections of desired employees implemented! 


## FAQ
**Q:** I would like to change the names of the connections whom I want to scrape
**Answer:** 
- Create an csv file called reqCon.csv. Under the 2 columns made below, append the name of the connection, and their url_code.
- Google how to check url_code for connection of a person
![reqcon.png](..\screenshots\reqcon.png)





