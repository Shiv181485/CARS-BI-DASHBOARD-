import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="🚗 Cars Analytics Dashboard",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# Functions
# -----------------------------
@st.cache_data
def load_data():
    if not os.path.exists("CARS.csv"):
        return None
    return pd.read_csv("CARS.csv")

df = load_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚗 Cars Analytics")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📁 Dataset",
        "📥 Download"
    ]
)

# -----------------------------
# HOME
# -----------------------------
if page == "🏠 Home":

    st.title("🚗 Cars Analytics Dashboard")

    st.markdown("""
Analyze vehicle pricing, fuel efficiency, engine performance,
manufacturer trends and market insights using **Power BI**.
""")

    if df is not None:

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🚗 Total Cars", len(df))
        c2.metric("🏭 Manufacturers", df["Make"].nunique())
        c3.metric("🌍 Origins", df["Origin"].nunique())
        c4.metric("🚘 Types", df["Type"].nunique())

        st.markdown("---")

        st.subheader("Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

    else:
        st.error("CARS.csv not found.")

# -----------------------------
# DASHBOARD
# -----------------------------
elif page == "📊 Dashboard":

    st.title("📊 Dashboard Screens")

    images = [
        ("Executive Dashboard", "page1.png"),
        ("Performance Dashboard", "page2.png"),
        ("Premium Dashboard", "page3.png")
    ]

    for title, img in images:

        st.subheader(title)

        if os.path.exists(img):
            st.image(img, use_container_width=True)
        else:
            st.warning(f"{img} not found")

# -----------------------------
# DATASET
# -----------------------------
elif page == "📁 Dataset":

    st.title("📁 Cars Dataset")

    if df is not None:
        st.dataframe(df, use_container_width=True)

        st.subheader("Statistics")
        st.write(df.describe())
    else:
        st.error("Dataset not found.")

# -----------------------------
# DOWNLOADS
# -----------------------------
elif page == "📥 Download":

    st.title("📥 Downloads")

    if os.path.exists("cars 1.pbix"):
        with open("cars 1.pbix", "rb") as file:
            st.download_button(
                "⬇ Download Power BI (.pbix)",
                file,
                file_name="Cars_Analytics_Dashboard.pbix"
            )
    else:
        st.warning("PBIX file not found.")

    if os.path.exists("CARS.csv"):
        with open("CARS.csv", "rb") as file:
            st.download_button(
                "⬇ Download Dataset",
                file,
                file_name="CARS.csv"
            )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
"""
<div align='center'>

### 🚗 Cars Analytics Dashboard

Built with ❤️ using Power BI • DAX • Power Query • Streamlit

</div>
""",
unsafe_allow_html=True
)
