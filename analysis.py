import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

# Filter sales greater than 500
high_sales = df[df["Sales"] > 500]

print("\nHigh Sales Records:")
print(high_sales[["Product line", "Sales", "City"]].head())

# Total sales by product line
product_sales = df.groupby("Product line")["Sales"].sum()

print("\nTotal Sales by Product Line:")
print(product_sales)

# Best selling product line
best_product = product_sales.idxmax()

print("\nBest Selling Product Line:")
print(best_product)

# Average rating
average_rating = df["Rating"].mean()

print("\nAverage Rating:")
print(round(average_rating, 2))

# Bar chart for product sales
product_sales.plot(kind="bar")

plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Sales")

plt.show()