import pandas as pd
import random

# -------------------------
# Sample Data Options
# -------------------------

regions = [
    "East",
    "West",
    "North",
    "South"
]

salespersons = [
    "John",
    "Alice",
    "Bob",
    "Emma",
    "David",
    "Sophia",
    "Chris",
    "Olivia"
]

products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Monitor"
]

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

# -------------------------
# Generate Random Data
# -------------------------

data = []

for i in range(100):

    units = random.randint(1, 20)

    price = random.randint(200, 1000)

    revenue = units * price

    data.append({
        "Order_ID": 1000 + i,
        "Region": random.choice(regions),
        "Salesperson": random.choice(salespersons),
        "Product": random.choice(products),
        "Units_Sold": units,
        "Unit_Price": price,
        "Revenue": revenue,
        "Month": random.choice(months)
    })

# -------------------------
# Convert to DataFrame
# -------------------------

df = pd.DataFrame(data)

# -------------------------
# Save CSV File
# -------------------------

df.to_csv(
    "data/sample_data.csv",
    index=False
)

print("Dataset generated successfully.")