# ============================================================
# Afficionado Coffee Roasters - Analytics Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Afficionado Coffee Analytics",
    page_icon="☕",
    layout="wide"
)

# ============================================================
# Load Data
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_excel('Afficionado Coffee Roasters.xlsx')
    df['revenue'] = df['transaction_qty'] * df['unit_price']
    return df

df = load_data()

# ============================================================
# Sidebar Filters
# ============================================================

st.sidebar.title("☕ Coffee Analytics")
st.sidebar.markdown("---")

all_categories = ['All'] + sorted(df['product_category'].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", all_categories)

all_stores = ['All'] + sorted(df['store_location'].unique().tolist())
selected_store = st.sidebar.selectbox("Select Store", all_stores)

top_n = st.sidebar.slider("Top N Products", min_value=5, max_value=20, value=10)

st.sidebar.markdown("---")
st.sidebar.markdown("**Unified Mentor Internship**")
st.sidebar.markdown("Data Analyst Project")

# ============================================================
# Apply Filters
# ============================================================

filtered_df = df.copy()
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['product_category'] == selected_category]
if selected_store != 'All':
    filtered_df = filtered_df[filtered_df['store_location'] == selected_store]

# ============================================================
# Main Title
# ============================================================

st.title("☕ Afficionado Coffee Roasters")
st.subheader("Product Optimization & Revenue Contribution Analysis")
st.markdown("---")

# ============================================================
# KPI Cards
# ============================================================

st.header("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.0f}")

with col2:
    st.metric("Total Transactions", f"{len(filtered_df):,}")

with col3:
    st.metric("Total Units Sold", f"{filtered_df['transaction_qty'].sum():,}")

with col4:
    st.metric("Avg Revenue/Transaction", f"${filtered_df['revenue'].mean():.2f}")

st.markdown("---")

# ============================================================
# Product Popularity Analysis
# ============================================================

st.header("🏆 Product Popularity Analysis")

col1, col2 = st.columns(2)

# Top N Products by Volume
product_vol = filtered_df.groupby('product_detail')['transaction_qty'].sum()
product_vol = product_vol.reset_index()
product_vol.columns = ['Product', 'Units Sold']
product_vol = product_vol.sort_values('Units Sold', ascending=False).head(top_n)

with col1:
    fig1 = px.bar(product_vol, x='Units Sold', y='Product',
                  orientation='h', title=f'Top {top_n} Products by Volume',
                  color='Units Sold', color_continuous_scale='Blues')
    fig1.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)

# Top N Products by Revenue
product_rev = filtered_df.groupby('product_detail')['revenue'].sum()
product_rev = product_rev.reset_index()
product_rev.columns = ['Product', 'Revenue']
product_rev = product_rev.sort_values('Revenue', ascending=False).head(top_n)

with col2:
    fig2 = px.bar(product_rev, x='Revenue', y='Product',
                  orientation='h', title=f'Top {top_n} Products by Revenue',
                  color='Revenue', color_continuous_scale='Greens')
    fig2.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ============================================================
# Category Analysis
# ============================================================

st.header("📂 Category Revenue Analysis")

col1, col2 = st.columns(2)

category_rev = filtered_df.groupby('product_category')['revenue'].sum().reset_index()
category_rev.columns = ['Category', 'Revenue']
category_rev = category_rev.sort_values('Revenue', ascending=False)

with col1:
    fig3 = px.pie(category_rev, values='Revenue', names='Category',
                  title='Revenue Share by Category',
                  color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.bar(category_rev, x='Category', y='Revenue',
                  title='Revenue by Category',
                  color='Revenue', color_continuous_scale='Oranges')
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ============================================================
# Pareto Analysis
# ============================================================

st.header("📉 Pareto Analysis (80/20 Rule)")

pareto = filtered_df.groupby('product_detail')['revenue'].sum().reset_index()
pareto.columns = ['Product', 'Revenue']
pareto = pareto.sort_values('Revenue', ascending=False).reset_index(drop=True)
pareto['Cumulative %'] = (pareto['Revenue'].cumsum() / pareto['Revenue'].sum() * 100).round(2)

fig5 = go.Figure()
fig5.add_trace(go.Bar(
    x=pareto['Product'], y=pareto['Revenue'],
    name='Revenue', marker_color='steelblue', opacity=0.7
))
fig5.add_trace(go.Scatter(
    x=pareto['Product'], y=pareto['Cumulative %'],
    name='Cumulative %', yaxis='y2',
    line=dict(color='red', width=2.5)
))
fig5.add_hline(y=80, line_dash='dash', line_color='orange',
               annotation_text='80% Threshold', yref='y2')
fig5.update_layout(
    title='Pareto Analysis — Revenue Concentration',
    yaxis=dict(title='Revenue ($)'),
    yaxis2=dict(title='Cumulative %', overlaying='y', side='right', range=[0, 110]),
    xaxis=dict(showticklabels=False),
    legend=dict(x=0.01, y=0.99)
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# ============================================================
# Product Drill Down Table
# ============================================================

st.header("🔍 Product Performance Table")

product_table = filtered_df.groupby('product_detail').agg(
    Units_Sold=('transaction_qty', 'sum'),
    Total_Revenue=('revenue', 'sum'),
    Transactions=('transaction_id', 'count')
).reset_index()

product_table['Revenue_Share_%'] = (
    product_table['Total_Revenue'] /
    product_table['Total_Revenue'].sum() * 100
).round(2)

product_table['Efficiency_Score'] = (
    product_table['Total_Revenue'] /
    product_table['Units_Sold']
).round(2)

product_table = product_table.sort_values('Total_Revenue', ascending=False)
product_table.columns = ['Product', 'Units Sold', 'Total Revenue',
                          'Transactions', 'Revenue Share %', 'Efficiency Score']

st.dataframe(product_table, use_container_width=True, height=400)

st.markdown("---")
st.markdown("**Built by Mohan Lal Kumawat | Unified Mentor Internship | Data Analyst Project**")