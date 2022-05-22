################################################################################
##Read me for formatting requirements (IMPORTANT)
##
##The connections that you want to find of are stored in a dictionary
##
##{"Name of Connection" : "Their URL code"}
##
##In the event of failure to find any connections, use returnCompanyConnectionsNotFound()
##to return a blank dictionary
################################################################################

import pandas as pd


def returnRequiredConnections():
    col_list = ["name", "url_code"]
    df = pd.read_csv("inputs/reqCon.csv", usecols=col_list).set_index('name')

    return df['url_code'].to_dict()

def returnCompanyConnectionsNotFound():
    conn = returnRequiredConnections();

    for person in conn:
        conn[person] = [];
    return conn
