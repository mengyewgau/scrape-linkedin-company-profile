import pandas as pd

def convert(d):
    df = pd.DataFrame(d)
    return df.transpose()


