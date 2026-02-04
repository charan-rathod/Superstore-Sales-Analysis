import streamlit as st
from utils import load_data
from analysis_module import (
    apply_filters,
    show_kpis,
    monthly_sales,
    sales_by_category,
    profit_by_region,
    profit_warning
)

st.set_page_config(
    page_title="Smart Sales Dashboard",
    layout="wide"
)

st.title("🚀 Smart Sales Analytics Dashboard")

st.write("Upload your dataset and get instant business insights.")

uploaded_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("✅ Data Loaded Successfully!")

    filtered_df = apply_filters(df)

    if filtered_df.empty:
        st.warning("No data available for selected filters.")
        st.stop()

    # KPIs
    show_kpis(filtered_df)

    st.divider()

    # Charts
    monthly_sales(filtered_df)
    sales_by_category(filtered_df)
    profit_by_region(filtered_df)

    st.divider()

    # Smart AI-like Insight
    profit_warning(filtered_df)

    st.divider()

    # Download report
    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Filtered Report",
        csv,
        "sales_report.csv",
        "text/csv"
    )

else:
    st.info("👆 Upload a CSV file to begin analysis.")
