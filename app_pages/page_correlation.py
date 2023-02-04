import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_original_no_nan_data, load_further_analysis
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_correlation_body():

    spearman_results = plt.imread(f"jupyter_notebooks/images/analysis-images/Spearmans-full-set.png")
    
    pearson_results = plt.imread(f"jupyter_notebooks/images/analysis-images/Pearsons-full-set.png")

    st.write('### Correlation Analysis')

    df_no_nan = load_original_no_nan_data()
    df_further_analyis = load_further_analysis()

    if st.checkbox("Original Data Sample"):
        st.write(
            f"* The dataset has {df_no_nan.shape[0]} rows and {df_no_nan.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df_no_nan.head(10))

    st.write("### Correlation Analysis")
    st.info(
        f"- The client is interested in discovering how the various attributes of the house correlate with the final sale price.\n"
        f" - Visualisations in the form of plots have been provided to help with understanding the analysis which was carried out.\n"
        f" - This analysis satisfies Business Requirement 1.\n"
    )

    st.write("---")

    st.info(f"#### **What analysis was carried out:**\n"
            f" - Categorical variables were one hot encoded.\n"
            f" - Spearman and Pearson correlation analysis was performed on this cleaned dataset.\n"
            f" - Both tests showed 'Overall Quality' as the most correlated vaiable with Sale Price\n"
            f" - This variable is influenced by other variables in the data. This is visualised below.\n"
            f" - Select the checkboxes below to view these plots and understand the correlations")

    st.write("---")
    st.write('Spearman Correltation Test Results')
    st.image(spearman_results)
    st.write('Pearson Correlation Test Results')
    st.image(pearson_results)
    st.write("---")

    if st.checkbox("How 'Overall Quality' of the property correlates with SalePrice"):
        plot_correlation_overall_qual_sale_price(df_further_analyis)
        st.write(f"This box plot shows how strong the correlation is between overall quality ratings between 8 and 10 and the eventual sale price.\n"
                f"There are very few outliers in the negative direction in this group.\n"
                f"The interquartile range of category 10 is the highest and largest of the plot.\n")

    if st.checkbox("How 'Kitchen Quality' affects 'Overall Quality' which correlates with Sale Price"):
        plot_correlation_overall_qual_sale_price_hue_by_kitchen_qual(df_further_analyis)
        st.write(f"This vertical viloin plot shows how few houses with a kitchen quality rating of TA(Typical,Average) managed a decent sale price.\n"
                f"Category 8 shows this particularly well.\n"
                f"The overall quality was high but the sale price has a negative correlation with kitchen quality.\n"
                f"There is a general jump in sale price when kitchen quality is excellent to compliment the overall house condition, although there are outliers.\n")

    if st.checkbox("How 'Overall Quality' (X axis) is correlated with size/area which correlates with higher Sale Price"):
        plot_overall_qual_property_area_sale_price(df_further_analyis)
        st.write("Bigger houses tend to be newer, of better overall quality and correlates with higher Sale Price.")

    if st.checkbox("Modern houses are more spacious, are higher quality and correlates with higher Sale Price"):
        plot_modern_house_sale_price_hue_overall_qual(df_further_analyis)
        st.write("Modern houses showing correlation with sale price. Modern houses seem to have greater space and better finishes and thus a greater sale price.")

    if st.checkbox("Spacious houses are more common in modern builds, which correlates with higher Sale Price"):
        plot_modern_house_sale_price_hue_overall_qual(df_further_analyis)
        st.write("The above plot shows a greater number of larger houses after about 1970. This correlates with higher sale price.")

    if st.checkbox("How 'Kitchen Quality' is correlated with other features which correlate with SalePrice"):
        plot_correlation_sale_price_kitchen_qual_overall_qual(df_further_analyis)



def plot_correlation_sale_price_kitchen_qual_overall_qual(df):
    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 5))
    fig.suptitle("Kitchen quality influences overall Sale Price by affecting the Overall Quality")
    sns.countplot(data=df, x='KitchenQual',ax=ax1)
    sns.scatterplot(data=df, x='KitchenQual', y='SalePrice', hue='OverallQual',ax=ax2)
    sns.scatterplot(data=df, x='KitchenQual', y='SalePrice', hue='GrLivArea',ax=ax3)
    sns.scatterplot(data=df, x='KitchenQual', y='SalePrice', hue='GarageArea',ax=ax4)
    plt.tight_layout()
    st.pyplot(fig)


def plot_correlation_overall_qual_sale_price(df):
    fig = plt.figure(figsize=(20, 10))
    fig.suptitle("Overall quality is heavily correlated with Sale Price")
    sns.boxplot(data=df, x='OverallQual', y='SalePrice')
    st.pyplot(fig)


def plot_correlation_overall_qual_sale_price_hue_by_kitchen_qual(df):
    fig = plt.figure(figsize=(20, 10))
    fig.suptitle("Coloring Overall Quality and Sale Price by Kitchen Quality")
    sns.violinplot(data=df, x=df['OverallQual'], y=df['SalePrice'], hue='KitchenQual')
    st.pyplot(fig)


def plot_overall_qual_property_area_sale_price(df):
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 5))
    fig.suptitle("How 'Overall Quality' correlates with property area which correlates to high 'Sale Price'")
    axes[0].set_title('SalePrice')
    axes[0].bar(data=df, x="OverallQual", height='SalePrice')
    axes[1].set_title('GrLivArea')
    axes[1].bar(data=df, x="OverallQual", height='GrLivArea')
    axes[2].set_title('GarageArea')
    axes[2].bar(data=df, x="OverallQual", height='GarageArea')
    axes[3].set_title('TotalBsmtSF')
    axes[3].bar(data=df, x="OverallQual", height='TotalBsmtSF')
    st.pyplot(fig)


def plot_modern_house_sale_price_hue_overall_qual(df):
    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,7))
    fig.suptitle("Modern houses have a better Overall Quality")
    sns.scatterplot(data=df, x='YearRemodAdd', y='SalePrice', hue='OverallQual', ax=ax1)
    sns.scatterplot(data=df, x='YearBuilt', y='SalePrice', hue='OverallQual', ax=ax2)
    st.pyplot(fig)


def plot_modern_house_sale_price_hue_1stFlrSF(df):
    fig =  plt.figure(figsize=(15,5))
    fig.suptitle("Modern houses are more spacious, leading to better Sale Price")
    sns.scatterplot(data=df, x='YearBuilt', y='SalePrice', hue='1stFlrSF')
    st.pyplot(fig)

