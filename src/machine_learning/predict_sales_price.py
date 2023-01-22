
import pandas as pd
import streamlit as st

def predict_inherited_sale_price(X_live, pipeline):

    # Drop House Choice here: Also The inherited data could be engineered in the notebooks to remove the other variables
    X_live = X_live.drop(['House Choice', 'EnclosedPorch', 'WoodDeckSF'], axis=1)
    
    # predict
    prediction = pipeline.predict(X_live)
    
    statement = (
            f"* Test\n"
            f"Test"
        )
    
    st.write(statement)
    st.write(prediction)