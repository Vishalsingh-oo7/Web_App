# 🚗 Used Car Price Prediction App (Streamlit + Pickle)
import pandas as pd
import streamlit as st
import pickle

# 📂 Load sample data for display
cars_df = pd.read_csv("cars24_car_price.csv")

# 🎯 App Title
st.title("🚗 Cars24 - Used Car Price Prediction")
st.markdown("Get an estimated resale price based on your car details.")

# 🔍 Show the first few rows of the dataset
with st.expander("📂 See Sample Car Data"):
    st.dataframe(cars_df.head())

# 🔐 Same Encoding used during Model Training
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

# 🎛️ --- USER INPUTS ---
st.header("📝 Enter Car Details:")

col1, col2 = st.columns(2)

# Left Column Inputs
year = col1.slider("Year of Purchase", 2000, 2023, 2015)
owner_type = col1.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
fuel_type = col1.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
mileage = col1.number_input("Mileage (in km/l)", min_value=5.0, max_value=40.0, value=18.0)

# Right Column Inputs
transmission_type = col2.selectbox("Transmission", ["Manual", "Automatic"])
engine_power = col2.slider("Engine Power (in CC)", 600, 5000, step=100, value=1200)
seats = col2.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8])
km_driven = col2.number_input("Kilometers Driven", min_value=0, max_value=500000, value=50000)

# 🧠 Encode categorical variables
fuel_encoded = encode_dict['fuel_type'][fuel_type]
seller_encoded = encode_dict['seller_type'][owner_type]
transmission_encoded = encode_dict['transmission_type'][transmission_type]

# 🧾 Model Prediction Function
def predict_price(year, seller_encoded, km_driven, fuel_encoded, transmission_encoded, mileage, engine_power, seats):
    try:
        with open("car_pred", "rb") as file:
            model = pickle.load(file)

        input_data = [[year, seller_encoded, km_driven, fuel_encoded, transmission_encoded,
                       mileage, engine_power, 46.3, seats]]
        prediction = model.predict(input_data)
        return round(prediction[0], 2)
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
        return None

# 🚀 Predict Button
if st.button("💰 Predict Resale Price"):
    price = predict_price(year, seller_encoded, km_driven, fuel_encoded, transmission_encoded,
                          mileage, engine_power, seats)
    if price is not None:
        st.success(f"✅ Estimated Resale Price: ₹{price:,.2f}")
