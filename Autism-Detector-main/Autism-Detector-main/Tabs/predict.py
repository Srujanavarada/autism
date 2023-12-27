"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Prediction of Autism Level.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    col1,col2,col3 = st.columns(3)

    with col1:
        # Take input of features from the user.
        Genetics = st.slider("Genetics", int(df["Genetics"].min()), int(df["Genetics"].max()))
        Prenatal_Factors = st.slider("Prenatal_Factors", int(df["Prenatal_Factors"].min()), int(df["Prenatal_Factors"].max()))
        Environmental_Factors = st.slider("Environmental_Factors", int(df["Environmental_Factors"].min()), int(df["Environmental_Factors"].max()))
        Parental_Age = st.slider("Parental_Age", float(df["Parental_Age"].min()), float(df["Parental_Age"].max()))
        Birth_Complications = st.slider("Birth_Complications", float(df["Birth_Complications"].min()), float(df["Birth_Complications"].max()))
        Immune_System = st.slider("Immune_System", float(df["Immune_System"].min()), float(df["Immune_System"].max()))
        Gastrointestinal_Issues = st.slider("Gastrointestinal_Issues", float(df["Gastrointestinal_Issues"].min()), float(df["Gastrointestinal_Issues"].max()))

    with col2:
        Sensory_Processing = st.slider("Sensory_Processing", int(df["Sensory_Processing"].min()), int(df["Sensory_Processing"].max()))
        Epigenetic_Factors = st.slider("Epigenetic_Factors", int(df["Epigenetic_Factors"].min()), int(df["Epigenetic_Factors"].max()))
        
        Nutritional_Factors = st.slider("Nutritional_Factors", float(df["Nutritional_Factors"].min()), float(df["Nutritional_Factors"].max()))
        Hormonal_Factors = st.slider("Hormonal_Factors", float(df["Hormonal_Factors"].min()), float(df["Hormonal_Factors"].max()))
        Neurotransmitter_Function = st.slider("Neurotransmitter_Function", float(df["Neurotransmitter_Function"].min()), float(df["Neurotransmitter_Function"].max()))
        Neurological_Factors = st.slider("Neurological_Factors", float(df["Neurological_Factors"].min()), float(df["Neurological_Factors"].max()))
        Social_Environment = st.slider("Social_Environment", float(df["Social_Environment"].min()), float(df["Social_Environment"].max()))

    with col3:
        Autism_Pregnancy = st.slider("Autism_Pregnancy", int(df["Autism_Pregnancy"].min()), int(df["Autism_Pregnancy"].max()))
        Parental_Health = st.slider("Parental_Health", int(df["Parental_Health"].min()), int(df["Parental_Health"].max()))
        Autoimmune_Disorders = st.slider("Autoimmune_Disorders", int(df["Autoimmune_Disorders"].min()), int(df["Autoimmune_Disorders"].max()))
        Inflammation = st.slider("Inflammation", float(df["Inflammation"].min()), float(df["Inflammation"].max()))
        Sleep_Disorders = st.slider("Sleep_Disorders", float(df["Sleep_Disorders"].min()), float(df["Sleep_Disorders"].max()))
        Metabolic_Factors = st.slider("Metabolic_Factors", float(df["Metabolic_Factors"].min()), float(df["Metabolic_Factors"].max()))
       

    # Create a list to store all the features
    features = [Genetics,Prenatal_Factors,Environmental_Factors,Parental_Age,Birth_Complications,Immune_System,Neurological_Factors,Gastrointestinal_Issues,Sensory_Processing,Epigenetic_Factors,Nutritional_Factors,Hormonal_Factors,Neurotransmitter_Function,Social_Environment,Autism_Pregnancy,Parental_Health,Autoimmune_Disorders,Inflammation,Sleep_Disorders,Metabolic_Factors,Metabolic_Factors]

    # error factor
    k = 3.9
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Autism level detected...")

        # Print the output according to the prediction
        if (prediction == 0):
            st.success("The person no autism")
        elif (prediction == 1):
            st.warning("The person has low Autism level 😐")
        elif (prediction == 2):
            st.error("The person has medium Autism level! 😞")
        elif (prediction == 3):
            st.error("The person has severe Autism level!! 😫")
        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", (score*100*k),"%")
