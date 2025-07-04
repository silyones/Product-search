import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # 🔁 Replace with your MySQL password
        database="product_db"
    )

def get_product_info(product_name):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Search for exact or partial match (case-insensitive)
    sql = """
    SELECT description, category, price, country 
    FROM products 
    WHERE LOWER(description) LIKE %s
    """
    search_term = f"%{product_name.lower()}%"
    cursor.execute(sql, (search_term,))

    results = cursor.fetchall()

    if results:
        for row in results:
            description, category, price, country = row
            print(f"\n🎯 Product: {description}")
            print(f"📦 Category: {category}")
            print(f"💰 Price: ₹{price}")
            print(f"🌍 Country: {country}")
    else:
        print("\n❌ No matching product found.")

    cursor.close()
    conn.close()

# 🧪 Test it
query = input("Ask about a product: ")
get_product_info(query)
