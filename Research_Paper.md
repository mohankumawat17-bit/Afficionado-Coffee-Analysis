# Research Paper
## Product Optimization & Revenue Contribution Analysis
### Afficionado Coffee Roasters

---

**Analyst:** Mohan Lal Kumawat  
**Internship:** Unified Mentor — Data Analyst Program  
**Date:** May 2026  
**Tools Used:** Python, Pandas, Matplotlib, Seaborn, Plotly, Streamlit

---

## 1. Abstract

This research paper presents a data-driven analysis of product performance and revenue contribution at Afficionado Coffee Roasters. Using transaction-level data of 1,49,116 records across 3 store locations, this study identifies top and bottom performing products, measures revenue concentration, and provides actionable recommendations for menu optimization.

The analysis reveals that Coffee dominates revenue at 38.63%, while 42 out of 80 products contribute 80% of total revenue — indicating an opportunity to streamline the menu and improve operational efficiency.

---

## 2. Introduction

### 2.1 Background

In specialty coffee retail, not all products contribute equally to revenue. Afficionado Coffee Roasters operates 3 store locations — Lower Manhattan, Hell's Kitchen, and Astoria — with a menu of 80 products across 9 categories.

Despite having rich transaction data, the business lacked:
- Clear visibility into product popularity vs profitability
- Category-level revenue dependency insights
- Identification of low-impact menu items

### 2.2 Problem Statement

Menu decisions were being made without structured product analytics, leading to:
- Overcrowded menu slowing service
- Resources spent on low-performing products
- Missed revenue opportunities from hero products

### 2.3 Research Objectives

**Primary:**
- Identify top-selling and least-selling products
- Quantify revenue contribution by product and category
- Measure revenue concentration across the menu

**Secondary:**
- Identify high-impact "Hero" products
- Highlight low-performing products for review
- Support menu simplification strategy

---

## 3. Dataset Description

| Attribute | Details |
|-----------|---------|
| Total Records | 1,49,116 transactions |
| Time Period | Year 2025 |
| Store Locations | 3 (Lower Manhattan, Hell's Kitchen, Astoria) |
| Total Products | 80 unique products |
| Product Categories | 9 categories |
| Missing Values | 0 (clean dataset) |

### 3.1 Key Columns Used

- **transaction_qty** — Units purchased per transaction
- **unit_price** — Price per unit
- **product_category** — Broad product group
- **product_type** — Product variant
- **product_detail** — Exact product name
- **store_location** — Branch name

### 3.2 Derived Column

```
Revenue = transaction_qty × unit_price
```

This column was computed for all 1,49,116 records.

---

## 4. Methodology

### Step 1 — Data Ingestion & Validation
- Loaded Excel dataset using Pandas
- Checked for missing values → Zero found
- Validated quantities (min = 1, no negatives)
- Validated prices (min = $0.80, max = $45.00)

### Step 2 — Revenue Computation
- Calculated revenue at transaction level
- Aggregated by product, product type, and category

### Step 3 — Product Popularity Analysis
- Counted total units sold per product
- Ranked products by sales volume
- Identified top 10 and bottom 10 performers

### Step 4 — Revenue Contribution Analysis
- Calculated total revenue per product
- Computed revenue share percentage
- Compared volume rank vs revenue rank

### Step 5 — Category & Product Type Analysis
- Aggregated revenue by category
- Analyzed product type contribution within categories

### Step 6 — Pareto Analysis (80/20 Rule)
- Calculated cumulative revenue percentage
- Identified products contributing 80% of revenue
- Classified revenue anchors vs long-tail products

### Step 7 — KPI Calculation
- Product Revenue Contribution %
- Product Sales Volume
- Category Revenue Share
- Revenue Concentration Ratio
- Product Efficiency Score (Revenue per Unit)

### Step 8 — Hero Product Identification
- Normalized volume, revenue, and efficiency scores
- Calculated composite Hero Score
- Ranked products by Hero Score

---

## 5. Analysis & Findings

### 5.1 Overall Revenue Summary

| KPI | Value |
|-----|-------|
| Total Revenue | $6,98,812.33 |
| Total Units Sold | 2,14,470 |
| Total Transactions | 1,49,116 |
| Average Revenue per Transaction | $4.69 |
| Highest Single Transaction | $360.00 |

---

### 5.2 Product Popularity Analysis

**Top 10 Best Selling Products:**

| Rank | Product | Units Sold |
|------|---------|------------|
| 1 | Earl Grey Rg | 4,708 |
| 2 | Dark Chocolate Lg | 4,668 |
| 3 | Morning Sunrise Chai Rg | 4,643 |
| 4 | Latte | 4,602 |
| 5 | Peppermint Rg | 4,564 |

**Bottom 5 Products:**

| Rank | Product | Units Sold |
|------|---------|------------|
| 76 | Jamaican Coffee River | 146 |
| 77 | Earl Grey | 142 |
| 78 | Guatemalan Sustainably Grown | 134 |
| 79 | Spicy Eye Opener Chai | 122 |
| 80 | Dark Chocolate | 118 |

**Key Finding:** Regular (Rg) and Large (Lg) sizes dominate top sellers. Small and no-size variants consistently underperform.

---

### 5.3 Revenue Contribution Analysis

**Top 5 Products by Revenue:**

| Product | Revenue | Share % |
|---------|---------|---------|
| Sustainably Grown Organic Lg | $21,151 | 3.03% |
| Dark Chocolate Lg | $21,006 | 3.01% |
| Latte Rg | $19,112 | 2.73% |
| Cappuccino Lg | $17,641 | 2.52% |
| Morning Sunrise Chai Lg | $17,384 | 2.49% |

**Key Finding:** Volume rank ≠ Revenue rank. Earl Grey Rg is #1 in volume but only #26 in revenue. Sustainably Grown Organic Lg is #1 in revenue despite lower volume — due to higher unit price.

---

### 5.4 Category Revenue Analysis

| Category | Revenue | Share % |
|----------|---------|---------|
| Coffee | $2,69,952 | 38.63% |
| Tea | $1,96,405 | 28.11% |
| Bakery | $82,315 | 11.78% |
| Drinking Chocolate | $72,416 | 10.36% |
| Coffee Beans | $40,085 | 5.74% |
| Branded | $13,607 | 1.95% |
| Loose Tea | $11,213 | 1.60% |
| Flavours | $8,408 | 1.20% |
| Packaged Chocolate | $4,407 | 0.63% |

**Key Finding:** Coffee + Tea = 66.74% of total revenue. Top 4 categories = 88.88% of revenue. Business is heavily dependent on Coffee and Tea.

---

### 5.5 Product Type Analysis

**Coffee Category:**
- Barista Espresso = 33.86% of coffee revenue
- Gourmet Brewed = 25.94%

**Tea Category:**
- Brewed Chai Tea = 39.25% of tea revenue

**Bakery Category:**
- Scones = 44.79% of bakery revenue

**Key Finding:** Drinking Chocolate has only 1 product type (Hot Chocolate = 100%). There is an opportunity to add variety.

---

### 5.6 Pareto Analysis

| Metric | Value |
|--------|-------|
| Total Products | 80 |
| Products for 80% Revenue | 42 |
| Menu % needed | 52.5% |
| Long-tail products | 38 (47.5%) |
| Long-tail revenue | ~20% |

**Key Finding:** This is not a classic 80/20 result. Revenue is well-distributed across products, indicating a healthy menu balance. However, 38 long-tail products still need review.

---

### 5.7 Hero Products

| Rank | Product | Hero Score | Revenue |
|------|---------|------------|---------|
| 1 | Dark Chocolate Lg | 69.5 | $21,006 |
| 2 | Sustainably Grown Organic Lg | 68.4 | $21,151 |
| 3 | Latte Rg | 65.1 | $19,112 |
| 4 | Latte | 62.6 | $17,257 |
| 5 | Morning Sunrise Chai Lg | 61.1 | $17,384 |

---

## 6. Key Insights

1. **Coffee is King** — 38.63% revenue share. Any disruption to coffee supply or quality will heavily impact business.

2. **Size Matters** — Regular (Rg) and Large (Lg) sizes dominate both volume and revenue. Small sizes underperform consistently.

3. **Volume ≠ Revenue** — Earl Grey Rg sells most units but ranks 26th in revenue. Price matters as much as popularity.

4. **Balanced Revenue** — 52.5% products drive 80% revenue (not classic 80/20). This shows good menu diversity.

5. **Dark Chocolate Lg is the True Hero** — Balanced across volume, revenue, and efficiency.

6. **Chocolate Variety Gap** — Drinking Chocolate has only 1 product type. New flavors could unlock additional revenue.

---

## 7. Recommendations

### Immediate Actions

| Action | Detail |
|--------|--------|
| Promote Hero Products | Dark Chocolate Lg, Sustainably Grown Organic Lg, Latte Rg |
| Review Bottom 10 | Consider removing or repricing Dark Chocolate (no size), Spicy Eye Opener Chai |
| Push Large Sizes | Customers prefer Lg/Rg — promote these sizes |
| Add Chocolate Variety | Only 1 type exists — new flavors can grow revenue |

### Strategic Actions

| Action | Detail |
|--------|--------|
| Protect Coffee & Tea | 66.74% revenue — maintain quality and supply |
| Simplify Menu | 80 items is too many — consider reducing to 60 |
| Price Optimization | Low-efficiency products may need price revision |
| Focus on Barista Espresso | 33.86% of coffee revenue — train staff, promote drinks |

---

## 8. Conclusion

This analysis successfully shifts focus from operational data to actionable product intelligence. By analyzing 1,49,116 transactions across 80 products and 3 stores, we identified clear revenue drivers, underperforming products, and strategic opportunities.

The key takeaway is that **data-driven menu decisions can directly improve revenue and operational efficiency** at Afficionado Coffee Roasters.

---

## 9. References

- Dataset: Afficionado Coffee Roasters Transaction Data (2025)
- Tools: Python 3.14, Pandas, Matplotlib, Seaborn, Plotly, Streamlit
- Internship: Unified Mentor Data Analyst Program
- Live Dashboard: https://afficionado-coffee-analysis-ip2nceibngh4brxb4av5iw.streamlit.app/

---

*Prepared by: Mohan Lal Kumawat | mohankumawat17@gmail.com*  
*LinkedIn: https://www.linkedin.com/in/mohan-kumawat-270125aa*
