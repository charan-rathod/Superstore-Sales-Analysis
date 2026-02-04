import streamlit as st


def apply_filters(df):

    st.sidebar.header("🔎 Filter Data")

    region = st.sidebar.multiselect(
        "Region",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

    category = st.sidebar.multiselect(
        "Category",
        options=df['Category'].unique(),
        default=df['Category'].unique()
    )

    segment = st.sidebar.multiselect(
        "Segment",
        options=df['Segment'].unique(),
        default=df['Segment'].unique()
    )

    # Date filter
    start_date = st.sidebar.date_input(
        "Start Date",
        df['Order Date'].min()
    )

    end_date = st.sidebar.date_input(
        "End Date",
        df['Order Date'].max()
    )

    filtered_df = df[
        (df['Region'].isin(region)) &
        (df['Category'].isin(category)) &
        (df['Segment'].isin(segment)) &
        (df['Order Date'] >= str(start_date)) &
        (df['Order Date'] <= str(end_date))
    ]

    return filtered_df


# ================= KPI =================

def show_kpis(df):

    st.subheader("📊 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Total Sales", f"${df['Sales'].sum():,.0f}")
    col2.metric("📈 Total Profit", f"${df['Profit'].sum():,.0f}")
    col3.metric("📦 Orders", df.shape[0])
    col4.metric("🏷 Avg Discount", f"{df['Discount'].mean()*100:.1f}%")



# ================= Charts =================

def monthly_sales(df):

    st.subheader("📅 Monthly Sales Trend")

    monthly = df.resample('M', on='Order Date')['Sales'].sum()

    st.line_chart(monthly)



def sales_by_category(df):

    st.subheader("🛒 Sales by Category")

    cat = df.groupby('Category')['Sales'].sum()

    st.bar_chart(cat)



def profit_by_region(df):

    st.subheader("🌎 Profit by Region")

    region = df.groupby('Region')['Profit'].sum()

    st.bar_chart(region)



# ================= Smart Insight =================

def profit_warning(df):

    loss_products = df.groupby('Sub-Category')['Profit'].sum()

    loss_products = loss_products[loss_products < 0]

    if not loss_products.empty:

        st.error("⚠️ Some sub-categories are generating LOSS!")

        st.dataframe(loss_products.sort_values())

    else:
        st.success("✅ No loss-making categories detected!")
