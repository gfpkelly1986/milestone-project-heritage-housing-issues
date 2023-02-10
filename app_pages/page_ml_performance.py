import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate import regression_performance


def page_model_performance_body():

    predict_sales_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_sale_price/v1/deploy_pca_pipeline.pkl")
    predict_general_house_sale_prices = load_pkl_file(
        "outputs/ml_pipeline/predict_sale_price/v3/deploy_extratrees_pipeline.pkl")

    actual_vs_prediction_plots = plt.imread(
        "outputs/ml_pipeline/predict_sale_price/v1/GBR-train-test-plots2.png")

    extra_trees_plots = plt.imread(
        "outputs/ml_pipeline/predict_sale_price/v3/ExtraTreesRegressor-Plots.png")

    extra_trees_feature_importance = plt.imread(
        "outputs/ml_pipeline/predict_sale_price/v3/Feature-Importance.jpg")

    X_train = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v1/X_train.csv")
    X_test = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v1/X_test.csv")
    y_train = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v1/y_train.csv").values
    y_test = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v1/y_test.csv").values

    X_train2 = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v3/X_train.csv")
    X_test2 = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v3/X_test.csv")
    y_train2 = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v3/y_train.csv").values
    y_test2 = pd.read_csv(
        "outputs/ml_pipeline/predict_sale_price/v3/y_test.csv").values

    st.write("### Model Performance - Model Understanding")

    st.info("- This model used Principal Component Analysis \
               with 2 components\n"
            "- It explained 92.05% of the variance in the \
               data with these components\n"
            "- The R2 score was used as a performance metric\
               for this model. Values above 0.8 for train and\
               test sets were deemed acceptable.\n"
            "- The R2 score for the Train and Test sets are \
               0.879 and 0.857 respectively.\n")

    st.write("---")
    st.info("- This ML Pipeline was used for predicting \
               the Sale Price of the 4 inherited houses\n"
            "- The exact features the model used to achieve \
               its performance are unknown as principal \
               component analysis was used.\n")

    st.write(predict_sales_pipeline)
    st.info("- This ML Pipeline was used for predicting\
               the General House Sale Prices of houses \
               in Ames Iowa.\n"
            "- The PCA pipeline was trained on all \
               features where this pipeline uses only 5.\n"
            "- This allowed me to have a cleaner dashboard\
               on the *Predict House Sale Price* page")

    st.write(predict_general_house_sale_prices)

    st.write("---")
    st.write()
    st.write("---")

    st.write("### Pipeline Performance PCA")

    regression_performance(
        X_train=X_train, y_train=y_train,
        X_test=X_test, y_test=y_test,
        pipeline=predict_sales_pipeline)

    st.write("- Plot showing actual vs predicted \
                outcomes for both Train and Test \
                sets shown below:\n")

    st.image(actual_vs_prediction_plots)

    st.success("- When a regression line is plotted correctly, \
                  about half of the data points will be above \
                  the line and the other half will be below \
                  the line.\n\n"
               "- The plots above show that both the Train\
                   and Test sets are performing well."
               "This is confirmed by the R2 score above")

    st.write("### Pipeline Performance ExtraTreesRegressor")

    regression_performance(
        X_train=X_train2, y_train=y_train2,
        X_test=X_test2, y_test=y_test2,
        pipeline=predict_general_house_sale_prices)

    st.write("- Plot showing actual vs predicted \
                outcomes for both Train and Test \
                sets shown below:\n")

    st.image(extra_trees_plots)

    st.write("---")
    st.write("- The features the ExtraTreesRegressor model\
                was trained on and their importance.")
    st.write(X_train2.columns.to_list())
    st.image(extra_trees_feature_importance)
