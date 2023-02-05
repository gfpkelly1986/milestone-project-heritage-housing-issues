import numpy as np
import pandas as pd
import streamlit as st
from src.data_management import load_original_no_nan_data, load_inherited_houses, load_pkl_file
from src.machine_learning.predict_sales_price import predict_inherited_sale_price
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_predict_sale_price_body():

    version = 'v1'

    df_inherited = load_inherited_houses()

    predict_sale_price_model = load_pkl_file("outputs/ml_pipeline/predict_sale_price/v1/deploy_pca_pipeline.pkl")


    st.write("### Predict House Sale Price")

    st.info(f"- The client has inherited 4 properties in Ames, Iowa."
            f" She wants to maximize her sale price on these 4 inherited houses.\n"
            f"- The model used to predict sale price uses 'principal component analysis'.\n"
            f"- It has explained 92.05% of the variance in the data using just 2 components\n"
            f"- This model satisfies Business Requirement 2.\n"
            f"\n")

    st.write("---")

    if st.checkbox("Click to view the 'Inherited Houses' dataset"):
        st.write(df_inherited)

    st.write("---")

    st.write(f"- Run the predicton button below to view the models prediction for the four inherited houses")

    X_live = df_inherited
    

    if st.button("Run Predictive Analysis"):
        predicted_price = predict_inherited_sale_price(X_live, predict_sale_price_model)
    
    
    




