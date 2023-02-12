import pandas as pd
import streamlit as st
from src.data_management import load_original_no_nan_data
from src.data_management import load_inherited_houses
from src.data_management import load_pkl_file
from src.machine_learning.predict_sales_price import predict_inherited_sale_price
from src.machine_learning.predict_sales_price import predict_generalised_sale_price
import seaborn as sns
sns.set_style("whitegrid")


def page_predict_sale_price_body():

    df_inherited = load_inherited_houses()

    predict_sale_price_model = load_pkl_file(
        "outputs/ml_pipeline/predict_sale_price/v1/deploy_pca_pipeline.pkl")

    predict_generalised_sale_price_model = load_pkl_file(
        "outputs/ml_pipeline/predict_sale_price/v3/deploy_extratrees_pipeline.pkl")

    st.write("### Predict House Sale Price")

    st.info("- The client has inherited 4 properties\
               in Ames, Iowa."
            " She wants to maximize her sale price \
               on these 4 inherited houses.\n"
            "- The model used to predict sale price \
               uses 'principal component analysis'.\n"
            "- It has explained 92.05% of the variance \
               in the data using just 2 components\n"
            "- This model satisfies Business Requirement 2.\n"
            "\n")

    st.write("---")

    if st.checkbox("Click to view the 'Inherited Houses' dataset"):
        st.write(df_inherited)

    st.write("---")

    st.info("- Run the predicton button below to view \
        the models prediction for the four inherited houses")

    X_live = df_inherited

    if st.button("Run Predictive Analysis for \
                    Business Requirement 2 (A)"):
        predicted_price = predict_inherited_sale_price(
            X_live, predict_sale_price_model)

    st.write("---")

    X_live2 = DrawInputsWidgets()

    st.info("- Adjust the widgets and run the predicton\
               button below to view the  models prediction \
               for general houses in the Ames area.")

    if st.button("Run Predictive Analysis for \
                  Business Requirement 2 (B)"):
        predicted_price = predict_generalised_sale_price(
            X_live2, predict_generalised_sale_price_model)


def DrawInputsWidgets():
    df = load_original_no_nan_data()

    col1, col2, col3, = st.beta_columns(3)
    col4, col5, col6,  = st.beta_columns(3)

    X_Live2 = pd.DataFrame([], index=[0])

    with col1:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].mean())
        )
    X_Live2[feature] = st_widget

    with col2:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].mean())
        )
    X_Live2[feature] = st_widget

    with col3:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].median())
        )
    X_Live2[feature] = st_widget

    with col4:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=1,
            max_value=10,
            value=5
        )
    X_Live2[feature] = st_widget

    with col5:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].mean())
        )
    X_Live2[feature] = st_widget

    return X_Live2
