import streamlit as st
import pandas as pd
import os
import pickle
from preprocess import Preprocess

class Prediction_file:

    def __init__(self) -> None:
        pass

    def Predict(self):

        # st.title('Titanic Ship Survival Prediction')

        # st.header('Making prediction using uploaded file')

        # with open(os.path.join('models','rfc_model.pkl'),'rb') as f:
        #     model = pickle.load(f)

        # uploaded_file = st.file_uploader("Choose a file")

        # uploaded_file_metadata = st.expander("Checkout the csv file specification needed for predictions")

        # uploaded_file_metadata.markdown("""
        #     **1. csv file should have these columns: Pclass, Sex, Age, SibSp (Siblings aboard), Parch (Parents/children aboard), and Fare.**
        # """)
        # uploaded_file_metadata.markdown("""
        #     **2. Sex field should have two fields namely male and female.**
        # """)
        # uploaded_file_metadata.markdown("""
        #     **3. Features named Age and Fare should have float values.**
        # """)
        # uploaded_file_metadata.markdown("""
        #     **4. All the other fields should be non-negative integers.**
        # """)

        # predict_btn_df = st.button("Predict Survival")


        
        # if predict_btn_df:
        #     with st.spinner('Wait for it...'):
        #         if uploaded_file is not None:
        #             df = pd.read_csv(uploaded_file,encoding='utf-16')
        #             process = Preprocess()
        #             process.encoding_sex_feature(df)
        #             if predict_btn_df:
        #                 df_prediction = model.predict(df)

        #                 st.write("Survival Prediction:")
        #                 st.write(df_prediction)

        #                 @st.cache
        #                 def convert_df(df):
        #                     # IMPORTANT: Cache the conversion to prevent computation on every rerun
        #                     return df.to_csv().encode('utf-16')

        #                 csv = convert_df(df_prediction)

        #                 st.download_button(
        #                     label="Download predictions as CSV",
        #                     data=csv,
        #                     file_name='large_df.csv',
        #                     mime='text/csv',
        #                 )

        # ABOVE DATA IS COMMENTED DUE TO DECODING ERROR

        st.header("Admin is resolving some issue. Please try again after some time...")

        
if __name__ == '__main__':

    p = Prediction_file()
    p.Predict()