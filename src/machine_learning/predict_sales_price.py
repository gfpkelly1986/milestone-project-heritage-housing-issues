
import pandas as pd
import streamlit as st
import numpy as np

def predict_inherited_sale_price(X_live, pipeline):

    # Drop House Choice here: Also The inherited data could be engineered in the notebooks to remove the other variables
    X_live = X_live.drop(['House Choice', 'EnclosedPorch', 'WoodDeckSF'], axis=1)
    
    # predict
    prediction = pipeline.predict(X_live)

    # Acess the model for further elaboration!
    regressor = pipeline.named_steps['model']
    train_score = regressor.train_score_
    
    statement = (
            f"- These are the 4 predictions for the clients inherited houses: \n"
        )
    
    st.write(statement)
    st.write(prediction)
    st.write(train_score)