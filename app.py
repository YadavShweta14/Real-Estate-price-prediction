import pandas as pd
import pickle as pk
import streamlit as st

model=pk.load(open('D:\\Realstatepricepredictor\\House_prediction_model.pkl','rb'))

st.header('Real Estate Price Prediction')
data = pd.read_csv('D:\\Realstatepricepredictor\\Cleaned_data1.xls')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter No of Bedrooms')
bath= st.number_input('Enter No of Bathrooms')
balc = st.number_input('Enter No of Balcony')


input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button("Predict Price"):
    output = model.predict(input)
    price_in_rupees=output[0] *100000
    #formatted_price= f"{price_in_rupees:,.2f}"
    formatted_price = f"{price_in_rupees:,.2f}"
    out_str = f"Price of the house is {formatted_price}"
    st.success(out_str)
