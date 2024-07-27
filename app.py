import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def monthly_revenue(data):
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = data['order_date'].dt.to_period('M')
    data['revenue'] = data['product_price'] * data['quantity']
    monthly_revenue = data.groupby('month')['revenue'].sum().reset_index()
    return monthly_revenue

def product_revenue(data):
    data['revenue'] = data['product_price'] * data['quantity']
    product_revenue = data.groupby('product_name')['revenue'].sum().reset_index()
    return product_revenue

def customer_revenue(data):
    data['revenue'] = data['product_price'] * data['quantity']
    customer_revenue = data.groupby('customer_id')['revenue'].sum().reset_index()
    return customer_revenue

def top_customers(data, top_n=10):
    customer_rev = customer_revenue(data)
    top_customers = customer_rev.nlargest(top_n, 'revenue')
    return top_customers

if __name__ == "__main__":
    data = load_data('orders.csv')
    print("Monthly Revenue:")
    print(monthly_revenue(data))
    print("Product Revenue:")
    print(product_revenue(data))
    print("Customer Revenue:")
    print(customer_revenue(data))
    print("Top 10 Customers:")
    print(top_customers(data))
