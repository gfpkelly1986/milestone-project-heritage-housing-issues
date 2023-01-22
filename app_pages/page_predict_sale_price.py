import plotly.express as px
import numpy as np
import pandas as pd
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_original_no_nan_data, load_inherited_houses, load_pkl_file
from src.machine_learning.predict_sales_price import predict_inherited_sale_price
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_predict_sale_price_body():

    version = 'v1'

    df_clean_full = load_original_no_nan_data()
    df_inherited = load_inherited_houses()

    house_a = df_inherited.iloc[[0]]
    house_b = df_inherited.iloc[[1]]
    house_c = df_inherited.iloc[[2]]
    house_d = df_inherited.iloc[[3]]

    predict_sale_price_model = load_pkl_file("outputs/ml_pipeline/predict_sale_price/v1/deploy_pca_pipeline.pkl")

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv").values

    st.write("### Predict House Sale Price")

    st.info(f"- The client has inherited 4 properties in Ames, Iowa."
            f" She wants to maximize her sale price on these 4 inherited houses.\n"
            f"- The model used to predict sale price uses 'principal component analysis'.\n"
            f"- It has explained 92.05% of the variance in the data using just 2 components\n"
            f"- This model satisfies Business Requirement 2.\n"
            f"\n")

    st.write("---")

    if st.checkbox("Inherited"):
        st.write(df_inherited)

    if st.checkbox("cleaned"):
        st.write(df_clean_full.head(2))

    if st.checkbox("A"):
        st.write(house_a)

    st.write("---")
    st.write(df_inherited.columns)
    st.write("---")



    X_live = df_inherited
    

    if st.button("Run Predictive Analysis"):
        predicted_price = predict_inherited_sale_price(X_live, predict_sale_price_model)
    


def inherited_houses_dropdown():

    df_inherited = load_inherited_houses()

    house_a = df_inherited.iloc[[0]]
    house_b = df_inherited.iloc[[1]]
    house_c = df_inherited.iloc[[2]]
    house_d = df_inherited.iloc[[3]]

    X_live = pd.DataFrame([], index=[0])

    option = st.selectbox("Choose one of the houses to make a prediction on its Sale Price",
    ('House A', 'House B', 'House C', 'House D'))

    if option == 'House A':
        X_live = X_live.append(house_a)
    
    return X_live


