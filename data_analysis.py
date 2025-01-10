import pandas as pd

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

#Calculate total revenue
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: ${total_revenue}")

#Find the top-selling products bu quantity
top_dishes = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Selling Products:")
print(top_dishes)