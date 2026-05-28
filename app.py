import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Configuration
st.set_page_config(page_title="Teenage Pregnancy Advocacy Hub", layout="wide")

# Sidebar for Navigation
st.sidebar.header("Advocacy Navigation")
page = st.sidebar.radio("Go to:", ["Crisis Overview", "Regional Data (5 Regions)", "Action & Re-entry"])

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.write("Focus: Eliminating Teenage Pregnancy")
st.sidebar.info("Advocacy Hub - 2026 Edition")

# --- Page Logic ---
if page == "Crisis Overview":
    st.title("🛡️ Advocacy Hub: Addressing Teenage Pregnancy")
    st.subheader("Mission: Data-Driven Action to Reduce Teenage Pregnancy in Northern Ghana")
    st.write("### The Reality")
    st.markdown("""
    Teenage pregnancy is the primary driver of school dropout for adolescent girls in our communities. 
    It is a multi-dimensional crisis:
    * **Health Risk:** Early pregnancy leads to higher maternal mortality risks.
    * **Educational Impact:** A cycle of premature school exit for thousands of girls.
    * **Economic Trap:** Lack of skills limits lifetime earning potential for young mothers.
    """)
    st.info("Our Goal: To reduce the rate of teenage pregnancy and ensure 100% re-entry for those who become pregnant.")

elif page == "Regional Data (5 Regions)":
    st.title("Regional Data Dashboard")
    st.write("### Prevalence Trends (Ages 15-19)")
    data = {
        'Region': ['Northern', 'Savannah', 'North East', 'Upper East', 'Upper West'],
        'Pregnancy_Index': [18.5, 17.2, 16.8, 15.0, 14.2]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Region', y='Pregnancy_Index', color='Pregnancy_Index', 
                 title="Estimated Teenage Pregnancy Prevalence Index (2026)")
    st.plotly_chart(fig, use_container_width=True)
    st.warning("These figures reflect the urgency of implementing the GES Re-entry Policy effectively.")

elif page == "Action & Re-entry":
    st.title("Action & Re-entry Plan")
    roadmap = pd.DataFrame({
        "Step": ["Community Awareness", "GES Re-entry Policy", "Support Systems", "Monitoring"],
        "Action": ["Engaging Parents/Chiefs", "Ensuring school access", "Providing childcare help", "Tracking return rates"],
        "Status": ["Active", "Pending", "Pending", "Not Started"]
    })
    st.table(roadmap)
    st.subheader("Your Call to Action")
    st.success("By using this dashboard, we pressure local stakeholders to move beyond talk and enforce the policy that allows girls back into the classroom.")