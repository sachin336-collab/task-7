
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Query 1: Total quantity and revenue per product
query1 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df1 = pd.read_sql_query(query1, conn)

# Query 2: Top 3 products by revenue
query2 = """
SELECT 
    product, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product 
ORDER BY revenue DESC 
LIMIT 3
"""
df2 = pd.read_sql_query(query2, conn)

conn.close()

# Print results of Query 1
print("📦 Total Quantity and Revenue per Product:\n")
print(df1)

# Print results of Query 2
print("\n🏆 Top 3 Products by Revenue:\n")
print(df2)

# Plot bar chart for revenue per product
df1.plot(kind='bar', x='product', y='revenue', color='skyblue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
