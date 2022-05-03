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
    industry = []
    country = []
    employees = [] 
    for item in range(0,len(uncleanedData),3):
        industry.append(uncleanedData[item])
    for item in range(1,len(uncleanedData),3):
        country.append(uncleanedData[item])
    for item in range(2,len(uncleanedData),3):
        employees.append(uncleanedData[item])

    write_csv(industry, "industry")
    write_csv(country, "country")
    write_csv(employees,"employees")
    print(uncleanedData)
def write_csv(data, filename):
    
    # PreCon: Data must be a list, filename MUST be a string
    with open(filename+".csv", "w", encoding = "utf8") as f:
        for line in data:
            f.write("%s\n"%line)



if __name__ == '__main__':
    html_extract = main()
