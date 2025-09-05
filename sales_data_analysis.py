import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    file_path='D:\project\Sales_Data\sales_250.csv'
    return pd.read_csv(file_path)


def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  

    
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    
    non_numeric_cols = df.select_dtypes(exclude=['number', 'datetime']).columns
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])  

    return df



def basic_eda(df):
    print("\n----- Data Info -----")
    print(df.info())
    
    print("\n----- Summary Statistics -----")
    print(df.describe())

    print("\n----- Correlation Matrix -----")
    numeric_df = df.select_dtypes(include=['number'])   
    print(numeric_df.corr())

# Sales Trend Visualization (Line Plot)
def plot_sales_trends(df):
    """Plot sales trends over time."""
    df_sorted = df.sort_values(by='Date')
    monthly_sales = df_sorted.groupby(df_sorted['Date'].dt.to_period('M')).agg({'Revenue': 'sum'}).reset_index()
    
    plt.figure(figsize=(10,6))
    plt.plot(monthly_sales['Date'].astype(str), monthly_sales['Revenue'], marker='o', color='blue')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Top-selling Products Analysis (Bar Plot)
def plot_top_products(df):
    """Visualize top-selling products by revenue."""
    top_products = df.groupby('Product').agg({'Revenue': 'sum'}).sort_values(by='Revenue', ascending=False)

    top_products.plot(kind='bar', color='green', figsize=(8,6))
    plt.title('Top-selling Products by Revenue')
    plt.xlabel('Product Name')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.show()

# Customer Segmentation Visualization (Pie Chart)
def plot_customer_segments(df):
    """Visualize customer distribution by gender."""
    gender_sales = df.groupby('Customer_Gender').agg({'Revenue': 'sum'}).reset_index()
    gender_sales.set_index('Customer_Gender', inplace=True)
    
    gender_sales.plot.pie(y='Revenue', autopct='%1.1f%%', figsize=(8,8), legend=False, startangle=90)
    plt.title('Sales Distribution by Gender')
    plt.ylabel('')
    plt.show()


def generate_insights(df):
    """Generate actionable insights from the sales data."""
    top_products = df.groupby('Product').agg({'Revenue': 'sum'}).sort_values(by='Revenue', ascending=False)

    print(f"Top Selling Product: {top_products.index[0]} with Revenue: {top_products['Revenue'].max()}")
    
    
    gender_sales = df.groupby('Customer_Gender').agg({'Revenue': 'sum'}).reset_index()
    top_gender = gender_sales.loc[gender_sales['Revenue'].idxmax(), 'Customer_Gender']
    print(f"Top Customer Gender: {top_gender} with highest revenue.")
    
    
    correlation = df[['Quantity', 'Revenue']].corr()

    print("\nCorrelation Matrix (useful for deeper analysis):")
    print(correlation)
    
    return top_products, correlation

file_path = 'D:\project\Sales_Data\sales_250.csv'  
df = load_data(file_path)
df = preprocess_data(df)
basic_eda(df)
plot_sales_trends(df)
plot_top_products(df)
plot_customer_segments(df)
top_products, correlation = generate_insights(df)
