import pandas as pd
import streamlit as st


@st.cache_data
def load_data(file):
    df = pd.read_csv(file, encoding='latin1')

    # Convert date column
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    return df
