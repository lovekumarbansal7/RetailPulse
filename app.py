import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("Data/Processed/cleaned_data.csv")

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("RetailPulse")

page = st.sidebar.radio(
    "Navigation",
    [
        " Home",
        " Sales Analytics",
        " Customer Segmentation",
        " Demand Forecasting",
        " Churn Prediction",
        " Inventory Optimization",
        " Reports"
    ]
)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

if page == " Home":

    st.title(" RetailPulse")

    st.subheader(
        "AI-Powered Customer Analytics & Demand Forecasting Platform"
    )

    st.markdown("---")

    st.markdown(
    """
    ##  Project Overview

    RetailPulse is an AI-powered retail analytics platform developed
    to help businesses analyze customers, forecast future demand,
    predict customer churn, and optimize inventory.

    ###  Project Objectives

    -  Analyze sales performance
    -  Segment customers using RFM Analysis & K-Means
    -  Forecast demand using Prophet & LSTM
    -  Predict customer churn using Machine Learning
    -  Optimize inventory based on forecasted demand

    ---
    """
    )

    st.subheader("🛠 Technologies Used")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("Python")
        st.success("Pandas")
        st.success("NumPy")

    with col2:
        st.success("Scikit-Learn")
        st.success("Prophet")
        st.success("PyTorch")

    with col3:
        st.success("Streamlit")
        st.success("Matplotlib")
        st.success("Seaborn")

    st.markdown("---")

    st.subheader(" Dashboard Modules")

    st.info("""
    
     Sales Analytics
    
     Customer Segmentation

     Demand Forecasting

     Churn Prediction

     Inventory Optimization

     Reports
    """)

    st.markdown("---")

    st.success("✅ RetailPulse Dashboard Loaded Successfully")

# -------------------------------------------------
# PLACEHOLDER PAGES
# -------------------------------------------------

elif page == " Sales Analytics":

    df = load_data()

    st.title(" Sales Analytics Dashboard")

    st.markdown("---")

    # ======================================
    # KPI CARDS
    # ======================================

    total_revenue = df["Sales"].sum()

    total_orders = df["Invoice"].nunique()

    total_customers = df["Customer ID"].nunique()

    avg_order_value = total_revenue / total_orders

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Revenue",
        f"${total_revenue:,.0f}"
    )

    col2.metric(
        "🛒 Orders",
        total_orders
    )

    col3.metric(
        "👥 Customers",
        total_customers
    )

    col4.metric(
        "📦 Avg Order",
        f"${avg_order_value:,.2f}"
    )

    st.markdown("---")

    # ======================================
    # DAILY SALES
    # ======================================

    daily_sales = (
        df.groupby(
            df["InvoiceDate"].dt.date
        )["Sales"]
        .sum()
        .reset_index()
    )

    daily_sales.columns = [
        "Date",
        "Revenue"
    ]

    st.subheader(" Daily Revenue Trend")

    st.line_chart(
        daily_sales.set_index("Date")
    )

    # ======================================
    # MONTHLY SALES
    # ======================================

    monthly_sales = (
        df.groupby(
            df["InvoiceDate"].dt.to_period("M")
        )["Sales"]
        .sum()
    )

    monthly_sales.index = monthly_sales.index.astype(str)

    st.subheader(" Monthly Revenue")

    st.bar_chart(
        monthly_sales
    )

    # ======================================
    # TOP COUNTRIES
    # ======================================

    country_sales = (
        df.groupby("Country")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader(" Top 10 Countries")

    st.bar_chart(country_sales)

    # ======================================
    # TOP PRODUCTS
    # ======================================

    product_sales = (
        df.groupby("Description")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader(" Top 10 Products")

    st.bar_chart(product_sales)

    # ======================================
    # DATA PREVIEW
    # ======================================

    st.markdown("---")

    with st.expander("📄 View Dataset"):

        st.dataframe(df.head(31))



elif page == " Customer Segmentation":

    st.title(" Customer Segmentation Dashboard")

    st.markdown("---")

    # ==============================
    # LOAD DATA
    # ==============================

    segment_df = pd.read_csv(
        "Data/Processed/customer_segments.csv"
    )

    # ==============================
    # KPI CARDS
    # ==============================

    total_customers = len(segment_df)

    total_segments = segment_df["Cluster"].nunique()

    largest_segment = segment_df["Segment"].value_counts().idxmax()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Total Customers",
        total_customers
    )

    col2.metric(
        "📊 Total Segments",
        total_segments
    )

    col3.metric(
        "🏆 Largest Segment",
        largest_segment
    )

    st.markdown("---")

    # ==============================
    # SEGMENT DISTRIBUTION
    # ==============================

    st.subheader(" Customer Segment Distribution")

    segment_counts = (
        segment_df["Segment"]
        .value_counts()
    )

    st.bar_chart(segment_counts)

    # ==============================
    # RFM AVERAGES
    # ==============================

    st.markdown("---")

    st.subheader(" Average RFM Values by Segment")

    rfm_summary = (
        segment_df
        .groupby("Segment")[["Recency","Frequency","Monetary"]]
        .mean()
        .round(2)
    )

    st.dataframe(rfm_summary)



    # ==============================
    # CUSTOMER TABLE
    # ==============================

    st.markdown("---")

    st.subheader(" Customer Information")

    st.dataframe(
        segment_df
    )

    # ==============================
    # BUSINESS INSIGHTS
    # ==============================

    st.markdown("---")

    st.subheader("💡 Business Insights")

    insights = """
    ### Customer Segments

    🟢 **VIP Customers**
    - High spending
    - Frequent purchases
    - Highest business value

    🟡 **Loyal Customers**
    - Purchase regularly
    - Good retention potential

    🟠 **Regular Customers**
    - Moderate spending
    - Can be converted into loyal customers

    🔴 **At Risk Customers**
    - Long time since last purchase
    - Need targeted marketing campaigns

    ⚫ **Lost Customers**
    - Inactive customers
    - Re-engagement offers recommended
    """

    st.info(insights)



elif page == " Demand Forecasting":

    st.title(" Demand Forecasting Dashboard")

    st.markdown("---")

    # =====================================
    # LOAD DATA
    # =====================================

    forecast_df = pd.read_csv(
        "Data/Processed/lstm_forecast.csv"
    )

    comparison_df = pd.read_csv(
        "Data/Processed/model_comparison.csv"
    )

    # =====================================
    # KPI CARDS
    # =====================================

    best_model = comparison_df.loc[
        comparison_df["MAPE (%)"].idxmin(),
        "Model"
    ]

    best_mape = comparison_df["MAPE (%)"].min()

    best_rmse = comparison_df.loc[
        comparison_df["MAPE (%)"].idxmin(),
        "RMSE"
    ]

    best_mae = comparison_df.loc[
        comparison_df["MAPE (%)"].idxmin(),
        "MAE"
    ]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🏆 Best Model",
        best_model
    )

    col2.metric(
        "📉 MAE",
        f"{best_mae:,.2f}"
    )

    col3.metric(
        "📈 RMSE",
        f"{best_rmse:,.2f}"
    )

    col4.metric(
        "🎯 MAPE",
        f"{best_mape:.2f}%"
    )

    st.markdown("---")

    # =====================================
    # ACTUAL VS PREDICTED
    # =====================================

    st.subheader(" Actual vs Predicted Sales")

    chart_data = forecast_df.set_index("Date")[
        ["Actual Sales", "Predicted Sales"]
    ]

    st.line_chart(chart_data)

    # =====================================
    # MODEL COMPARISON
    # =====================================

    st.markdown("---")

    st.subheader(" Model Comparison")

    st.dataframe(comparison_df)

    # =====================================
    # DOWNLOAD
    # =====================================

    st.markdown("---")

    st.download_button(
        label=" Download Forecast",
        data=forecast_df.to_csv(index=False),
        file_name="lstm_forecast.csv",
        mime="text/csv"
    )

    # =====================================
    # BUSINESS INSIGHTS
    # =====================================

    st.markdown("---")

    st.subheader("💡 Business Insights")

    st.success(f"""
    ### Forecast Summary

    ✅ Prophet and Multivariate LSTM models were developed for demand forecasting.

    ✅ The **{best_model}** achieved the best performance.

    **Performance**

    • MAE : {best_mae:.2f}

    • RMSE : {best_rmse:.2f}

    • MAPE : {best_mape:.2f}%

    The LSTM model captures sales trends more effectively than Prophet and has been selected as the final forecasting model for RetailPulse.
    """)
    


elif page == " Churn Prediction":

    st.title(" Churn Prediction Dashboard")

    st.markdown("---")

    # =====================================
    # KPI CARDS
    # =====================================

    accuracy = 99.91
    roc_auc = 1.00
    total_customers = 5878
    churn_rate = 40.83

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🎯 Accuracy",
        f"{accuracy:.2f}%"
    )

    col2.metric(
        "📈 ROC-AUC",
        f"{roc_auc:.2f}"
    )

    col3.metric(
        "👥 Customers",
        total_customers
    )

    col4.metric(
        "❤️ Churn Rate",
        f"{churn_rate:.2f}%"
    )

    st.markdown("---")

    # =====================================
    # CHURN DISTRIBUTION
    # =====================================

    churn_df = pd.DataFrame({

        "Category":[
            "Active",
            "Churned"
        ],

        "Customers":[
            3478,
            2400
        ]

    })

    fig = px.pie(

        churn_df,

        names="Category",

        values="Customers",

        hole=0.45,

        color="Category",

        color_discrete_sequence=[
            "#2ecc71",
            "#e74c3c"
        ]

    )

    fig.update_layout(
        title="Customer Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================

    feature_df = pd.DataFrame({

        "Feature":[
            "Recency",
            "Frequency",
            "Monetary"
        ],

        "Importance":[
            0.85,
            0.08,
            0.07
        ]

    })

    fig2 = px.bar(

        feature_df,

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        color_continuous_scale="Blues"

    )

    fig2.update_layout(
        title="Feature Importance"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =====================================
    # MODEL PERFORMANCE
    # =====================================

    st.markdown("---")

    st.subheader(" Model Performance")

    performance = pd.DataFrame({

        "Metric":[
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
            "ROC-AUC"
        ],

        "Value":[
            99.91,
            100,
            99.79,
            99.90,
            1.00
        ]

    })

    st.dataframe(
        performance,
        use_container_width=True
    )

    # =====================================
    # BUSINESS INSIGHTS
    # =====================================

    st.markdown("---")

    st.subheader("💡 Business Insights")

    st.success("""

    ### Customer Churn Summary

    • Random Forest classifier was developed to identify customers at risk of churn.

    • Customers were labeled using Recency > 180 days.

    • Recency is the strongest indicator of churn.

    ### Recommendations

    ✅ Reward loyal customers

    ✅ Send promotional offers to at-risk customers

    ✅ Re-engage inactive customers through personalized campaigns

    """)

elif page == " Inventory Optimization":

    st.title(" Inventory Optimization Dashboard")

    st.markdown("---")

    # ============================================
    # LOAD FORECAST
    # ============================================

    inventory_df = pd.read_csv(
        "Data/Processed/lstm_forecast.csv"
    )

    inventory_df["Date"] = pd.to_datetime(
        inventory_df["Date"]
    )

    # ============================================
    # USER INPUTS
    # ============================================

    st.subheader("⚙ Inventory Planning")

    col1, col2, col3 = st.columns(3)

    with col1:

        selected_date = st.selectbox(

            "Forecast Date",

            inventory_df["Date"].dt.strftime("%Y-%m-%d")

        )

    with col2:

        lead_time = st.slider(

            "Lead Time (Days)",

            1,

            30,

            7

        )

    with col3:

        service_level = st.selectbox(

            "Service Level",

            ["90%", "95%", "99%"]

        )

    # ============================================
    # SERVICE FACTOR
    # ============================================

    if service_level == "90%":

        z = 1.28

    elif service_level == "95%":

        z = 1.65

    else:

        z = 2.33

    # ============================================
    # SELECT FORECAST
    # ============================================

    selected_row = inventory_df[
        inventory_df["Date"].dt.strftime("%Y-%m-%d") == selected_date
    ]

    forecast_demand = float(
        selected_row["Predicted Sales"].values[0]
    )

    demand_std = inventory_df[
        "Predicted Sales"
    ].std()

    # ============================================
    # INVENTORY CALCULATIONS
    # ============================================

    safety_stock = z * demand_std * np.sqrt(lead_time)

    reorder_point = (

        forecast_demand * lead_time

        +

        safety_stock

    )

    recommended_order = forecast_demand * lead_time

    # ============================================
    # KPI CARDS
    # ============================================

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "Forecast Demand",

        f"{forecast_demand:,.0f}"

    )

    c2.metric(

        "Safety Stock",

        f"{safety_stock:,.0f}"

    )

    c3.metric(

        "Reorder Point",

        f"{reorder_point:,.0f}"

    )

    c4.metric(

        "Recommended Order",

        f"{recommended_order:,.0f}"

    )

    # ============================================
    # INVENTORY VISUALIZATION
    # ============================================

    st.markdown("---")

    chart_df = pd.DataFrame({

        "Metric":[

            "Forecast",

            "Safety Stock",

            "ROP",

            "Order Qty"

        ],

        "Value":[

            forecast_demand,

            safety_stock,

            reorder_point,

            recommended_order

        ]

    })

    fig = px.bar(

        chart_df,

        x="Metric",

        y="Value",

        color="Metric",

        text_auto=".0f"

    )

    fig.update_layout(

        title="Inventory Planning Metrics"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ============================================
    # RECOMMENDATION
    # ============================================

    st.markdown("---")

    st.subheader("📋 Recommendation")

    st.success(

    f"""
    ### Inventory Recommendation

    Forecast Date : **{selected_date}**

    Forecast Demand : **{forecast_demand:,.0f} units**

    Lead Time : **{lead_time} days**

    Service Level : **{service_level}**

    Safety Stock : **{safety_stock:,.0f} units**

    Reorder Point : **{reorder_point:,.0f} units**

    Recommended Order Quantity : **{recommended_order:,.0f} units**

    **Recommendation**

    Place a replenishment order when inventory falls below the Reorder Point to maintain the selected service level and reduce the risk of stockouts.

    """
        )

elif page == " Reports":

    st.title(" Reports & Downloads")

    st.markdown("---")

    st.write(
        """
        Download the processed datasets and model outputs
        generated during the RetailPulse analysis.
        """
    )

    # ==========================================
    # LOAD FILES
    # ==========================================

    customer_segments = pd.read_csv(
        "Data/Processed/customer_segments.csv"
    )

    lstm_forecast = pd.read_csv(
        "Data/Processed/lstm_forecast.csv"
    )

    model_comparison = pd.read_csv(
        "Data/Processed/model_comparison.csv"
    )

    inventory_summary = pd.read_csv(
        "Data/Processed/inventory_summary.csv"
    )

    # ==========================================
    # CUSTOMER SEGMENTS
    # ==========================================

    st.subheader(" Customer Segments")

    st.dataframe(customer_segments.head())

    st.download_button(
        label=" Download Customer Segments",
        data=customer_segments.to_csv(index=False),
        file_name="customer_segments.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # ==========================================
    # LSTM FORECAST
    # ==========================================

    st.subheader(" Demand Forecast")

    st.dataframe(lstm_forecast.head())

    st.download_button(
        label=" Download Forecast",
        data=lstm_forecast.to_csv(index=False),
        file_name="lstm_forecast.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # ==========================================
    # MODEL COMPARISON
    # ==========================================

    st.subheader(" Model Comparison")

    st.dataframe(model_comparison)

    st.download_button(
        label=" Download Model Comparison",
        data=model_comparison.to_csv(index=False),
        file_name="model_comparison.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # ==========================================
    # INVENTORY SUMMARY
    # ==========================================

    st.subheader(" Inventory Summary")

    st.dataframe(inventory_summary)

    st.download_button(
        label="📥 Download Inventory Summary",
        data=inventory_summary.to_csv(index=False),
        file_name="inventory_summary.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.success(
        """
        ✔ All reports are available for download.

        These files can be used for:

        • Business Reporting

        • Future Analysis

        • Decision Making

        • Presentation Purposes
        """
    )