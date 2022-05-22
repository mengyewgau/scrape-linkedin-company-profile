import csv_functions as cf

def details():
    try:
        loginDetails = cf.read_csv('inputs/login.csv')
        return {"email" : loginDetails[0], "password" : loginDetails[1]};
    except:
        raise Exception("Fill in your email and password in login.csv")        

def main():
    pass

if __name__ == '__main__':
    main()


