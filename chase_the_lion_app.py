import streamlit as st
import pandas as pd
import datetime
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Chase the Lion - High Performance Tracker",
    page_icon="🦁",
    layout="wide"
)

# --- Sidebar Navigation ---
st.sidebar.title("🦁 Chase the Lion")
st.sidebar.markdown("### High-Performance Command Center")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Peptide Protocol & Tracker",
        "Daily Review & Reflection Log",
        "Google Calendar & Daily Schedule"
    ]
)

# ==========================================
# MODULE 1: PEPTIDE PROTOCOL & TRACKER
# ==========================================
if menu == "Peptide Protocol & Tracker":
    st.header("🧬 Peptide Protocol & Daily Injection Tracker")
    
    st.write("""
    **Current Protocol Specifications:**
    - **Compound:** BPC-157 / TB-500 Blend (Tissue Repair, Joint Regeneration, Anti-Inflammatory)
    - **Dosage:** 250 mcg (0.25 mg) Subcutaneously Daily
    - **Timing:** Administer in the morning on an empty stomach or post-workout near target joint/site.
    """)
    
    peptide_file = "chase_the_lion_peptide_history.csv"
    
    # Initialize session state for peptide tracking
    if 'peptide_logs' not in st.session_state:
        st.session_state.peptide_logs = []
        
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        admin_date = st.date_input("Administration Date", datetime.date.today(), key="pep_date")
        dose_mcg = st.number_input("Dosage (mcg)", value=250, step=50, key="pep_dose")
        site = st.selectbox(
            "Injection Site / Focus Area", 
            [
                "Left Shoulder / Rotator Cuff", 
                "Right Shoulder / Rotator Cuff", 
                "Left Knee / Patellar Tendon", 
                "Right Knee / Patellar Tendon", 
                "Lower Back / Lumbar", 
                "Subcutaneous Abdomen (Systemic)"
            ], 
            key="pep_site"
        )
    with p_col2:
        fasted = st.checkbox("Administered Fasted (Morning)", value=True, key="pep_fasted")
        joint_pain_scale = st.slider("Joint Pain / Stiffness Level (1 = None, 10 = Severe)", min_value=1, max_value=10, value=3, key="pep_pain")
        pep_notes = st.text_input("Protocol Notes (Recovery response, site reaction):", value="Felt great, minor tendon relief.", key="pep_notes")
        
    if st.button("💉 Log Peptide Administration"):
        pep_entry = {
            "Date": admin_date.strftime("%Y-%m-%d"),
            "Dose (mcg)": dose_mcg,
            "Site": site,
            "Fasted": fasted,
            "Joint Pain (1-10)": joint_pain_scale,
            "Notes": pep_notes
        }
        df_pep = pd.DataFrame([pep_entry])
        if os.path.exists(peptide_file):
            df_pep.to_csv(peptide_file, mode='a', header=False, index=False)
        else:
            df_pep.to_csv(peptide_file, mode='w', header=True, index=False)
        st.success("✅ Peptide dose logged successfully to permanent history!")
        
    if os.path.exists(peptide_file):
        st.subheader("📜 Peptide Protocol History")
        df_pep_hist = pd.read_csv(peptide_file)
        st.dataframe(df_pep_hist, use_container_width=True)

# ==========================================
# MODULE 2: DAILY REVIEW & REFLECTION LOG
# ==========================================
elif menu == "Daily Review & Reflection Log":
    st.header("🙏 Daily Review & Faith Reflection Log")
    st.write("End-of-day spiritual and mental debrief. Align your heart and mind with the mission.")
    
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    review_file = "chase_the_lion_daily_reviews.csv"
    
    wins = st.text_area("1. What were today's biggest victories (physical, spiritual, or mental)?", placeholder="e.g. Hit heavy overhead press, maintained 100% clean nutrition.")
    battles = st.text_area("2. Where did I face friction, temptation, or weakness today?", placeholder="e.g. Felt fatigue during afternoon slump, but pushed through work.")
    gratitude = st.text_area("3. What am I deeply grateful for today?", placeholder="e.g. Strength, health, family, and God's unwavering grace.")
    tomorrow_goal = st.text_input("4. One primary mission for tomorrow:", value="Attack 5 AM workout with lionhearted intensity and zero excuses.")
    
    if st.button("💾 Save Daily Reflection & Review"):
        review_entry = {
            "Date": today_str,
            "Victories": wins,
            "Battles Fought": battles,
            "Gratitude": gratitude,
            "Tomorrow's Mission": tomorrow_goal
        }
        df_rev = pd.DataFrame([review_entry])
        if os.path.exists(review_file):
            df_rev.to_csv(review_file, mode='a', header=False, index=False)
        else:
            df_rev.to_csv(review_file, mode='w', header=True, index=False)
        st.success("✅ Daily Reflection saved successfully!")
        
    if os.path.exists(review_file):
        st.subheader("📜 Past Daily Reflections")
        df_rev_hist = pd.read_csv(review_file)
        st.dataframe(df_rev_hist, use_container_width=True)

# ==========================================
# MODULE 3: GOOGLE CALENDAR & SCHEDULE
# ==========================================
elif menu == "Google Calendar & Daily Schedule":
    st.header("📅 Google Calendar & Daily Tactical Schedule")
    st.write("Align your daily calendar events with your high-performance routine.")
    
    st.markdown("""
    ### 🦁 Daily Routine Timeline (The Lionhearted Schedule)
    - **4:15 AM — Wake Up & Fuel:** Pre-workout meal (Oats + Protein / Fruit) + Electrolytes.
    - **5:00 AM — 6:30 AM — Iron Temple (Lift Engine):** Execute daily training block (Phase & Week matrix).
    - **6:30 AM — 7:15 AM — Post-Workout Recovery & Shower:** Protein-rich breakfast & hydration.
    - **7:30 AM — 8:00 AM — Personal Devotional & Bible Reading:** Core Rule 1 & 4 (Year in Bible).
    - **8:00 AM — 5:00 PM — Professional Mission / Deep Work:** High-focus execution blocks.
    - **12:30 PM — Midday Fuel & Walk:** Meal 3 + 15-minute sunlight walk.
    - **6:30 PM — Anabolic Dinner & Family Time:** Meal 4 + evening connection.
    - **9:00 PM — Wind Down & Reflection:** Meal 5, review Daily Discipline Dashboard, prepare for tomorrow.
    """)
    
    st.info("💡 **Tip:** To sync this schedule with Google Calendar, you can copy these time blocks directly into your Google Calendar app or Google Workspace account.")
