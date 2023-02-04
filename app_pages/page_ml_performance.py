import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from src.data_management import load_original_no_nan_data, load_pkl_file
from src.machine_learning.evaluate import regression_performance, regression_evaluation

def page_model_performance_body():

    version = 'v1'

    df_clean_full = load_original_no_nan_data()

    predict_sales_pipeline = load_pkl_file("outputs/ml_pipeline/predict_sale_price/v1/deploy_pca_pipeline.pkl")

    actual_vs_prediction_plots = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/GBR-train-test-plots2.png")

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv").values

    st.write("### Model Performance - Model Understanding")

    st.info(f"- This model used Principal Component Analysis with 2 components\n"
            f"- It explained 92.05% of the variance in the data with these components\n"
            f"- The R2 score for the Train and Test sets are 0.871 and 0.844\n"
            f"- \n")

    st.write("---")
    st.write(f"- The Pipeline used for this model is shown below:\n")
    st.write(predict_sales_pipeline)
    st.write("---")
    st.write(f"- The precise features the model worked with to achieve its performance are unknown as principal component analysis was used.\n")
    st.write("---")

    st.write("### Pipeline Performance")

    regression_performance(X_train=X_train, y_train=y_train, X_test=X_test,
                            y_test=y_test, pipeline=predict_sales_pipeline)

    st.write(f"- Plot showing actual vs predicted outcomes for both Train and Test sets shown below:\n")
    st.image(actual_vs_prediction_plots)

    st.write('TO DO: Add more interpretations/evaluations')
