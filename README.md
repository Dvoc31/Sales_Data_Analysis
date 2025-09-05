# Sales_Data_Analysis
This project analyzes retail sales data using Python. It helps understand sales trends over time, identifies top-selling products, and shows customer segments by gender or region. The project uses data cleaning, simple analysis, and visualizations like line charts, bar charts, and pie charts to generate insights for better business decisions.

**Dataset: **
The dataset `sales_250.csv` contains 250+ sales records with the following columns:  
- `Date` – Transaction date  
- `Product` – Product name  
- `Quantity` – Number of units sold  
- `Revenue` – Revenue generated per transaction  
- `Customer_Gender` – Gender of the customer (M/F)  
- `Region` – Store region  

---

**Technologies Used**
- **Python** – Programming language for data analysis  
- **Pandas** – Data manipulation and cleaning  
- **Matplotlib** – Visualizing sales trends and product performance  
- **Seaborn** – Optional for advanced visualizations  

---

**Project Workflow**
1. **Data Loading:** Read CSV file and load it into a pandas DataFrame.  
2. **Data Preprocessing:** Convert dates, handle missing values, and clean columns.  
3. **Exploratory Data Analysis (EDA):** Check data types, summary statistics, and correlation matrices.  
4. **Visualizations:**  
   - **Sales Trends:** Line plot showing revenue trends over months.  
   - **Top-selling Products:** Bar chart visualizing revenue per product.  
   - **Customer Segments:** Pie chart showing revenue distribution by gender.  
5. **Insights Generation:** Identify top-selling products, highest-revenue customer segments, and quantity-revenue correlation.

---

**Key Insights**
- Top-selling product by revenue  
- Customer segment (gender) generating highest revenue  
- Correlation between quantity sold and revenue to understand sales patterns  
