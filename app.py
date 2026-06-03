import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Configuration
st.set_page_config(page_title="Teenage Pregnancy Advocacy Hub", layout="wide")

# Sidebar for Navigation
st.sidebar.header("Advocacy Navigation")
page = st.sidebar.radio("Go to:", ["Crisis Overview", "Regional Data (5 Regions)", "Action & Re-entry", "Prevention & Awareness"])

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
    elif page == "Prevention & Awareness":
    st.title("💡 Prevention & Awareness")
    
    st.write("### Real-Life Scenarios")
    
    st.subheader("Scenario 1: The Pressure to Stay in School")
    st.write("""
    Aminata, a 15-year-old in Bimbila, is told by a suitor that marriage will provide 
    financial security for her family. Her teachers and community leaders intervene, 
    not just by talking, but by showing her parents a path to a scholarship that 
    keeps her in the classroom. **Prevention is providing an alternative path 
    before the pressure becomes a choice.**
    """)
    
    st.subheader("Scenario 2: Breaking the Silence")
    st.write("""
    A young girl in the community stops attending school. Instead of assuming she 
    is just 'bored,' a local volunteer visits her home, discovers she is facing 
    early pregnancy, and helps her navigate the process of keeping her education 
    alive through the re-entry policy. **Awareness is recognizing the signs 
    of dropout before the girl is lost to the system.**
    """)
    
    st.subheader("Scenario 3: Community-Led Advocacy")
    st.write("""
    A village chief, recognizing the high rate of dropouts in his area, publicly 
    declares that girls' education is a priority. He meets with local radio stations 
    to talk about the importance of reproductive health. When a community leader 
    speaks up, the stigma decreases, and families feel safer seeking help. 
    **Prevention is community-wide support that makes it easier to stay in school.**
    """)