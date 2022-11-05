import numpy as np
import os


class Preprocess:


    def __init__(self):
        pass

    def remove_useless_columns(self,df):

        df.drop(columns=['PassengerId','Name','Ticket','Cabin','Embarked'],axis=1,inplace=True)

        return df

    def getting_num_and_cat_features(self,df):

        num_feat = ['Fare','Age']

        cat_feat = [feature for feature in df.columns if feature not in num_feat]

        return num_feat, cat_feat

    def missing_values_imputation(self,df):

        num_feat, cat_feat = self.getting_num_and_cat_features(df)

        for feature in num_feat:
            df[feature].fillna(np.mean(df[feature]),inplace=True)

        for feature in cat_feat:
            df[feature].fillna(np.mode(df[feature]), inplace=True)

        return df

    def encoding_sex_feature(self,df):
        
        mapping_dict = {'male':0, 'female':1}

        df['Sex'].map(mapping_dict)

        df.to_csv(os.path.join('processed_data','processed_data.csv'),columns=df.columns,index=False)




if __name__ == '__main__':

    process = Preprocess()
    process.remove_useless_columns()
    process.missing_values_imputation()
    process.encoding_sex_feature()