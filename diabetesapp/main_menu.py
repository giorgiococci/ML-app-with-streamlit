import streamlit as st
import pandas as pd
from PIL import Image

from src.data.load import load_sklearn_object
from src.features.transform import feature_engineering
from src.model.prediction import prediction

def main_interface():
    # Add Streamlit title, descriptions and load an image
    st.title('Diabetes Prediction App')
    st.write('The data for the following example contains information on females at least 21 years old. This is a sample application and cannot be used as a substitute for real mediacl advice.')

    image = Image.open('static/diabetes_prevention.png')
    st.image(image, use_column_width=True)

    st.write('Please fill in the details of the the person under consideration in the left sidebar and click on the button below!')


def side_menu():
    """
    Streamlit side menu configuration
    """

    age =           st.sidebar.number_input("Age in Years", 1, 150, 25, 1)
    pregnancies =   st.sidebar.number_input("Number of pregnancies", 0, 20, 0, 1)
    glucose =       st.sidebar.slider("Glucose Level", 0, 200, 25, 1)
    skinthickness = st.sidebar.slider("Skin Thickness", 0, 99, 20, 1)
    bloodpressure = st.sidebar.slider("Blood Pressure", 0, 122, 69, 1)
    insulin =       st.sidebar.slider("Insulin", 0, 846, 79, 1)
    bmi =           st.sidebar.slider("BMI", 0.0, 67.1, 31.4, 0.1)
    dpf =           st.sidebar.slider("Diabetes Pedigree Function", 0.000, 2.420, 0.471, 0.001)

    row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

    if(st.button('Find Health Status')):
        print('Button clicked!')
        feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

        feature_trasformation = load_sklearn_object("featureTransformations.pkl")
        model = load_sklearn_object("RandomForestClassifier.pkl")

        # Create the Dataframe
        features = pd.DataFrame([row], columns = feat_cols)

        # Feature Engineering
        data = feature_engineering(feature_trasformation, features)

        # Prediction
        predictions = prediction(model, data)

        if(predictions[0] == 0):
            st.write("This is a healthy person!")
        else:
            st.write("This person has high chances of having diabetes!")


def launch():
    """
    Main function to launch all functionalities of Streamlit    
    """

    try:
        main_interface()
        side_menu()
        return True
    except:
        print('Error')
        return False