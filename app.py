import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Teenage Pregnancy Advocacy Hub", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("Advocacy Navigation")
page = st.sidebar.radio("Go to:", ["Crisis Overview", "Regional Data (5 Regions)", "Action & Re-entry"])

st.sidebar.markdown("---")
st.sidebar.write("Focus: Eliminating Teenage Pregnancy")
st.sidebar.markdown("---")
st.sidebar.info("Advocacy Hub - 2026 Edition")

# 3. Page Content Logic
if page == "Crisis Overview":
    st.title("Addressing Teenage Pregnancy")
    st.markdown("### Mission: Data-Driven Action to Reduce Teenage Pregnancy in Northern Ghana")
    st.markdown("**The Reality:** Teenage pregnancy is the primary driver of school dropout for adolescent girls in our communities.")
    # Add your hero section text/stats here

elif page == "Regional Data (5 Regions)":
    st.title("Regional Data Dashboard")
    st.write("Visualizing regional trends in Northern Ghana.")
    # Add your charts and tables here

elif page == "Action & Re-entry":
    st.title("Action & Re-entry Plan")
    st.write("Details on how we are supporting girls to return to school.")
    # Add your advocacy plan table here