import streamlit as st
import pandas as pd
import joblib, requests, os

url = "https://huggingface.co/ochiengbilly/Car-price-estimator-ke/resolve/main/predictor-app/model_pipeline.pkl"
model_path = "model_pipeline.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(model_path):
        r = requests.get(url)
        with open(model_path, "wb") as f:
            f.write(r.content)
    return joblib.load(model_path)

model = load_model()

# Title
st.title('Car Price Estimator KE')

# Input form
with st.form('prediction_form'):
    st.subheader("Enter the car's details:")

    make = st.selectbox("Make", ['Mercedes-Benz', 'Bentley', 'Land Rover', 'Lexus', 'Honda',
                                'Toyota', 'Porsche', 'Nissan', 'BMW', 'Ford', 'Jeep', 'Rover',
                                'Audi', 'Maserati', 'Isuzu', 'Daihatsu', 'Volkswagen', 'Jaguar',
                                'Mazda', 'Kia', 'Volvo', 'Mitsubishi', 'Subaru', 'Alfa Romeo',
                                'Suzuki', 'JMC', 'Peugeot', 'Hyundai', 'Mini', 'Infiniti',
                                'Renault', 'Citroen', 'Smart', 'MG', 'Great Wall', 'Mahindra',
                                'Chevrolet', 'Maruti Suzuki', 'Other Make', 'Geely', 'Vauxhall',
                                'Chery'])
    model_name = st.text_input("Model (E400)")
    
    transmission = st.selectbox("Transmission", ['Automatic', 'AMT', 'CVT', 'Manual'])
    previous_ownership = st.selectbox("Previous Ownership", ['Foreign Used', 'Brand New', 'Local Used', 'Kenyan Used'])
    mileage = st.number_input("Mileage (in kilometers)", min_value=0)
    
    age = st.number_input("Age (in years)", min_value=0)

    submit = st.form_submit_button("Predict Price")

# Run prediction
if submit:
    try:
        # Create DataFrame with the same structure used during training
        input_df = pd.DataFrame([{
            'make': make,
            'model': model_name,
            'transmission': transmission,
            'previous_ownership': previous_ownership,
            'mileage': mileage,
            'age': age
        }])

        # Predict using the full pipeline
        prediction = model.predict(input_df)[0]

        st.success(f"Estimated car price: Ksh{prediction:,.2f}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
