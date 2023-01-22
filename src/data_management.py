import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_original_no_nan_data():
    df = pd.read_csv("outputs/datasets/collection/original_no_nan.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_further_analysis():
    df = pd.read_csv("outputs/datasets/collection/further_analysis.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_houses():
    df = pd.read_csv("outputs/datasets/collection/inherited.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)