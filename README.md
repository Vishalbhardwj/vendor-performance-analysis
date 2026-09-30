# 📦 Vendor Performance Analysis

## 🎯 Overview / Business Problem

This project analyzes **vendor sales, purchasing, profitability, pricing, and inventory performance** to identify opportunities for improving profitability and inventory efficiency.

The analysis focuses on:
- 🏪 Identifying top and underperforming vendors
- 🏷️ Finding low-sales, high-margin brands
- 💰 Understanding bulk purchasing and unit-cost savings
- 📦 Identifying slow-moving inventory and unsold capital
- 📊 Comparing profitability across vendor groups

---

## 📊 Dataset / Source

The project uses retail and wholesale data covering:

- 🛒 Purchases
- 💵 Sales
- 💰 Purchase Prices
- 🚚 Vendor Invoices & Freight
- 📦 Beginning & Ending Inventory

The raw CSV files were loaded into **SQLite** and combined into a consolidated `vendor_sales_summary` dataset for analysis.

---

## 🛠️ Tools

- 🐍 Python
- 🐼 Pandas
- 🗃️ SQL / SQLite
- 📊 Matplotlib & Seaborn
- 📐 SciPy
- ⚙️ SQLAlchemy
- 📓 Jupyter Notebook
- 📈 Power BI

---

## 🔍 Analysis

- 💰 Sales, purchases & gross profit
- 📈 Profit margin analysis
- 🏪 Vendor performance & purchase contribution
- 🏷️ Brand performance
- 📦 Inventory & stock turnover
- 💵 Bulk purchasing & unit-cost analysis
- 🚚 Freight cost analysis
- 🔗 Correlation analysis
- 🧪 Statistical analysis of vendor profitability

---

## 📈 Dashboard

The Power BI dashboard provides an interactive view of:

- 💰 Total Sales, Purchase & Gross Profit
- 📊 Profit Margin
- 📦 Unsold Inventory Capital
- 🏪 Purchase Contribution by Vendor
- 💵 Top Vendors by Sales
- 🏷️ Top Brands by Sales
- 📉 Low-Performing Vendors & Brands
- 📊 Sales vs. Profit Margin

### 🖼️ Dashboard Preview

![Vendor Performance Dashboard](images/vendor-performance-dashboard.png)

---

## 💡 Key Insights

- 🏪 The **top 10 vendors contribute 65.69% of total purchases**.
- 💰 Bulk purchasing can reduce unit costs by approximately **72%**.
- 📦 Approximately **$2.71M** of capital is tied up in unsold inventory.
- 🏷️ **198 brands** have lower sales but higher profit margins.
- 📊 Top-performing vendors have a mean profit margin of **31.17%**, compared with **41.55%** for low-performing vendors.
- 🔗 Purchase price has a weak relationship with total sales dollars and gross profit.
- 📈 Faster stock turnover does not necessarily result in higher profitability.

---

## 🎯 Recommendations

- 🏷️ Re-evaluate pricing for low-sales, high-margin brands.
- 🏪 Diversify vendor partnerships to reduce supplier dependency.
- 💰 Leverage bulk purchasing where appropriate.
- 📦 Optimize slow-moving inventory and reduce tied-up capital.
- 📣 Improve marketing and distribution for low-performing vendors.
- 💵 Optimize pricing and operating costs for high-volume vendors.

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/VishalBhardwj/vendor-performance-analysis.git
cd vendor-performance-analysis
```
### 2️⃣ Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy sqlalchemy jupyter
```

### 3️⃣ Run the Data Pipeline

```bash
python script/ingestion_db.py
python script/get_vendor_summary.py
```
This loads the raw CSV files into SQLite and creates the vendor_sales_summary table.

### 4️⃣ Run the Analysis

Open Jupyter Notebook and run the analysis notebooks in the notebook/ folder.

### 👤 Author

Vishal Bhardwaj

📊 Data Analyst | 🐍 Python | 🗃️ SQL | 📈 Power BI 
