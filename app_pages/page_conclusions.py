import streamlit as st
import os


def page_conclusions_body():

    st.write("### Project Conclusions")

    st.success(" - **Results:** Both models predict 'Sale Price'\
                  values within approximately 5 to 10 per cent\
                  of each other if you set the 5 input widgets \
                  to have the same values as the properties \
                  contained in the inherited houses dataframe.\n"
            "This leads me to believe that both models are accurate\
                  to within 10 percent of the realised Sale Prices.")

    st.success(" - **Strengths and Limitations: ** I believe both models\
                  suffer from some slight overfitting, which is \
                  reflected in the error values and that a larger\
                  dataset to Train a new model with would help to \
                  improve their accuracy. 10 per cent of $678,000\
                  is 67,800 which may be too large of a discrepency over\
                  the total 'Sale Price' for 4 houses. Our ideal outcome\
                  was set out at +-0.05% of the realised Sale Price. \
                  A larger data sample could help reduce this to more \
                  acceptable levels.\n")

    st.success("- **The Business Requirements** have been satisfied\
                  by the project. Both models score over 0.8 for \
                  both the Train and Test sets of data.")

    st.write("---")
