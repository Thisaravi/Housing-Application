import streamlit as st
import joblib
import pandas as pd

import numpy as np


price_model = joblib.load('house_price_model2.pkl')
preprocessor = joblib.load('preprocessor.pkl')
rentalmarket_segmentation_model = joblib.load('Market_Segment2.pkl')
scaler=joblib.load('scaler2.pkl')
encoder=joblib.load('encoder.pkl')
#rentaffordability_model = joblib.load('rent_affordability_model.pkl')

main_regions = [
    'San Francisco Bay Area','Los Angeles', 'New York City',
    'Chicago', 'Houston','Dallas / Fort Worth','Miami',
    'Atlanta','Boston','Washington, DC','Las Vegas','Denver',
    'Seattle','San Diego','Phoenix','Philadelphia','Detroit',
    'Minneapolis / St Paul','Austin','Orlando','Tampa Bay Area',
    'Sacramento','Portland','Charlotte','Raleigh / Durham',
    'Nashville','San Antonio','Salt Lake City','Kansas City',
    'Cleveland','Pittsburgh','St Louis','Indianapolis','Baltimore','New Orleans',
    'Milwaukee','Cincinnati','Columbus','Oklahoma City','Tulsa', 'Richmond',
    'Memphis','Buffalo','Albuquerque','Honolulu','reno / tahoe'
]

types=['apartment', 'condo', 'house', 'duplex', 'townhouse',
       'manufactured', 'flat', 'loft', 'in-law', 'cottage/cabin', 'land',
       'assisted living']

laundryoptions=['w/d in unit', 'w/d hookups', 'laundry on site',
       'no laundry on site', 'laundry in bldg']

parking=['carport', 'attached garage', 'off-street parking',
       'detached garage', 'street parking', 'no parking', 'valet parking']

states=['ca', 'co', 'ct', 'dc', 'fl', 'de', 'ga', 'hi', 'id', 'il', 'in',
       'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'nc',
       'mo', 'mt', 'ne', 'nv', 'nj', 'nm', 'ny', 'nh', 'oh', 'nd', 'ok',
       'or', 'pa', 'ri', 'sc', 'tn', 'sd', 'tx', 'ut', 'va', 'vt', 'wa',
       'wv', 'wi', 'wy', 'al', 'ak', 'az', 'ar']

import base64




def set_background_image(image_file):
    with open(image_file, "rb") as f:
      encoded_image = base64.b64encode(f.read()).decode()
    
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{encoded_image}");
    background-size: cover;
    background-size: cover;
    
    

     }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)



st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    'Select a Page:',
    ('Home', 'Price Prediction','Market Segmentation','Rent Affordability')
)

#----------------------------------------------------------------home---------------------------------------------------------------
if option == 'Home':
    set_background_image('dark.jpg')
    st.title("Welcome to the USA Housing Prediction App")
    st.markdown('<div class="blurred-div">', unsafe_allow_html=True)
    st.write("Select options from the menu to get started.")
    st.write("About Us")
    st.write("""
Our machine learning-powered app helps customers and property sellers in the USA housing market by predicting key factors such as rental prices, affordability, and market segmentation.
Whether you're looking to price a property or evaluate its affordability for renters, our tool provides insightful predictions to help you make informed decisions. Tailored for both buyers and sellers, the app is designed to offer accurate and actionable real estate insights.
""")
   
    
    
elif option == 'Price Prediction':
    set_background_image('usa.jpg')
    st.title("House Price Prediction")
    st.write("Please fill out the details below to get the predicted price.")
  

   
    col1, col2 = st.columns(2)


    with col1:
        region = st.selectbox('Region', main_regions)
        sqfeet = st.number_input('Square Feet', min_value=100, max_value=10000, value=1200)
        beds = st.number_input('Number of Beds', min_value=0, max_value=10, value=2)
        cats_allowed = st.selectbox('Cats Allowed', [0, 1])
        wheelchair_access = st.selectbox('Wheelchair Access', [0, 1])
        laundry_options = st.selectbox('Laundry Options', laundryoptions)
        

    with col2:
        type_of_house = st.selectbox('Type of House', types)
        baths = st.number_input('Number of Baths', min_value=0, max_value=10, value=2)
        dogs_allowed = st.selectbox('Dogs Allowed', [0, 1])
        electric_vehicle_charge = st.selectbox('Electric Vehicle Charge', [0, 1])
        comes_furnished = st.selectbox('Comes Furnished', [0, 1])
        parking_options = st.selectbox('Parking Options', parking)
        
        state = st.selectbox('State', states)

   
    if st.button('Predict Price'):
       
        new_data = {
            'region': [region],
            'type': [type_of_house],
            'sqfeet': [sqfeet],
            'beds': [beds],
            'baths': [baths],
            'cats_allowed': [cats_allowed],
            'dogs_allowed': [dogs_allowed],
            'wheelchair_access': [wheelchair_access],
            'electric_vehicle_charge': [electric_vehicle_charge],
            'comes_furnished': [comes_furnished],
            'laundry_options': [laundry_options],
            'parking_options': [parking_options],
           
            'state': [state]
        }
        
       
        new_data_df = pd.DataFrame(new_data)
        
       
        new_data_processed = preprocessor.transform(new_data_df)
        
       
        predicted_price = price_model.predict(new_data_processed)

       
        st.markdown(f"""
    <div style='border: 2px solid #2c2e30; padding: 10px; border-radius: 10px; background-color:#2c2e30; display: inline-block;'>
        <h2 style='font-size:24px;'>The predicted price is: ${predicted_price[0]:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

       
  
#----------------------------------------------------------------Market Segmentation---------------------------------------------------------------
elif option == "Market Segmentation":
    set_background_image('usa1.jpg')
    st.header("Market Segmentation Prediction")


    col1, col2 = st.columns(2)

    
    with col1:
        region = st.selectbox('Region', main_regions)
        sqfeet = st.number_input('Square Feet', min_value=100, max_value=10000, value=1200)
        beds = st.number_input('Number of Beds', min_value=0, max_value=10, value=2)
        cats_allowed = st.selectbox('Cats Allowed', [0, 1])
        wheelchair_access = st.selectbox('Wheelchair Access', [0, 1])
        laundry_options = st.selectbox('Laundry Options', laundryoptions)
        

    with col2:
        type_of_house = st.selectbox('Type of House', types)
        baths = st.number_input('Number of Baths', min_value=0, max_value=10, value=2)
        dogs_allowed = st.selectbox('Dogs Allowed', [0, 1])
        electric_vehicle_charge = st.selectbox('Electric Vehicle Charge', [0, 1])
        comes_furnished = st.selectbox('Comes Furnished', [0, 1])
        parking_options = st.selectbox('Parking Options', parking)
        state = st.selectbox('State', states)

 
    if st.button("Predict Market Segment"):
     
        input_data = {
            'region': region,
            'type': type_of_house,
            'sqfeet': sqfeet,
            'beds': beds,
            'baths': baths,
            'cats_allowed': 1 if cats_allowed == "Yes" else 0,
            'dogs_allowed': 1 if dogs_allowed == "Yes" else 0,
            'wheelchair_access': 1 if wheelchair_access == "Yes" else 0,
            'electric_vehicle_charge': 1 if electric_vehicle_charge == "Yes" else 0,
            'comes_furnished': 1 if comes_furnished == "Yes" else 0,
            'laundry_options': laundry_options,
            'parking_options': parking_options,
         
            'state': state
        }

       
        input_df = pd.DataFrame([input_data])
        numerical_features = ['sqfeet', 'beds', 'baths', 'cats_allowed', 'dogs_allowed', 
                      'wheelchair_access', 'electric_vehicle_charge', 'comes_furnished']
        categorical_features = ['region', 'type', 'laundry_options', 'parking_options', 'state']

        new_data_num_scaled = scaler.transform(input_df[numerical_features])
        new_data_cat_encoded = encoder.transform(input_df[categorical_features]) 
        new_data_transformed = np.hstack([new_data_num_scaled, new_data_cat_encoded])
        predicted_segment = rentalmarket_segmentation_model.predict(new_data_transformed)
        st.markdown(f"""
    <div style='border: 2px solid #2c2e30; padding: 10px; border-radius: 10px; background-color: #2c2e30; display: inline-block;'>
        <h2 style='font-size:24px;'>The predicted market segment is: <strong>{predicted_segment[0]}</strong></h2>
    </div>
    """, unsafe_allow_html=True)


#----------------------------------------------------------------Rent Affordability---------------------------------------------------------------
elif option == 'Rent Affordability':
    set_background_image('dark.jpg')
    st.title("Rent Affordability Analysis")
    
    col1, col2 = st.columns(2)


   
    with col1:
        region = st.selectbox('Region', main_regions)
        sqfeet = st.number_input('Square Feet', min_value=100, max_value=10000, value=1200)
        beds = st.number_input('Number of Beds', min_value=0, max_value=10, value=2)
        cats_allowed = st.selectbox('Cats Allowed', [0, 1])
        wheelchair_access = st.selectbox('Wheelchair Access', [0, 1])
        laundry_options = st.selectbox('Laundry Options', laundryoptions)
        

    with col2:
        type_of_house = st.selectbox('Type of House', types)
        baths = st.number_input('Number of Baths', min_value=0, max_value=10, value=2)
        dogs_allowed = st.selectbox('Dogs Allowed', [0, 1])
        electric_vehicle_charge = st.selectbox('Electric Vehicle Charge', [0, 1])
        comes_furnished = st.selectbox('Comes Furnished', [0, 1])
        parking_options = st.selectbox('Parking Options', parking)
        state = st.selectbox('State', states)

   
    monthly_budget = st.number_input('Your Monthly Budget (USD)')
    

    
    new_data = pd.DataFrame({
        'region': [region],
        'type': [type_of_house],
        'laundry_options': [laundry_options],
        'parking_options': [parking_options],
        'state': [state],
        'sqfeet': [sqfeet],
        'beds': [beds],
        'baths': [baths],
        'cats_allowed': [cats_allowed],
        'dogs_allowed': [dogs_allowed],
        'wheelchair_access': [wheelchair_access],
        'electric_vehicle_charge': [electric_vehicle_charge],
        'comes_furnished': [comes_furnished],
        
    })
    
    new_data_df = pd.DataFrame(new_data)
        
       
    new_data_processed = preprocessor.transform(new_data_df)
        
       
    predicted_price = price_model.predict(new_data_processed)

   
    numerical_features = ['sqfeet', 'beds', 'baths', 'cats_allowed', 'dogs_allowed', 
                          'wheelchair_access', 'electric_vehicle_charge', 'comes_furnished']
    categorical_features = ['region', 'type', 'laundry_options', 'parking_options', 'state']

    new_data_num_scaled = scaler.transform(new_data[numerical_features])
    new_data_cat_encoded = encoder.transform(new_data[categorical_features])

    
    new_data_transformed = np.hstack([new_data_num_scaled, new_data_cat_encoded])

 
    affordable = predicted_price < 0.30 * monthly_budget

    if st.button('Check Affordability'):
        if affordable:
            st.success(f'This rental is affordable based on your budget (${monthly_budget:.2f})!')
        else:
            st.error(f'This rental exceeds your affordability limit based on your budget (${monthly_budget:.2f}).')
