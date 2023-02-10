import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.success("- **Hypothesis A:** Overall quality, greater square footage, \
                    and greater number of bedrooms will correlate \
                    with the target variable 'SalePrice' more than \
                    other features.\n"
               "- **Hypothesis B:** Few features/components will \
                    be required to predict SalePrice.\n\n"
               "- **Hyothesis C:** Modern spacious houses will have a \
                    higher probability of fetching a high 'SalePrice'\n\n"
               "- Houses tend to have key drivers in the final sale price.\n"
               "Size and overall quality should stand out as \
                features of concern.\n")
    st.success(" - **Validation A**: Hypothesis A is validated \
                    by the Spearman and Pearson correlation test \
                    results on the following dashboard page.\
                    Further plots on the correlation analysis page \
                    show validation for hypothesis A.\n\n"
               "- The final sale price for House D of $205,047.07 \
                    when the predictive analysis performed is \
                    further validation for hypothesis A.\n"
               "  - This house is the second largest in the \
                    set by just 25sqf at 1604sqf, but has a \
                    higher overall quality rating of '6'.\n\n"
               "  - House C on the other hand is predicted to \
                    sell for $191,163.13. It is larger than \
                    House A and B but has an overall quality \
                    rating of 5."
               "- Further validation for hypothesis A \
                    is seen by comparing House B to House A.\n"
               "  - House B is larger, has more bedrooms, \
                    and a higher overall quality rating and \
                    is predicted to sell for $150,922.03"
               "  - House A is smaller, has only 2 bedrooms\
                    and has a quality rating of 5. It has \
                    the lowest predicted sale price of \
                    $131,855.70. \n\n\n"
               " - **Validation B**: Validation for \
                    hypothesis B is seen by both the \
                    PCA analysis and the correlation analysis.\n"
               "The correlation analysis shows strong correlation \
                    between large houses of good quality and final \
                    sale price. The PCA analysis reduced the \
                    dataset from 23 features to two.\n\n"
               "- **Validation C:** Validation for this hypothesis \
                    can be seen by viewing the numerous \
                    scatterplotplots on the correlation analysis \
                    page showing correlation between new properties,\
                    greater square footage, better quality and the \
                    eventual 'SalePrice'.")
