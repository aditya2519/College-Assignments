# Sample sales data
sales_data = [
    {"product name": "Product A", "category": "Electronics", "units sold": 100, "unit price": 50.0},
    {"product name": "Product B", "category": "Clothing", "units sold": 150, "unit price": 30.0},
    {"product name": "Product C", "category": "Electronics", "units sold": 200, "unit price": 100.0},
    {"product name": "Product D", "category": "Food", "units sold": 300, "unit price": 5.0},
]

# 1. Calculate total sales
total_sales = 0
for item in sales_data:
    total_sales += item["units sold"] * item["unit price"]

# 2. Calculate average sales per product
average_sales = total_sales / len(sales_data)

# 3. Find top-selling products by revenue and units sold without lambda
top_by_revenue = sales_data[0]  # Start by assuming the first product is the top
top_by_units = sales_data[0]    # Same for top by units

for item in sales_data:
    revenue = item["units sold"] * item["unit price"]
    
    # Check for top by revenue
    top_revenue = top_by_revenue["units sold"] * top_by_revenue["unit price"]
    if revenue > top_revenue:
        top_by_revenue = item
    
    # Check for top by units sold
    if item["units sold"] > top_by_units["units sold"]:
        top_by_units = item

# 4. Sales by category
sales_by_category = {}
for item in sales_data:
    category = item["category"]
    category_sales = item["units sold"] * item["unit price"]
    
    if category not in sales_by_category:
        sales_by_category[category] = 0
    sales_by_category[category] += category_sales

# Output results
print(f"Total Sales: {total_sales} INR")
print(f"Average Sales per Product: {average_sales:.2f} INR")
print(f"Top-selling product by revenue: {top_by_revenue['product name']} with {top_by_revenue['units sold'] * top_by_revenue['unit price']} INR")
print(f"Top-selling product by units: {top_by_units['product name']} with {top_by_units['units sold']} units sold")

print("\nSales by Category:")
for category, sales in sales_by_category.items():
    print(f"{category}: {sales} INR")
