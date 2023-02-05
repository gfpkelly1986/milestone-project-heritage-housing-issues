import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"- **Client:** *Lydia Doe* \n\n"
        f"- Lydia has received an inheritance from a deceased great-grandfather. Included in the inheritance are four houses located in Ames, Iowa, USA.\n\n"
        f" - Lydia has a poor knowledge of the property market in Iowa and wants a model to predict likely *Sale Price* values for the four properties\n\n"
        f"**Original Dataset: ** The original data can be found at this link: [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)\n"
        f" - **Features in DataSet: ** There were 23 features to consider in this dataset at the outset of the project.\n\n"
        f" - **Target: ** The target variable for this project is '*SalePrice*' "
        f" - **Quantity of data: ** There were 1460 rows of data in the table which was analyzed."
    )

    st.write("---")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/gfpkelly1986/milestone-project-heritage-housing-issues).")
    
    st.write("---")
    
    st.success(
        f"**The project has 2 business requirements:**\n"
        f"- Business Requirement 1:- The client is interested in discovering how the house attributes correlate with the sale price.\n "
        f"- Business Requirement 2: - The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa."
        )

        

