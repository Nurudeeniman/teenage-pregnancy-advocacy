import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Teenage Pregnancy Advocacy Hub", layout="wide")

# 2. Hero Section
st.title("Ending Teenage Pregnancy Through Education & Action")
st.markdown("### A data-driven advocacy initiative for Northern Ghana.")

col1, col2, col3 = st.columns(3)
with col1: st.button("📊 View Regional Data")
with col2: st.button("📢 Join the Advocacy")
with col3: st.button("🎓 Support Re-entry")

st.markdown("---")

# 3. Statistics Overview (Based on current trends)
st.subheader("📊 Key Impact Metrics")
m1, m2, m3, m4 = st.columns(4)
m1.metric("National Prevalence", "15.2%", "-0.5%")
m2.metric("Northern Vulnerability", "High", "Critical")
m3.metric("School Dropout Impact", "Primary Driver", "Urgent")
m4.metric("Target", "Universal Re-entry", "2030")

st.markdown("---")

# 4. Regional Comparison Dashboard
st.subheader("🗺️ Regional Prevalence Index (15-19 Years)")
# Data adjusted based on 2026/DHS research findings
data = {
    'Region': ['Northern', 'Savannah', 'North East', 'Upper East', 'Upper West'],
    'Prevalence_Index': [18.5, 17.8, 16.5, 15.2, 14.8]
}
df = pd.DataFrame(data)
fig = px.bar(df, x='Region', y='Prevalence_Index', color='Prevalence_Index', 
             color_continuous_scale='Reds', title="Estimated Teenage Pregnancy Index by Region")
st.plotly_chart(fig, width='stretch')

# 5. The Reality: Drivers and Consequences
c1, c2 = st.columns(2)
with c1:
    st.subheader("🩺 The Reality")
    st.markdown("""
    * **🎓 Educational Impact:** Premature school exit, loss of human capital.
    * **💼 Economic Consequences:** Cycle of poverty; limited lifetime earnings.
    * **🚫 Social Barriers:** Stigma, cultural norms, and misinformation.
    """)
    
with c2:
    st.subheader("🗣️ Voices From the Community")
    with st.expander("Read a story from Northern Ghana"):
        st.write("“I thought my education was over after childbirth, but community awareness of the Re-entry Policy gave me a second chance.”")

# 6. Strategic Action Plan (Tabs)
st.subheader("🎯 Strategic Action Plan")
tab1, tab2, tab3 = st.tabs(["Education", "Community Engagement", "Re-entry Support"])
tab1.write("Intensify sexual and reproductive health education (SRH) in all junior and senior high schools.")
tab2.write("Direct dialogues with traditional authorities and parents to eliminate stigma.")
tab3.write("Establishing local monitoring teams to track girls returning to school post-childbirth.")

# 7. Sources and Footer
st.markdown("---")
st.caption("Data Sources: Ghana Health Service (DHIMS-II), UNFPA Ghana, and recent Adolescent Health studies (2026).")