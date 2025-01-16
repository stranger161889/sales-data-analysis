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

4. **Choose- an Otion from the Menu**:
- Enter '1' or type 'view total revenue' to view the total revenue.
- Enter '2' or type 'display top selling products' to display top-selling products.
- Enter '3' or type 'show bar chart' to view bar chart.
- Enter '4' or type 'show pie chart' to view pie chart.
- Enter '5' or type 'show line plot' to view a line plot of revenue over time.
- Enter'6' or type 'exit' to quit the program

## Example Menu Output
```plaintext

Choose and option:
1. View Total Revenue
2. Display Top-Selling Products
3. Show Bar Chart for Top-Seling Products
4. Show Pie Chart for Revenue Contribution
5. Show Line Plot for Revenue Over Time
6. Exit