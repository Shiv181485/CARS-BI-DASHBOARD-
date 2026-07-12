import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cars Analytics Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("🚗 Cars Analytics Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "📁 Dataset", "📥 Download"]
)

# ---------------- Load Dataset ----------------
@st.cache_data
def load_data():
    return pd.read_csv("CARS.csv")

df = load_data()

# ---------------- Home ----------------
if page == "🏠 Home":

    st.title("🚗 Cars Analytics Dashboard")

    st.markdown("""
### 📊 Power BI Business Intelligence Project

This dashboard analyzes automobile data using **Power BI**, **Power Query**, and **DAX** to generate business insights.

### ✨ Features
- 🚗 Manufacturer Analysis
- 💰 MSRP & Invoice Analysis
- ⚙️ Engine Performance
- ⛽ Fuel Efficiency
- 🌍 Origin Analysis
- 📈 Interactive Visualizations
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🚗 Total Cars", len(df))
    c2.metric("🏭 Manufacturers", df["Make"].nunique())
    c3.metric("🌍 Origins", df["Origin"].nunique())
    c4.metric("🚘 Types", df["Type"].nunique())

# ---------------- Dashboard ----------------
elif page == "📊 Dashboard":

    st.title("📊 Dashboard Preview")

    st.subheader("🏠 Executive Dashboard")
    st.image("page1.png", use_container_width=True)

    st.subheader("🚘 Performance Dashboard")
    st.image("page2.png", use_container_width=True)

    st.subheader("🏎 Premium Vehicle Dashboard")
    st.image("page3.png", use_container_width=True)

# ---------------- Dataset ----------------
elif page == "📁 Dataset":

    st.title("📁 Cars Dataset")

    st.dataframe(df, use_container_width=True)

    st.markdown("### Dataset Statistics")

    st.write(df.describe())

# ---------------- Download ----------------
else:

    st.title("📥 Download Project")

    with open("cars 1.pbix", "rb") as f:
        st.download_button(
            label="⬇ Download Power BI Project",
            data=f,
            file_name="Cars_Analytics_Dashboard.pbix",
            mime="application/octet-stream"
        )

    with open("CARS.csv", "rb") as f:
        st.download_button(
            label="⬇ Download Dataset",
            data=f,
            file_name="CARS.csv",
            mime="text/csv"
        )

st.markdown("---")

st.markdown(
    """
<div align='center'>

### 🚗 Cars Analytics Dashboard

Built with ❤️ using **Power BI**, **DAX**, **Power Query**, and **Streamlit**

</div>
""",
unsafe_allow_html=True)
