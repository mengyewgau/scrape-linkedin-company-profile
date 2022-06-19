import csv
import scraper as dataScraper
import convertDict
import pathlib

# Modules
import csv_functions as cf

def main(): 
    links = []
    
    file = open("inputs/linkedins.csv", encoding = "utf8")

    csvreader = csv.reader(file)
    for row in csvreader:
        if len(row) == 0:
            links.append("Blank")
        else:
            links.append(row[0])
        
    
    uncleanedData = dataScraper.main(links)
    #Write data for industry
    industry = uncleanedData["industry"]
    cf.write_csv(industry, "industry")
    #Write data for countries
    country = uncleanedData["country"]
    cf.write_csv(country, "country")
    #Write data for employees
    employees = uncleanedData["totalEmployees"] 
    cf.write_csv(employees,"employees")


    # Convert the dictionary to a pandas dataframe
    allCompanyConnections = uncleanedData["connections"]
    print(allCompanyConnections)
    df = convertDict.convert(allCompanyConnections)
    connPath = pathlib.Path('results/connections.csv')
    df.to_csv(connPath)



if __name__ == '__main__':
    html_extract = main()





