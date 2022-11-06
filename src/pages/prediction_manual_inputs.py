import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from preprocess import Preprocess

class Prediction_file:

    def __init__(self) -> None:
        pass

    def Predict(self):

        st.title('Titanic Ship Survival Prediction')

        st.header('Making prediction using manually provided feature values')

        with open(os.path.join('models','rfc_model.pkl'),'rb') as f:
            model = pickle.load(f)

        input_from_user = []

        pclass_input = st.radio("Pclass",(1,2,3))

        sex_input = st.radio("Sex",(0,1))
        st.markdown("""
            **Note: Male sex is represented using 0 and female sex is represented by 1.**
        """)

        age_input = st.number_input('Age',0.0,90.0,30.0,0.1)

        SibSp_input = st.number_input('SibSp',0,8,1)

        Parch_input = st.number_input('Parch',0,8,1)

        Fare_input = st.number_input('Fare',value= 300.0, step= 0.1)

        input_from_user.append(pclass_input)
        input_from_user.append(sex_input)
        input_from_user.append(age_input)
        input_from_user.append(SibSp_input)
        input_from_user.append(Parch_input)
        input_from_user.append(Fare_input)

        input = np.array(input_from_user).reshape(1,-1)

        predict_btn = st.button("Predict Survival")

        if predict_btn:
            with st.spinner('Wait for it...'):
                st.write("Survival Prediction:")
                s_prediction = model.predict(input)
                st.write(s_prediction)

        st.markdown("""
            **Note:**
        """)
        st.markdown("""
            **1 - Person Survived**
        """)
        st.markdown("""
            **0 - Person did not Survive**
        """)


if __name__ == '__main__':

    p = Prediction_file()
    p.Predict()