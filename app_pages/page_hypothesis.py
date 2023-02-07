import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"- **Hypothesis A:** Overall quality, greater square footage, and greater number of bedrooms will correlate with the target variable 'SalePrice' more than other features.\n"
        f"- **Hypothesis B:** Few features/components will be required to predict SalePrice.\n\n"
        f"- **Hyothesis C:** Modern spacious houses will have a higher probability of  fetching a high 'SalePrice'\n\n"
        f"- Houses tend to have key drivers in the final sale price. Size and overall quality should stand out as features of concern. \n")
    st.success(
        f" - **Validation A**: Hypothesis A is validated by the Spearman and Pearson correlation test results on the following dashboard page.Further plots on the correlation analysis page show validation for hypothesis A.\n\n"
        
        f"- The final sale price for House D of $205,047.07 when the predictive analysis performed is further validation for hypothesis A.\n"
        f"  - This house is the second largest in the set by just 25sqf at 1604sqf, but has a higher overall quality rating of '6'.\n\n"
        f"  - House C on the other hand is predicted to sell for $191,163.13. It is larger than House A and B but has an overall quality rating of 5."
        f"- Further validation for hypothesis A is seen by comparing House B to House A. \n"
        f"  - House B is larger, has more bedrooms, and a higher overall quality rating and is predicted to sell for $150,922.03"
        f"  - House A is smaller, has only 2 bedrooms and has a quality rating of 5. It has the lowest predicted sale price of $131,855.70. \n\n\n"
        f" - **Validation B**: Validation for hypothesis B is seen by both the PCA analysis and the correlation analysis.\n"
        f"The correlation analysis shows strong correlation between large houses of good quality and final sale price. The PCA analysis reduced the dataset from 23 features to two.\n\n"
        f"- **Validation C:** Validation for this hypothesis can be seen by viewing the numerous scatterplotplots on the correlation analysis page showing correlation between new properties,"
        f"greater square footage, better quality and the eventual 'SalePrice'."
    )