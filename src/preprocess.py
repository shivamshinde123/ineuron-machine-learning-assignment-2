import numpy as np
import os
import json
from get_data import GetData
from sklearn.model_selection import train_test_split


class Preprocess:


    def __init__(self):
        pass

    def getting_num_and_cat_features(self,df):

        num_feat = ['Fare','Age']

        cat_feat = [feature for feature in df.columns if feature not in num_feat]

        return num_feat, cat_feat

    def separating_dependent_and_independent_features(self,df):

        X = df.drop('Survived',axis=1)
        y = df['Survived']

        return X, y

    def train_and_test_split(self,X,y):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32490,stratify=y)

        return X_train, X_test, y_train, y_test

    def remove_useless_columns(self,df):

        df.drop(columns=['PassengerId','Name','Ticket','Cabin','Embarked'],axis=1,inplace=True)

        return df

    def missing_values_imputation(self,df):

        num_feat, cat_feat = self.getting_num_and_cat_features(df)

        for feature in num_feat:
            df[feature].fillna(np.mean(df[feature]),inplace=True)

        for feature in cat_feat:
            df[feature].fillna(df[feature].mode(), inplace=True)

        return df

    def encoding_sex_feature(self,df):
        
        mapping_dict = {'male':0, 'female':1}

        if not os.path.exists('encoding_info'):
            os.makedirs('encoding_info')
        
        with open(os.path.join('encoding_info','encoding_dict.json'),'w') as f:
            json.dump(mapping_dict,f)

        df['Sex'] = df['Sex'].map(mapping_dict)

        if not os.path.exists('processed_data'):
            os.makedirs('processed_data')

        df.to_csv(os.path.join('processed_data','processed_data.csv'),columns=df.columns,index=False)




if __name__ == '__main__':

    process = Preprocess()
    df = GetData().get_data()
    df = process.remove_useless_columns(df)
    df = process.missing_values_imputation(df)
    process.encoding_sex_feature(df)