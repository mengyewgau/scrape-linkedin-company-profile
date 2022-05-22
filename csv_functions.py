import pathlib
import csv

def write_csv(data, filename):
    
    fPath = pathlib.Path('results/' + filename + ".csv")
    if fPath.exists() == False:
        fPath.parent.mkdir(parents=True, exist_ok=True) 

    # PreCon: Data must be a list, filename MUST be a string
    with open(fPath, "w", encoding = "utf8") as f:
        for line in data:
            f.write("%s\n"%line)

def read_csv(pathName):

    fPath = pathlib.Path(pathName)
    with open(fPath, "r", encoding = "utf-8-sig") as f:
        try:
            reader = csv.reader(f, delimiter = ",")
            results = []
            for row in reader:
                results.append(row[0]);

            # Debugging 
            assert (len(list(results)) > 0), "File has no lines to read"
            return results;
        except AssertionError as msg:
            print(msg)
        
def main():
    pass

if __name__ == '__main__':
    main()
