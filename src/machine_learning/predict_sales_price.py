
#     ****-------------- Rewrite logic to predict sale price from inherited set of data  --------------------****

def predict_tenure(X_live, tenure_features, tenure_pipeline, tenure_labels_map):

    # from live data, subset features related to this pipeline
    X_live_tenure = X_live.filter(tenure_features)

    # predict
    tenure_prediction = tenure_pipeline.predict(X_live_tenure)
    tenure_prediction_proba = tenure_pipeline.predict_proba(X_live_tenure)
    # st.write(tenure_prediction_proba)

    # create a logic to display the results
    proba = tenure_prediction_proba[0, tenure_prediction][0]*100
    tenure_levels = tenure_labels_map[tenure_prediction[0]]

    if tenure_prediction != 1:
        statement = (
            f"* In addition, there is a {proba.round(2)}% probability the prospect "
            f"will stay **{tenure_levels} months**. "
        )
    else:
        statement = (
            f"* The model has predicted the prospect would stay **{tenure_levels} months**, "
            f"however we acknowledge that the recall and precision levels for {tenure_levels} is not "
            f"strong. The AI tends to identify potential churners, but for this prospect the AI is not "
            f"confident enough on how long the prospect would stay."
        )

    st.write(statement)