import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.metrics import mean_absolute_error

# Load updated dataset
df = pd.read_csv("simulated_pricing_data.csv")

# Label Encoding for categorical features
le_product = LabelEncoder()
le_day = LabelEncoder()
le_time = LabelEncoder()
le_demand = LabelEncoder()

df["Product"] = le_product.fit_transform(df["Product"])
df["Day"] = le_day.fit_transform(df["Day"])
df["Time"] = le_time.fit_transform(df["Time"])
df["Demand"] = le_demand.fit_transform(df["Demand"])

# Features & target
X = df[["Product", "Day", "Time", "Inventory", "Demand", "Festival"]]
y = df["Price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"✅ Model trained! Mean Absolute Error: ₹{round(mae, 2)}")

# Save model & encoders
joblib.dump(model, "pricing_model.pkl")
joblib.dump(le_product, "le_product.pkl")
joblib.dump(le_day, "le_day.pkl")
joblib.dump(le_time, "le_time.pkl")
joblib.dump(le_demand, "le_demand.pkl")
