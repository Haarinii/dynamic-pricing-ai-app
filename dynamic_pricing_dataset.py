import pandas as pd
import random

# Product types
products = [
    ("Chocolate Cake", 250),
    ("Vanilla Cake", 200),
    ("Black Forest Cake", 300),
    ("Red Velvet Cake", 350),
    ("Pineapple Cake", 220),
    ("Strawberry Cake", 240),
    ("Butterscotch Cake", 260),
    ("Rainbow Cake", 400)
]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
times = ['Morning', 'Afternoon', 'Evening']
demand_levels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']


data = []

for _ in range(1000):
    product, base_price = random.choice(products)
    day = random.choice(days)
    time = random.choice(times)
    inventory = random.randint(10, 100)
    demand = random.choice(demand_levels)
    festival = random.choice([0, 1])
    
    # Dynamic price logic (this is the target AI should learn)
    price = base_price
    if demand == 'High':
        price += random.randint(10, 40)
    elif demand == 'Low':
        price -= random.randint(5, 25)
    if festival:
        price += random.randint(15, 50)
    if inventory < 30:
        price += random.randint(5, 15)
    
    data.append([product, day, time, inventory, demand, festival, round(price, 2)])

# Save to CSV
df = pd.DataFrame(data, columns=["Product", "Day", "Time", "Inventory", "Demand", "Festival", "Price"])
df.to_csv("simulated_pricing_data.csv", index=False)
