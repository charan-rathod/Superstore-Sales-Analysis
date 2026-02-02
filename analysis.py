import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# -------------------------------
# BASIC DATA UNDERSTANDING
# -------------------------------

print("Shape of dataset:", df.shape)
print("\nColumns:\n", df.columns)
print("\nDataset Info:")
print(df.info())

# -------------------------------
# TOTAL SALES & PROFIT
# -------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# -------------------------------
# SALES BY CATEGORY
# -------------------------------

category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()

# -------------------------------
# PROFIT BY CATEGORY
# -------------------------------

category_profit = df.groupby("Category")["Profit"].sum()
print("\nProfit by Category:\n", category_profit)

category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.ylabel("Total Profit")
plt.show()

# -------------------------------
# LOSS MAKING PRODUCTS
# -------------------------------

loss_products = df[df["Profit"] < 0]

print("\nSample Loss Making Products:")
print(loss_products[["Product Name", "Sales", "Profit"]].head(10))

print("\nTotal Loss Orders:", loss_products.shape[0])

# Average discount on loss orders
print("Average Discount on Loss Orders:",
      loss_products["Discount"].mean())

# Loss by category
loss_by_category = loss_products.groupby("Category")["Profit"].sum()
print("\nLoss by Category:\n", loss_by_category)

loss_by_category.plot(kind='bar')
plt.title("Loss by Category")
plt.ylabel("Total Loss")
plt.show()

# -------------------------------
# TOP 10 CUSTOMERS
# -------------------------------

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Customers:\n", top_customers)

top_customers.plot(kind='bar')
plt.title("Top 10 Customers by Sales")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# SALES BY REGION
# -------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:\n", region_sales)

region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.show()

print("\n✅ ANALYSIS COMPLETE!")
