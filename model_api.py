import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load your pre-trained model
model = load_model('celestial_classification_model.h5')

# Define the feature names (these should correspond to your model's expected input)
feature_names = [
    'ra', 'dec', 'u', 'g', 'r', 'i', 'z',
    'run', 'camcol', 'field', 'specobjid',
    'redshift', 'plate', 'mjd', 'fiberid'
]

# Streamlit app layout

st.set_page_config(
    page_title="Astronomical Object Classifier",  # Change this to your desired title
    page_icon="🌌",  # Optional: Change this to your desired favicon
    layout="wide"    # Optional: Set the layout to 'wide' or 'centered'
)




st.title("Astronomical Object Classifier\n")
st.write("Welcome to the Astronomical Classification App!")
st.write("Explore the universe by predicting whether your chosen features correspond to a star, quasar, or galaxy. Adjust the sliders to customize the input values and discover the wonders of celestial objects!")
st.write('\n\n\n\n')

#Mapping features
feature_mapping = {
    "ra": "Right Ascension Coordinate",
    "dec": "Declination Coordinate",
    "u": "u Band",
    "g": "g Band",
    "r": "r Band",
    "i": "i Band",
    "z": "z Band",
    "run": "Run Number",
    "camcol": "Camera Column",
    "field": "Field Number",
    "specobjid": "Spectroscopic Object ID",
    "redshift": "Redshift",
    "plate": "Plate Number",
    "mjd": "Modified Julian Date of Observation",
    "fiberid": "Fiber ID"
}

# Create a list to store feature values
features = []

# Create sliders for each feature using the descriptive names
for var_name, desc_name in feature_mapping.items():
    if var_name in ['run', 'camcol', 'field', 'specobjid', 'plate', 'fiberid']:                # Assuming these are integers
        value = st.slider(desc_name, min_value=0, max_value=1000, value=500, step=1)           # Adjust ranges as needed
    else:  # For the others, use float sliders
        value = st.slider(desc_name, min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    features.append(value)
    



# Convert the features list to a numpy array and reshape for the model
try:
    input_data = np.array(features, dtype=float).reshape(1, -1)
except ValueError as e:
    st.error(f"Error converting features to float: {e}")
    st.stop()
st.markdown("___")
# Make prediction when the button is pressed
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        class_labels = ['Star', 'Quasar', 'Galaxy']
        predicted_class = class_labels[np.argmax(prediction)]

        st.write(f"The predicted class is: **{predicted_class}**")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
