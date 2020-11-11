import streamlit as st

from src.data.load import load_sklearn_object

def main_interface():
    # Add Streamlit title, descriptions and load an image
    st.title('Diabetes Prediction App')
    st.write('The data for the following example contains information on females at least 21 years old. This is a sample application and cannot be used as a substitute for real mediacl advice.')


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
        feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

        model = load_sklearn_object("RandomForestClassifier.pkl")

def launch():
    """
    Main function to launch all functionalities of Streamlit    
    """

    #TODO READ FEATURE ENGINNERING PICKLE FILE
    model = load_sklearn_object("RandomForest.pkl")

    try:
        main_interface()
        side_menu()
        return True
    except:
        print('Error')
        return False