import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
# Read the CSV file
df = pd.read_csv(r'C:\Users\emre-\Downloads\amazonSales.csv')



# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Calculate total sales by category
category_sales = df.groupby('Category')['Amount'].sum()

# Visualize the Sales Distribution by Category
plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Sales Distribution by Category')
plt.show()

# Extract the month from 'Date' column
df['Month'] = df['Date'].dt.month

# Calculate total sales by month
monthly_sales = df.groupby('Month')['Amount'].sum()

# Visualize the Monthly Sales Trend
plt.figure(figsize=(8, 6))
monthly_sales.plot(kind='line', marker='o')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trend')
plt.xticks(range(1, 13))  # Set x-axis ticks from 1 to 12 (representing months)
plt.show()



