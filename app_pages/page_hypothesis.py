import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"- **Hypothesis A:** Overall quality, greater square footage, and greater number of bedrooms will correlate with the target variable 'SalePrice' more than other features.\n"
        f"- **Hypothesis B:** Few features/components will be required to predict SalePrice.\n\n"

        f"- Houses tend to have key drivers in the final sale price. Size and overall quality should stand out as features of concern. \n"

        f" - **Complete this page.\n**"
    )