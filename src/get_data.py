import pandas as pd


class GetData:


    def __init__(self):
        pass

    def get_data(self):

        url = "https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv"

        df = pd.read_csv(url)

        return df


        
        