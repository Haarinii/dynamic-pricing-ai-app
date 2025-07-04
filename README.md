# AI-Powered Dynamic Pricing Engine for Cake Shop 🎂

This project is an intelligent pricing prediction application built using **Machine Learning** and **Streamlit**. It assists cake shop businesses in determining the most optimal selling price based on real-time operational conditions like product type, demand, inventory levels, time of day, and seasonal factors.

---

## 📌 Project Overview

Pricing plays a crucial role in maximizing profit and customer satisfaction. Static pricing fails to adapt to dynamic business factors like festive demand or stock availability.

This app solves that by using a **Random Forest Regression model** to recommend data-driven pricing decisions for different cake varieties. It helps users compare fixed (static) pricing and model-predicted dynamic pricing, highlighting potential profit improvements.

---

## 🎯 Key Features

- User-friendly web app interface built with **Streamlit**
- Input options include:
  - Product type (8 cake types)
  - Day of the week
  - Time of day
  - Inventory level
  - Demand level
  - Festival flag (Yes/No)
- Real-time prediction of best selling price
- Comparison between static price vs AI-recommended price
- Highlights expected **profit gain**

---

## 🧠 Machine Learning Details

- **Model Used**: Random Forest Regressor
- **Target**: Selling Price (₹)
- **Input Features**:
  - Product
  - Day
  - Time
  - Inventory
  - Demand
  - Festival (Boolean)
- **Encoding**: Used `LabelEncoder` for all categorical inputs
- **Evaluation Metric**: Mean Absolute Error (MAE)  
  → Final MAE achieved: ₹**7.87**

---

## 🛠️ Tech Stack

| Technology     | Role                                 |
|----------------|--------------------------------------|
| Python         | Core programming                     |
| Pandas         | Data handling                        |
| Scikit-learn   | Model training & label encoding      |
| Streamlit      | Web app frontend                     |
| Joblib         | Saving/loading model & encoders      |

---

## 📁 Project Structure

Dynamic_Pricing_Engine/
├── app_dynamic_pricing.py        # Streamlit app to interact with the model
├── train_pricing_model.py        # Script to train the Random Forest model
├── simulated_pricing_data.csv    # Dataset used for training
├── pricing_model.pkl             # Trained machine learning model
├── le_product.pkl                # LabelEncoder for product types
├── le_day.pkl                    # LabelEncoder for days of the week
├── le_time.pkl                   # LabelEncoder for time slots
├── le_demand.pkl                 # LabelEncoder for demand levels



---

## ✅ My Learnings

- End-to-end development of an ML application
- Real-time prediction deployment using Streamlit
- Difference between static and dynamic pricing models
- Data preprocessing and label encoding techniques
- Building UI/UX with functional design for business tools

---

## ⚙️ How to Run the App

1. Clone the repository
2. Install dependencies  
   `pip install streamlit pandas scikit-learn joblib`
3. Run the app  
   `streamlit run app_dynamic_pricing.py`

---

## 📌 About the Author

I developed this project as part of my learning in Data Science and AI. Initially, I faced challenges understanding encoding, model integration, and UI structuring, but by exploring and debugging step by step, I was able to build a fully functional business tool.

This project helped me understand the **real-world impact of AI on small businesses**, especially in optimizing pricing strategies through data.

---

## 🖼️ Screenshot

![App Screenshot](screenshot_app.png)

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/harinik13/) or drop a message if you want to collaborate or give feedback.

---




