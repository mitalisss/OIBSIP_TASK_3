import streamlit as st
import numpy as np
import joblib

model=joblib.load("C:/Users/mital/OneDrive/Desktop/oasis internship/CAR_PRICE/car_price_model")

st.title("CAR PRICE PREDICTION")
st.write("ENTER DETAILS")

YEAR =st.text_input("YEAR OF MANUFACTURING: ")
PRICE  = st.text_input('PRICE: ') 
KM =st.text_input('DRIVEN KM: ')
FUEL=st.text_input(" FUEL TYPE : PETROL:0 , DISEL:1 , CNG:2")
SELL=st.text_input('Selling_type: Dealer:0 ,Individual:1')
TRANS=st.text_input('Transmission: Manual:0, Automatic:1')
OWN=st.text_input(" OWNER:")




def predict():
    # Convert input data to appropriate types
    row = [int(YEAR), float(PRICE), int(KM), int(FUEL), int(SELL), int(TRANS), int(OWN)]
    input_data_as_numpy_array = np.asarray(row)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    predictions = model.predict(input_data_reshaped)
    
    # Store result in session state as a list
    st.session_state['result'] = predictions.tolist()

# Predict button
st.button("Predict", on_click=predict)

# Display the result at the bottom
if 'result' in st.session_state:
    st.write(f"## SELLING PRICE IS {st.session_state['result'][0]}")