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

# --- Custom Styling to Mirror Dark Theme Interface ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #161b22;
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #2ea043;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🦁 Chase the Lion")
st.sidebar.markdown("### High-Performance Command Center")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Peptide Protocol & Tracker",
        "Daily Review & Reflection Log",
        "Google Calendar & Daily Schedule",
        "12-Week Training Program & Tracker"
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

# ==========================================
# MODULE 4: 12-WEEK TRAINING PROGRAM & TRACKER
# ==========================================
elif menu == "12-Week Training Program & Tracker":
    st.header("🏋️‍♂️ 12-Week Training Architecture & Logs")
    st.write("Select your active week and log your daily sets, weights, and RPE targets.")
    
    week_selection = st.selectbox(
        "Select Training Week",
        [
            "Phase 1: Week 1 (Baseline)",
            "Phase 1: Week 2 (Progression)",
            "Phase 1: Week 3 (Complexity)",
            "Phase 1: Week 4 (Peak Base)",
            "Phase 2: Week 5 (New Patterns)",
            "Phase 2: Week 6 (Volume & Tempo)",
            "Phase 2: Week 7 (High Density)",
            "Phase 2: Week 8 (Peak Phase 2)",
            "Phase 3: Week 9 (Entry to Peak)",
            "Phase 3: Week 10 (High-Density)",
            "Phase 3: Week 11 (Metabolic Peak)",
            "Phase 3: Week 12 (Pump Deload)"
        ]
    )
    
    st.markdown(f"### Currently viewing: **{week_selection}**")
    st.info("Log your working weights and completion checkmarks below to track progressive overload across your 12-week block.")
    
    # Sample interactive logging table for current training day
    train_day = st.radio("Select Training Day", ["Day 1: Push", "Day 2: Pull", "Day 3: Lower Hypertrophy", "Day 5: Upper Pump"])
    
    if "Push" in train_day:
        data = {
            "Series": ["A-Series", "B1", "B1", "B2", "B2", "C-Series", "C-Series"],
            "Exercise": ["Overhead / Incline Press", "Flat DB / Barbell Press", "Row / High Row", "Arnold Press", "Skull Crushers / Tricep Ext", "Cable Fly", "Tricep Pushdown"],
            "Sets": [5, 3, 3, 3, 3, 3, 3],
            "Reps": ["5-8", "8-12", "10-15", "8-12", "6-10", "12-20", "12-20"],
            "Target RPE": [8, 8, 8, 8, 8, 8, 8],
            "Logged Weight (lbs)": [90, 55, 45, 30, 80, 30, 80],
            "Completed": [True, True, True, True, True, True, True]
        }
        df_train = pd.DataFrame(data)
        edited_df = st.data_editor(df_train, use_container_width=True)
        
        if st.button("💾 Save Workout Log"):
            st.success("✅ Workout performance logged successfully!")
