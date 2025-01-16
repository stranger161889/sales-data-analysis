# Interactive Data Analysis Tool

This project builds on the original Data Analysis Tool by introducing an interactive menu system. Users can explore sales data dynamically through a command-line interface.

## Features
- **Total Revenue**: Calculate and display the total revenue from the dataset.
- **Top-Selling Products**: Identify and display the top 5 products based on the quantity sold.
- **Bar Chart**: Visualize the top 5 selling products with a bar chart.
- **Pie Chart**: Show each product's contribution to total revenue as a pie chart.
- **Line Plot**: Display revenue trends over time using a line plot.
- **Interactive Menu**: Users can choose any of the above options or exit the program via a menu system.

## How to run
To use the interactive data analysis tool, folow these steps:

1. **Clone or Download the Repository**:
    If haven't already, clone this repository or download the files
```bash
git clonse https://github.com/stranger161889/sales-data-analysis.git
cd sales-data-analysis/interactive
```
2. **Install Dependencies**:
    This project requires the following Python libraries:
    -`pandas`
    -`matplotlib`
    
    Install them using:
    ```bash
    pip install pandas matplotlib
    ```

3. **Run the script**:
    Execute the sript in your terminal or command prompt:
```bash
python interactive_data_analysis.py
```

4. Choose an option from the menu:
- Enter (1) to view total revenue.
- Enter (2) to display top-selling products.
- Enter (3) to view a bar chart.
- Enter (4) to view a pie chart.
- Enter (5) to view a line plot of revenue over time.
- Enter (6) to exit.

## Example Menu Output
```plaintext

Choose and option:
1. View Total Revenue
2. Display Top-Selling Products
3. Show Bar Chart for Top-Seling Products
4. Show Pie Chart for Revenue Contribution
5. Show Line Plot for Revenue Over Time
6. Exit