# ☕ Afficionado Coffee Roasters
## Product Optimization & Revenue Contribution Analysis

**Internship:** Unified Mentor | Data Analyst Project  
**Analyst:** Mohan Lal Kumawat  
**Tool:** Python, Streamlit  
**Live Dashboard:** [Click Here](https://afficionado-coffee-analysis-ip2nceibngh4brxb4av5iw.streamlit.app/)

---
## 💼 Business Problem

Afficionado Coffee Roasters offers a wide range of products across multiple stores and categories. As the product portfolio grows, it becomes difficult to identify which products drive revenue, which products should be promoted, and which products contribute little to overall business performance.

Without product-level analysis, management may struggle to make informed decisions about inventory planning, product promotions, and menu optimization.

---
## 📌 Project Overview

This project analyzes transaction-level sales data from Afficionado Coffee Roasters to understand product performance, revenue contribution, and menu optimization opportunities.

The goal is to shift focus from **when customers buy** to **what they buy** and **what drives revenue**.

---
## ❓ Business Questions

- Which products generate the highest revenue?
- Which products sell the highest quantity?
- Which product categories contribute the most revenue?
- Which products should be considered Hero Products?
- Does the Pareto Principle (80/20 Rule) apply to product revenue?
- Which products should management focus on for business growth?

---
## 🎯 Business Objectives

- Identify top-selling and least-selling products
- Quantify revenue contribution by product and category
- Measure revenue concentration across the menu
- Identify high-impact "Hero" products
- Support menu simplification and optimization

---

## 📁 Project Structure

```
Coffee_Project2/
│
├── Afficionado Coffee Roasters.xlsx   ← Raw dataset
├── analysis.ipynb                     ← Python EDA notebook
├── app.py                             ← Streamlit dashboard
├── README.md                          ← Project documentation
│
├── Charts/
│   ├── product_popularity.png
│   ├── revenue_contribution.png
│   ├── category_revenue.png
│   ├── product_type_analysis.png
│   ├── pareto_analysis.png
│   └── hero_products.png
```

---

## 📊 Dataset Description

| Column | Description |
|--------|-------------|
| transaction_id | Unique identifier per transaction |
| year | Transaction year (2025) |
| transaction_time | Time of transaction |
| transaction_qty | Quantity purchased |
| unit_price | Price per unit |
| store_id | Store identifier |
| store_location | Physical store location |
| product_id | Unique product identifier |
| product_category | Broad product group |
| product_type | Product variant |
| product_detail | Detailed product name |

**Total Records:** 1,49,116 transactions  
**Total Products:** 80  
**Total Categories:** 9  
**Store Locations:** Lower Manhattan, Hell's Kitchen, Astoria

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3.14 | Core programming |
| Pandas | Data cleaning & analysis |
| NumPy | Mathematical calculations |
| Matplotlib | Static charts |
| Seaborn | Enhanced visualizations |
| Plotly | Interactive charts |
| Streamlit | Web dashboard |

---

## 🔑 Key Findings

- **Total Revenue:** $6,98,812
- **Top Category:** Coffee (38.63% revenue share)
- **#1 Hero Product:** Dark Chocolate Lg (Hero Score: 69.5)
- **Pareto Result:** 42 products = 80% of total revenue
- **Best Selling Product:** Earl Grey Rg (4,708 units)
- **Highest Revenue Product:** Sustainably Grown Organic Lg ($21,151)

---

## ▶️ How to Run

**Step 1:** Install required libraries
```bash
python -m pip install pandas numpy matplotlib seaborn plotly streamlit openpyxl
```

**Step 2:** Run the Streamlit dashboard
```bash
python -m streamlit run app.py
```

**Step 3:** Open browser at `http://localhost:8501`

---

## 📈 Dashboard Features

- **KPI Cards** — Total Revenue, Transactions, Units Sold
- **Product Ranking** — Top N by Volume & Revenue
- **Category Analysis** — Pie & Bar charts
- **Pareto Analysis** — 80/20 revenue concentration
- **Product Table** — Full drill-down with filters
- **Filters** — Category, Store Location, Top N slider

---
## 💡 Business Recommendations

- Focus marketing efforts on Hero Products with high revenue contribution.
- Maintain sufficient inventory for high-demand products.
- Review low-performing products and evaluate their business value.
- Optimize the product portfolio using Pareto Analysis.
- Monitor category performance regularly to support data-driven decisions.

---
## 📈 Business Impact

This analysis helps management understand product performance, improve inventory planning, optimize the product portfolio, and make better business decisions based on revenue contribution and customer purchasing patterns.

---
## 🚀 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning & Transformation
- Product Performance Analysis
- Revenue Analysis
- Pareto Analysis (80/20 Rule)
- Business Reporting
- Data Visualization
- Streamlit Dashboard Development

---
## 👨‍💻 About

**Mohan Lal Kumawat**  
Aspiring Business Data Analyst
Skills: Excel | SQL | Power BI | Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
📧 mohankumawat17@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mohan-kumawat-270125aa)
