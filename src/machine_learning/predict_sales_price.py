import pandas as pd
import streamlit as st
import numpy as np

def predict_inherited_sale_price(X_live, pipeline):

    X_live = X_live.drop(
        ['House Choice', 'EnclosedPorch', 'WoodDeckSF'], axis=1)

    prediction = pipeline.predict(X_live)

    regressor = pipeline.named_steps['model']
    num_features = regressor.n_features_in_

    st.write("\n\n\n\n")
    st.write('---')
    st.write("- **These are the 4 predictions for \
                   the clients inherited houses:** \n")
    st.write(prediction)
    st.write(f"- **The number of features used to train\
                    this model was: {num_features}.**")
    st.write('---')

    house_a = prediction[0].round(2)
    house_b = prediction[1].round(2)
    house_c = prediction[2].round(2)
    house_d = prediction[3].round(2)
    total = house_a + house_b + house_c + house_d
    st.success("### Predicted Sale Prices:\n\n"
            f"House A Predicted SalePrice:\
                **${house_a:,}**\n\n"
            f"House B Predicted SalePrice:  \
                **${house_b:,}**\n\n"
            f"House C Predicted SalePrice:  \
                **${house_c:,}**\n\n"
            f"House D Predicted SalePrice:  \
                **${house_d:,}**\n\n"
            f"The Total predicted value of all the \
                inherited properties comes to: \
                **${total:,}**")


def predict_generalised_sale_price(X_live, pipeline):
    regressor = pipeline.named_steps['model']
    num_features = regressor.n_features_in_

    prediction = pipeline.predict(X_live)

    st.write("---")
    total = int(prediction)

    st.success("### Predicted Sale Price for a Property\
                in Ames Iowa With the Selected Inputs:\n\n"
                f" **${total:,}**")

    st.write("---")
