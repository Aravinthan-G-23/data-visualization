import sqlite3
import random
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Define sample products
products = ["Apples", "Bananas", "Oranges", "Grapes", "Mangoes"]

# Generate 100 random sales records
sample_data = []
for _ in range(100):
    product = random.choice(products)
    quantity = random.randint(1, 20)         # Quantity between 1 and 20
    price = round(random.uniform(0.2, 1.5), 2)  # Price between ₹0.20 and ₹1.50
    sample_data.append((product, quantity, price))

# Insert data into the table
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Query total quantity and revenue per product
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       ROUND(SUM(quantity * price), 2) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Display results
print("Sales Summary (100 Records):")
print(df)

# Plot revenue per product
plt.figure(figsize=(8, 5))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='mediumseagreen')
plt.title("Revenue by Product (100 Sales Records)")
plt.ylabel("Revenue (₹)")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart_100.png")
plt.show()

# Close connection
conn.close()
