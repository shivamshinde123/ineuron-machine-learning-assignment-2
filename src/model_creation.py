from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from preprocess import Preprocess 
import pickle
import json
import os
from sklearn.metrics import roc_auc_score, confusion_matrix


class ModelCreation:

    def __init__(self) -> None:
        pass

    def model_creation(self):
        
        ## reading the processed data
        df = pd.read_csv('processed_data/processed_data.csv')

        X, y = Preprocess().separating_dependent_and_independent_features(df)

        X_train, X_test, y_train, y_test = Preprocess().train_and_test_split(X,y)

        ## creating a module
        rfc = RandomForestClassifier(max_depth=3,n_jobs=-1,random_state=2397)

        ## fitting the model
        rfc_model = rfc.fit(X_train, y_train)

        ## saving the model
        if not os.path.exists('models'):
            os.makedirs('models')
        
        with open(os.path.join('models','rfc_model.pkl'),'wb') as f:
            pickle.dump(rfc_model,f)


        ## evaluating the model on the test data and then saving the metrics
        roc_auc = roc_auc_score(y_test, rfc_model.predict_proba(X_test)[:, 1])
        conf_matrix = confusion_matrix(y_test, rfc_model.predict(X_test))

        if not os.path.exists('metrics'):
            os.makedirs('metrics')

        with open(os.path.join('metrics','roc_auc_score.json'), 'w') as f:
            json.dump(roc_auc, f)

        # with open(os.path.join('metrics','confusion_matrix.pkl'), 'w') as f:
        #     pickle.dump(conf_matrix, f)

        pd.DataFrame(conf_matrix).to_csv(os.path.join('metrics','confusion_matrix.csv'),index=False)


if __name__ == '__main__':
    mr = ModelCreation()

    mr.model_creation()
