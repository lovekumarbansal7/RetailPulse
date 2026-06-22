# RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

## Overview

RetailPulse is an end-to-end retail analytics platform designed to help businesses understand customer behavior, identify high-value customers, forecast product demand, and improve decision-making through data-driven insights.

The project uses the Online Retail II dataset containing over 1 million retail transactions and applies machine learning techniques for customer segmentation and demand forecasting.

---

## Objectives

* Analyze retail sales data
* Segment customers using RFM Analysis
* Identify VIP, Loyal, Regular, At-Risk, and Lost customers
* Forecast future product demand
* Support inventory optimization
* Build an interactive analytics dashboard

---

## Dataset

**Dataset:** Online Retail II

**Original Records:** 1,067,371

**Records After Cleaning:** 779,425

**Unique Customers:** 5,878

Features:

* Invoice
* StockCode
* Description
* Quantity
* InvoiceDate
* Price
* Customer ID
* Country

---

## Work Completed

### 1. Data Cleaning

Performed the following preprocessing steps:

* Removed missing Customer IDs
* Removed cancelled/returned transactions (Quantity ≤ 0)
* Removed invalid prices (Price ≤ 0)
* Removed duplicate records
* Converted InvoiceDate to datetime format
* Created Sales feature

### 2. Exploratory Data Analysis

Completed:

* Missing Value Analysis
* Quantity Distribution Analysis
* Price Distribution Analysis
* Sales Distribution Analysis
* Outlier Detection using Boxplots
* Correlation Heatmap
* Top 10 Products by Revenue
* Top 10 Countries by Revenue
* Monthly Sales Trend Analysis

### 3. RFM Analysis

Created customer-level features:

* Recency
* Frequency
* Monetary

Generated RFM table for 5,878 customers.

### 4. Customer Segmentation

Applied:

* Log Transformation
* StandardScaler
* K-Means Clustering

Evaluation:

* Elbow Method used for cluster selection
* Selected K = 5
* Silhouette Score = 0.342

Customer Segments:

| Segment           | Customers |
| ----------------- | --------- |
| VIP Customers     | 458       |
| Loyal Customers   | 1294      |
| Regular Customers | 1143      |
| At-Risk Customers | 1363      |
| Lost Customers    | 1620      |


## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## Current Progress

### Completed

* Data Cleaning
* Exploratory Data Analysis
* RFM Analysis
* Customer Segmentation

### Upcoming

* Time Series Analysis
* Demand Forecasting (Prophet)
* Demand Forecasting (LSTM)
* Inventory Optimization
* MLflow Tracking
* Streamlit Dashboard
* Deployment

---

## Author

LOVE KUMAR BANSAL

B.Tech Electronics & Communication Engineering

SKIT Jaipur

2027
