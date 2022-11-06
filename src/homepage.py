import streamlit as st

def app():

    st.title("Titanic ship accident survival prediction")

    st.header("Some background about the dataset used to train the machine learning model")

    st.markdown("""
        The sinking of the Titanic is one of the most infamous shipwrecks in history.
        On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.
        While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.
        The aim of the project is to predict the survival given the input from the user.
    """)

    st.markdown("""
        **Use the sidebar options to provide the inputs for the prediction.**
    """)

app()