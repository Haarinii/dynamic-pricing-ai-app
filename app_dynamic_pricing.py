import streamlit as st
import pandas as pd
import joblib

# Load model and label encoders
model = joblib.load("pricing_model.pkl")
le_product = joblib.load("le_product.pkl")
le_day = joblib.load("le_day.pkl")
le_time = joblib.load("le_time.pkl")
le_demand = joblib.load("le_demand.pkl")

# 🎀 Cute Styling
st.markdown("""
    <style>
    .stApp { background-color: #fff0f5; }
    .stSlider > div[data-baseweb="slider"] { color: #ff69b4; }
    .css-1aumxhk {
        font-family: "Comic Sans MS", cursive;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# 🎀 Page Setup
st.set_page_config(page_title="💰 AI Dynamic Pricing App")
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4; font-size: 40px;'>
        🎀&nbsp;AI Dynamic Pricing Predictor&nbsp;🎀
    </h1>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>💡 <i>Enter your cute business values below, and I’ll find the smartest price for you! 🧸✨</i></p>", unsafe_allow_html=True)

# 🧁 User Input
product_type = st.selectbox("🍰 Select Product", [
    "Chocolate Cake", "Vanilla Cake", "Black Forest Cake", "Red Velvet Cake",
    "Pineapple Cake", "Strawberry Cake", "Butterscotch Cake", "Rainbow Cake"
])

# Static pricing for reference
if product_type == "Chocolate Cake":
    static_price = 250
elif product_type == "Vanilla Cake":
    static_price = 200
elif product_type == "Black Forest Cake":
    static_price = 300
elif product_type == "Red Velvet Cake":
    static_price = 350
elif product_type == "Pineapple Cake":
    static_price = 220
elif product_type == "Strawberry Cake":
    static_price = 240
elif product_type == "Butterscotch Cake":
    static_price = 260
elif product_type == "Rainbow Cake":
    static_price = 400

# Categorical options
day = st.selectbox("📅 Day", le_day.classes_)
time = st.selectbox("⏰ Time", le_time.classes_)
inventory = st.slider("📦 Inventory Level", 0, 100, 50)
demand = st.selectbox("📈 Demand Level", le_demand.classes_)
festival = st.checkbox("🎉 Festival Day?")

# 💻 Encode inputs
product_enc = le_product.transform([product_type])[0]
day_enc = le_day.transform([day])[0]
time_enc = le_time.transform([time])[0]
demand_enc = le_demand.transform([demand])[0]
festival_enc = int(festival)

# 🎯 Predict
input_data = [[product_enc, day_enc, time_enc, inventory, demand_enc, festival_enc]]
predicted_price = model.predict(input_data)[0]

# 💰 Display Result
st.markdown(f"""
    <div style="background-color:#ffe4e1; padding:20px; border-radius:20px; text-align:center; box-shadow: 0 0 10px pink;">
        <h2 style="color:#ff1493;">💰 Your Smart Price is: ₹{round(predicted_price, 2)}</h2>
        <p style="font-size:18px;">🎯 Best price for a {product_type} based on current demand & inventory!</p>
    </div>
""", unsafe_allow_html=True)

profit = round(predicted_price - static_price, 2)

st.markdown("""
    <br><h3 style='text-align:center; color:#d63384;'>📊 Profit Comparison</h3>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div style="background-color:#fff5f8; padding:20px; border-radius:15px;">
        <table style='width:100%; font-size:18px; text-align:center;'>
            <tr style='background-color:#ffb6c1; color:white;'>
                <th>Pricing Type</th><th>Price</th>
            </tr>
            <tr><td>🧁 Static Price</td><td>₹{static_price}</td></tr>
            <tr><td>🧠 AI Smart Price</td><td>₹{round(predicted_price, 2)}</td></tr>
            <tr><td>💸 Extra Profit</td><td style='color:#d63384;'>+ ₹{profit}</td></tr>
        </table>
    </div>
""", unsafe_allow_html=True)

