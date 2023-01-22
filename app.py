import streamlit as st
from app_pages.multipage import MultiPage

# ADD AND ORDER PAGES THAT YOUR DASHBOARD WILL CONTAIN!

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_project_hypothesis_body
from app_pages.page_correlation import page_correlation_body
from app_pages.page_predict_sale_price import page_predict_sale_price_body
from app_pages.page_ml_performance import page_model_performance_body

app = MultiPage(app_name= "Heritage Housing Issues") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Quick Project Summary", page_summary_body)
app.app_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.app_page("Correlation Analysis", page_correlation_body)
app.app_page("Predict House Sale Price", page_predict_sale_price_body)
app.app_page("Model Performance", page_model_performance_body)


app.run() # Run the  app