# Housing Heritage Issues.

### Predictive model for the sale of house prices in Ames, Iowa

<p href="#intro" id="intro"> - Intended Purpose of This Project:
Complete an intro for this project.
</p>

## Table of contents
- <a href="#dc">Dataset Content</a>
- <a href="#br">Business Requirements</a>
- <a href="#hy">Hypothesis and how to validate?</a>
- <a href="#rt">The rationale to map the business requirements to the Data Visualizations and ML tasks</a>
- <a href="#ml">ML Business Case</a>
- <a href="#dd">Dashboard Design</a>
- <a href="#wf">Wireframe of Dashboard</a>
- <a href="#dep">Deployment</a>
- <a href="#tu">Technologies Used</a>
- <a href="#bu">Bugs</a>
- <a href="#cr">Credits</a>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dc"></p>

## Dataset Content

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="br"></p>

## Business Requirements

- Business Requirement 1:

    - The client is interested in discovering how the house attributes correlate with the sale price.
    
    Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.

- Business Requirement 2:

    - The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="hy"></p>

## Hypothesis and how to validate?

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="rt"></p>

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- Business Requirement 1:

    - Perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price.

    - Visualize these variables against the sale price, so you can summarize the insights.

- Business Requirement 2:

    - Deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses and houses in this area.

    - Use either conventional ML or Neural Networks to map the relationships between the features and the target.

    - Note: consider changing the ML task from Regression to Classification if you find a valid rationale for that.

        - Evaluating the the r2 score/business requirement success definition will determine this.

    - Conduct an extensive hyperparameter optimization for a given algorithm.

        - Refer to the Scikit-learn lesson, Unit Notebook 6: Cross-Validation Search Part 2.

            - At the end of the notebook, you will find a list of hyperparameter options and values to start with, for the family of algorithms we covered in the course.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ml"></p>

## ML Business Case

- Understand Correlation between house attributes and the resulting sale price.

- This section relates to the models used.

    - We want an ML model to: Target variable is: 
    - Our ideal outcome is
    - The model success metrics are
    - The output is defined as
    - Heuristics if any
    - The training data to fit the model comes from: 
        - This dataset contains:

- Prdeict house prices in the Ames, Iowa area.

- This section relates to the models used.

    - We want an ML model to: Target variable is: 
    - Our ideal outcome is
    - The model success metrics are
    - The output is defined as
    - Heuristics if any
    - The training data to fit the model comes from: 
        - This dataset contains:

- If clustering or further models were necessary document them here.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dd"></p>

## Dashboard Design for Project 5

**What will the dashboard need to have and what business requirements are being met?**

- Page 1

    - Section 1:

    - Summary Page: 

    - Explain and validate the project hypothesis

    - Summarise the project. Terminology used. Who and what are being studied and why. What was the initial business requirement?

    - Where the dataset was sourced: Link out to the read me files.

    - Section 2:

    - What were the business requirements for the creation of this dashboard solution? What is it that this ML project is going to solve for the customer?

- Page 2

    - Section 1:

    - Document Initial study of the data.

    - Show sample of data.

    - Section 2:

    - What techniques were used to understand the data.

    - Show plots of the data analysis and understanding phase of CRISP_DM to demonstrate how the understanding was arrived at.

- Page 3

    - Section 1:

    - Predictive Analysis Correlation:

    - How the various features in the data correlated with the resulting house price.

    - Plots will be required to demonstrate which features influenced the target sale price the most.

    - These are the house attributes like location and bedroom quantity etc.

    - Note Here:

    - Important to thoroughly evaluate the performance of the numerical/regression model.

    - If the target R2 score is not met other avenues must be explored to achieve model performance!

- Page 4

    - Section 1:

    - Predictive Analysis Correlation:

    - Provide a deployed working model that will predict the price of the 4 inherited houses and any inherited houses in the area.

    - ToDo: How will this look? How will this be achieved?



<p>

A project summary page, showing the project dataset summary and the client's requirements.

A page listing your findings related to which features have the strongest correlation to the house sale price.

A page displaying the 4 houses' attributes and their respective predicted sale price.

It should display a message informing the summed predicted price for all 4 inherited houses.

You should add interactive input widgets that allow a user to provide real-time house data to predict the sale price.

A page indicating your project hypothesis(es) and how you validated it across the project.

A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.

<p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="wf"></p>

## Wireframe of Dashboard.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dep"></p>

## Deployment of a Streamlit Application

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

## Technologies Used

- Libraries and Packages Used for this Machine Learning Project.

    - Library Name
        - Specific ecample on how this library was used.

    - Library Name
        - Specific ecample on how this library was used.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="bu"></p>

## Bugs

- Live Bugs

- Solved Bugs
    - Deployment error:
        - Changed Python version from python-3.8.15 to python-3.8.16 as suggested by Niel_CI to
        
            eliminate the error of Heroku-Stack-22 being incompatible with the python version which was installed after forking the repository. 
         
            Python version: python-3.8.16 is the version used by Heroku-20.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="cr"></p>

## Credits

- Credit any external code

- Credit code institute code
