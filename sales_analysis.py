import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Load the dataset
data = pd.read_csv("D:\DATA ANALYSIS\sales analysis\sales_data.csv")  # Make sure this file is in the same directory

# Display the first few rows of the dataset
print(data.head())

# Data Cleaning
data.dropna(inplace=True)  # Drop missing values
data['Date'] = pd.to_datetime(data['Date'])  # Convert 'Date' to datetime format
data['TotalSales'] = data['QuantitySold'] * data['SalePrice']  # Create Total Sales column

# Sales Trends Over Time
monthly_sales = data.resample('M', on='Date').sum()['TotalSales']
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Top-Selling Products
top_products = data.groupby('ProductName')['TotalSales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Sales by Region
region_sales = data.groupby('Region')['TotalSales'].sum()
plt.figure(figsize=(12, 6))
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Region')
plt.ylabel('')  # Hide the y-label
plt.show()