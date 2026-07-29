# Retail Sales Analytics
# Author: Rishu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Display first five rows
print("First Five Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
print(df.info())

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Basic Statistics
print("\nSummary Statistics")
print(df.describe())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Average Sales
print("Average Sales:", df["Sales"].mean())

# Average Profit
print("Average Profit:", df["Profit"].mean())

# -------------------------------
# Exploratory Data Analysis (EDA)
# -------------------------------

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar", color="lightgreen")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(color="blue", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind="barh", color="orange")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

# Sales by Segment
segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,6))
plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales by Customer Segment")
plt.show()
