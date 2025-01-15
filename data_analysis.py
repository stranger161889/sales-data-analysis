import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03"], 
    "Product": ["Pizza", "Pasta", "Sushi"], "Revenue": [500, 400, 600], 
    "Quantity": [25, 20, 30]
    }

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame(data)
print("Sales Data:")
print(df)

# Calculate total revenue
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: ${total_revenue}")

# Find the top-selling products bu quantity
top_dishes = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Selling Products:")
print(top_dishes)

# ---Data Visualization---

# 1. Bar chart for top selling products
plt.figure(figsize=(8,5)) 
top_dishes.plot(kind='bar', title='Top 5 Selling Products', ylabel='Quantity Sold', xlabel='Product')
plt.show()

# 2. Pie chart for revenue contribution
plt.figure(figsize=(8,5))
df.groupby("Product")["Revenue"].sum().plot(kind='pie', autopct='%1.1f%%', title='Revenue Contribution by PRoduct')
plt.ylabel("") #Hides the default ylabel
plt.show()

# 3. Line plot for revenue over time
df["Date"] = pd.to_datetime(df["Date"]) # Convert 'Date' to datetime format
plt.plot(df["Date"], df["Revenue"], marker='o')

# Annotate each point with its revenue value
for i, txt in enumerate(df["Revenue"]):
    plt.annotate(f"${txt}", (df["Date"][i], df["Revenue"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)

#Format the x-axis ticks (rotate for readability)
plt.xticks(df["Date"], df["Date"].dt.strftime('%Y-%m-%d'), rotation=45)

plt.show()