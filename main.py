from googlesearch import search   
import csv
import scraper as dataScraper

def main(): 
    links = []
    file = open("linkedins.csv", encoding = "utf8")

    csvreader = csv.reader(file)
    for row in csvreader:
        if len(row) == 0:
            links.append("Blank")
        else:
            links.append(row[0])
        
    
    uncleanedData = dataScraper.main(links)
    #Write data for industry
    industry = uncleanedData["industry"]
    write_csv(industry, "industry")
    #Write data for countries
    country = uncleanedData["country"]
    write_csv(country, "country")
    #Write data for employees
    employees = uncleanedData["totalEmployees"]
    write_csv(employees,"employees")


    # Convert the dictionary to a pandas dataframe

    allCompanyConnections = uncleanedData["connections"]

    for co in allCompanyConnections:
        print(co)
    
    
def write_csv(data, filename):
    
    # PreCon: Data must be a list, filename MUST be a string
    with open(filename+".csv", "w", encoding = "utf8") as f:
        for line in data:
            f.write("%s\n"%line)



if __name__ == '__main__':
    html_extract = main()
