import pandas as pd
import matplotlib.pyplot as plt

#Sample sales data
data = {
    "Date": ["2025-01-01", "2025-01-02","2025-01-03"],
    "Product": ["Pizza", "Pasta", "Sushi"],
    "Revenue": [500, 400, 600],
    "Quantity": [25,20,30]
}

# Create DataFrame
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Function to display total revenue
def display_total_revenue():
    total_revenue = df["Revenue"].sum()
    print(f"\nTotal Revenue: ${total_revenue}")

# Function to display top_selling products
def display_top_selling_products():
    top_dishes = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Selling Products:")
    print(top_dishes)

# Function to show bar chart for top-selling products
def show_bar_chart():
    top_dishes = df.groupby("Product") ["Quantity"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8,5))
    top_dishes.plot(kind='bar',title='Top 5 Selling Products', ylabel='Quantity Sold', xlabel='Product')
    plt.show()

# Function to show pie chart for revenue contribution
def show_pie_chart():
    plt.figure(figsize=(8,5))
    df.groupby("Product")["Revenue"].sum().plot(kind='pie', autopct='%1.1f%%', title='Revenue Contribution by Product', legend=True)
    plt.ylabel("")
    plt.show()

#Function to show line plot for revenue over time
def show_line_plot():
    plt.figure(figsize=(8, 5))
    plt.plot(df["Date"], df["Revenue"], marker='o')
    for i, txt in enumerate(df["Revenue"]):
        plt.annotate(f"${txt}", (df["Date"][i], df["Revenue"][i]), textcoords="offset points", xytext=(0, 5), ha='center')
    plt.title('Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.xticks(df["Date"], df["Date"].dt.strftime('%Y-%m-%d'), rotation=45)
    plt.show()

#Interactive menu
while True:
    print("\nChoose an option:")
    print("1. View Total Revenue")
    print("2. Display Top-Selling Products")
    print("3. Show Bar Chart for Top-Selling Products")
    print("4. Show Pie Chart for Revenue Contribution")
    print("5. Show Line Plot for Revenue Over Time")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        display_total_revenue()
    elif choice == "2":
        display_top_selling_products()
    elif choice == "3":
        show_bar_chart()
    elif choice == "4":
        show_pie_chart()
    elif choice =="5":
        show_line_plot()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")