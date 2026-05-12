# ☕ Afficionado Coffee Roasters
## Product Optimization & Revenue Contribution Analysis

**Internship:** Unified Mentor | Data Analyst Project  
**Analyst:** Mohan Lal Kumawat  
**Tool:** Python, Streamlit  
**Live Dashboard:** [Click Here](https://afficionado-coffee-analysis-ip2nceibngh4brxb4av5iw.streamlit.app/)

---

## 📌 Project Overview

This project analyzes transaction-level sales data from Afficionado Coffee Roasters to understand product performance, revenue contribution, and menu optimization opportunities.

The goal is to shift focus from **when customers buy** to **what they buy** and **what drives revenue**.

---

## 🎯 Objectives

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

## 👨‍💻 About

**Mohan Lal Kumawat**  
Data Analyst | Unified Mentor Internship  
📧 mohankumawat17@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mohan-kumawat-270125aa)
