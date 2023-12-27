"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('autism_dataset.csv')

    
    

    # Perform feature and target split
    X = df[["Genetics","Prenatal_Factors","Environmental_Factors","Parental_Age","Birth_Complications","Immune_System","Neurological_Factors","Gastrointestinal_Issues","Sensory_Processing","Epigenetic_Factors","Nutritional_Factors","Hormonal_Factors","Neurotransmitter_Function","Social_Environment","Autism_Pregnancy","Parental_Health","Autoimmune_Disorders","Inflammation","Sleep_Disorders","Metabolic_Factors","Unknown_Factors"]]
    y = df['Result']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score
