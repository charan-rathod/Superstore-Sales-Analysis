import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Superstore Sales Analysis Dashboard")

# Load Data
df = pd.read_csv("superstore.csv", encoding='latin1')


st.subheader("Dataset Preview")
st.dataframe(df.head())

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")

# Sales by Category
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind='bar', ax=ax)
plt.xticks(rotation=0)

st.pyplot(fig)

# Profit by Category
st.subheader("Profit by Category")

category_profit = df.groupby("Category")["Profit"].sum()

fig2, ax2 = plt.subplots()
category_profit.plot(kind='bar', ax=ax2)
plt.xticks(rotation=0)

st.pyplot(fig2)

# Loss Making Orders
st.subheader("Loss Making Orders")

loss_orders = df[df["Profit"] < 0]

st.write("Total Loss Orders:", loss_orders.shape[0])
st.dataframe(loss_orders.head())
