import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # 🔁 replace with your root password
    database="product_db"
)

cursor = conn.cursor()

# List of product rows (each is a tuple)
products = [
    ("Wireless Bluetooth Headphones", "Electronics", 49.99, "USA"),
    ("Noise Cancelling Earbuds", "Electronics", 59.99, "Canada"),
    ("Ceramic Coffee Mug", "Kitchenware", 9.99, "UK"),
    ("Stainless Steel Water Bottle", "Fitness", 19.99, "Australia"),
    ("Fitness Tracker Watch", "Wearables", 99.99, "Germany"),
    ("Organic Green Tea Pack", "Grocery", 14.99, "USA"),
    ("Portable Bluetooth Speaker", "Electronics", 39.99, "USA"),
    ("Yoga Mat with Carry Strap", "Fitness", 29.99, "India"),
    ("LED Desk Lamp with USB Charging", "Home Decor", 24.99, "UK"),
    ("Reusable Eco-Friendly Grocery Bags", "Grocery", 12.49, "Canada")
]

# SQL insert query
sql = "INSERT INTO products (description, category, price, country) VALUES (%s, %s, %s, %s)"

# Insert all rows at once
cursor.executemany(sql, products)
conn.commit()

print(f"✅ Inserted {cursor.rowcount} rows into MySQL.")

# Fetch and print all records
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
