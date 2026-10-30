import streamlit as st
import pandas as pd
import datetime
import json
import urllib.request
import os

### PERSISTENT STORAGE FILES
HABITS_FILE = "chase_the_lion_daily_habits.json"
WORKOUT_HISTORY_FILE = "chase_the_lion_workout_history.csv"
PEPTIDE_HISTORY_FILE = "chase_the_lion_peptide_history.csv"
REVIEW_HISTORY_FILE = "chase_the_lion_daily_reviews.csv"

def load_json_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_json_file(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

### Page Config - Tactical Dark Theme
st.set_page_config(
    page_title="TXP Chase The Lion — Ecosystem",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

### Tactical Custom Styling (Clean Dark Cards, Hyrox Yellow Accents)
st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: #E5E7EB;
    }
    .sidebar .sidebar-content {
        background-color: #161b22;
    }
    h1, h2, h3 {
        color: #FFFFFF;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .tactical-card {
        background-color: #1E1E1E;
        border: 1px solid #2D2D2D;
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
    }
    .scripture-box {
        background: linear-gradient(135deg, #1a1f2c 0%, #11141d 100%);
        border-left: 4px solid #FFCC00;
        padding: 1rem;
        border-radius: 4px;
        margin-bottom: 1.5rem;
    }
    .scripture-text {
        font-style: italic;
        color: #e2e8f0;
        font-size: 1.1rem;
    }
    .scripture-ref {
        text-align: right;
        font-weight: bold;
        color: #FFCC00;
        margin-top: 0.5rem;
    }
    .stButton>button {
        background-color: #FFCC00;
        color: #000000;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 700;
    }
    .stButton>button:hover {
        background-color: #e6b800;
    }
    </style>
""", unsafe_allow_html=True)

### Sidebar Navigation & Customization
st.sidebar.markdown("""
    <div style="background-color: #FFCC00; color: #000000; font-weight: 900; padding: 6px 12px; font-size: 1.1rem; text-align: center; border-radius: 6px; margin-bottom: 10px;">
        TXP CHASE THE LION
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Warrior Navigation")
menu = st.sidebar.radio("Select Module:", [
    "Dashboard & Daily Discipline",
    "12-Week Lift Engine (Real-Time)",
    "Nutrition & Macro Engine",
    "Peptide Protocol & Tracker",
    "Daily Review & Faith Log",
    "Google Calendar & Schedule"
])

st.sidebar.markdown("---")
with st.sidebar.expander("📊 Google Sheets Live Sync", expanded=False):
    webhook_url = st.text_input("Google Web App URL:", value="https://script.google.com/macros/s/AKfycbyTr1VtWCvnb6_4IwMi64pDvTy-uDtL4DtHYls1wRq8s0rzOJLl7DD30_6IQZkajktfUQ/exec", key="gsheet_url")
    st.markdown("Workouts sync automatically to your Google Sheet upon saving session.")

# ==========================================
# MODULE 1: DASHBOARD & DAILY DISCIPLINE
# ==========================================
if menu == "Dashboard & Daily Discipline":
    st.markdown("""
        <div class="tactical-card" style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Command Center</span>
                <h2 style="margin-top: 10px; margin-bottom: 5px;">Daily Discipline & Warrior Vitals</h2>
                <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Execute core rules, track daily vitals, and anchor your mind in Scripture.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    scriptures = {
        "Proverbs 28:1": '"The wicked flee when no one pursues, but the righteous are bold as a lion."',
        "2 Samuel 23:20": '"Benaiah son of Jehoiada was a valiant fighter... He also went down into a pit on a snowy day and killed a lion."',
        "Joshua 1:9": '"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go."',
        "1 Corinthians 16:13": '"Be on your guard; stand firm in the faith; be courageous; be strong."',
        "2 Timothy 1:7": '"For God has not given us a spirit of fear, but of power and of love and of a sound mind."'
    }
    
    selected_ref = st.selectbox("Select Daily Scripture Focus:", list(scriptures.keys()))
    st.markdown(f"""
    <div class="scripture-box">
        <div class="scripture-text">{scriptures[selected_ref]}</div>
        <div class="scripture-ref">— {selected_ref}</div>
    </div>
    """, unsafe_allow_html=True)

    today_date = st.date_input("Today's Date", datetime.date.today())
    today_str = today_date.strftime("%Y-%m-%d")

    all_habits_data = load_json_file(HABITS_FILE)
    if today_str not in all_habits_data:
        all_habits_data[today_str] = {
            "devotional": False, "lift": False, "water": False, "bible": False,
            "sleep_hrs": 7.5, "hrv": 65, "rhr": 54, "mood": "Driven", "weight": 192.5,
            "devo_notes": "Proverbs 28 / Lionhearted Faith", "chapters_read": "Genesis 1-3 / Matthew 1"
        }
        save_json_file(HABITS_FILE, all_habits_data)

    today_data = all_habits_data[today_str]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Core Rules")
        devotional = st.checkbox("Rule 1: Personal Devotional", value=today_data.get("devotional", False))
        lift = st.checkbox("Rule 2: Lift Session", value=today_data.get("lift", False))
        water = st.checkbox("Rule 3: Gallon Water (128 oz)", value=today_data.get("water", False))
        bible = st.checkbox("Rule 4: Year In Bible Reading", value=today_data.get("bible", False))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Health Vitals")
        sleep_hrs = st.number_input("Sleep Duration (Hours)", min_value=0.0, max_value=12.0, value=float(today_data.get("sleep_hrs", 7.5)))
        hrv = st.number_input("HRV (ms)", value=int(today_data.get("hrv", 65)))
        rhr = st.number_input("Resting Heart Rate (BPM)", value=int(today_data.get("rhr", 54)))
        mood = st.selectbox("Daily Mood Focus", ["Driven", "Focused", "Sore", "Fatigued", "Reflective"], index=0)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Spiritual & Physical Log")
        weight = st.number_input("Current Weight (lbs)", value=float(today_data.get("weight", 192.5)))
        devo_notes = st.text_input("Devotional / Passage Focus", value=str(today_data.get("devo_notes", "Proverbs 28")))
        chapters_read = st.text_input("Bible Reading Passages", value=str(today_data.get("chapters_read", "Genesis 1-3")))
        st.markdown('</div>', unsafe_allow_html=True)

    today_data.update({"devotional": devotional, "lift": lift, "water": water, "bible": bible, "sleep_hrs": sleep_hrs, "hrv": hrv, "rhr": rhr, "mood": mood, "weight": weight, "devo_notes": devo_notes, "chapters_read": chapters_read})
    all_habits_data[today_str] = today_data
    save_json_file(HABITS_FILE, all_habits_data)

    completed = sum([devotional, lift, water, bible])
    st.markdown(f"""
        <div class="tactical-card">
            <h3>Discipline Scorecard: {completed} / 4 Rules Completed ({int((completed/4)*100)}%)</h3>
        </div>
    """, unsafe_allow_html=True)

    if st.button("💾 Log Daily Scorecard History"):
        df_log = pd.DataFrame([{
            "Date": today_str, "Devotional": devotional, "Lift": lift, "Water": water, "Bible": bible,
            "Score": f"{completed}/4", "Weight": weight, "Sleep": sleep_hrs, "HRV": hrv, "RHR": rhr, "Mood": mood
        }])
        df_log.to_csv("chase_the_lion_daily_history.csv", mode='a', header=not os.path.exists("chase_the_lion_daily_history.csv"), index=False)
        st.success("Daily Scorecard saved successfully!")

    if os.path.exists("chase_the_lion_daily_history.csv"):
        st.markdown("### Scorecard History")
        st.dataframe(pd.read_csv("chase_the_lion_daily_history.csv"), use_container_width=True)

# ==========================================
# MODULE 2: 12-WEEK LIFT ENGINE
# ==========================================
elif menu == "12-Week Lift Engine (Real-Time)":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Lift Engine</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">12-Week Ultimate Lift Engine & Real-Time Set Tracker</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Select your training block, log set-by-set working weights, and auto-sync progress.</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        phase = st.selectbox("Training Phase:", ["Phase 1: Base Phase (Weeks 1-4)", "Phase 2: Structural Shift (Weeks 5-8)", "Phase 3: Peak Hypertrophy (Weeks 9-12)"])
    with c2:
        week = st.selectbox("Training Week:", ["Week 1 (Baseline)", "Week 2 (Progression)", "Week 3 (Peak Base Volume)", "Week 4 (Deload & Test)", "Week 5 (Structural Intro)", "Week 6 (Eccentric Tempo)", "Week 7 (Density Peak)", "Week 8 (Deload)", "Week 9 (Hypertrophy Intro)", "Week 10 (Double Supersets)", "Week 11 (Peak Fiber Recruitment)", "Week 12 (Pump Deload)"])
    with c3:
        day = st.selectbox("Training Day:", [
            "Day 1: Push (Chest / Shoulders / Triceps)",
            "Day 2: Pull (Back / Rear Delts / Biceps)",
            "Day 3: Lower Hypertrophy (Quads / Hamstrings / Calves)",
            "Day 4: Active Recovery & Mobility",
            "Day 5: Upper Hypertrophy / Pump",
            "Day 6: Arms, Calves & Core (Optional)",
            "Day 7: Off & Regeneration"
        ])

    st.markdown("---")
    
    exercises = [
        {"series": "A-Series", "name": "Barbell Bench Press / Incline Press", "sets": 4, "reps": "6-8", "load": 185},
        {"series": "B1", "name": "Seated Overhead Dumbbell Press", "sets": 3, "reps": "8-10", "load": 60},
        {"series": "B2", "name": "Weighted Dips", "sets": 3, "reps": "8-12", "load": 45},
        {"series": "C-Series", "name": "Cable Lateral Raises", "sets": 3, "reps": "12-15", "load": 25}
    ]

    completed_sets = 0
    total_sets = sum([ex["sets"] for ex in exercises])
    
    workout_prefix = f"{phase}_{week}_{day}"
    for idx, ex in enumerate(exercises):
        st.markdown(f"""
            <div class="tactical-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="color: #FFCC00; font-weight: bold; font-size: 14px;">{ex['series']} — {ex['name']}</span>
                    <span style="font-size: 12px; color: #9CA3AF;">Target: {ex['sets']} Sets x {ex['reps']} Reps</span>
                </div>
        """, unsafe_allow_html=True)
        
        col_wt, col_chk = st.columns([1, 3])
        with col_wt:
            st.number_input("Weight Used (lbs)", value=ex['load'], key=f"{workout_prefix}_ex{idx}_wt")
        with col_chk:
            st.write("Mark Completed Sets:")
            set_cols = st.columns(ex['sets'])
            for s in range(1, ex['sets'] + 1):
                set_key = f"{workout_prefix}_ex{idx}_set{s}"
                with set_cols[s - 1]:
                    if st.checkbox(f"Set {s}", key=set_key):
                        completed_sets += 1
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="tactical-card">
            <h3>Session Progress: {completed_sets} / {total_sets} Sets Completed ({int((completed_sets/total_sets)*100)}%)</h3>
        </div>
    """, unsafe_allow_html=True)

    session_notes = st.text_area("Session Notes (Pump Quality, Joint Health, Energy):")
    if st.button("💾 Save Completed Workout Session"):
        log_entry = {
            "Date": datetime.date.today().strftime("%Y-%m-%d"),
            "Phase": phase, "Week": week, "Day": day,
            "Sets Completed": f"{completed_sets}/{total_sets}", "Notes": session_notes
        }
        df_w = pd.DataFrame([log_entry])
        df_w.to_csv(WORKOUT_HISTORY_FILE, mode='a', header=not os.path.exists(WORKOUT_HISTORY_FILE), index=False)
        
        gs_url = st.session_state.get("gsheet_url", "").strip()
        if gs_url:
            try:
                payload = json.dumps(log_entry).encode('utf-8')
                req = urllib.request.Request(gs_url, data=payload, headers={'Content-Type': 'application/json'})
                urllib.request.urlopen(req, timeout=3)
            except Exception:
                pass
        st.success("Workout saved successfully and synced!")

    if os.path.exists(WORKOUT_HISTORY_FILE):
        st.markdown("### Permanent Workout History")
        st.dataframe(pd.read_csv(WORKOUT_HISTORY_FILE), use_container_width=True)

# ==========================================
# MODULE 3: NUTRITION & MACRO ENGINE
# ==========================================
elif menu == "Nutrition & Macro Engine":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Nutrition Engine</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Nutrition & Daily Macro Targets</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Precision fuel targets optimized for lean muscle hypertrophy and recovery.</p>
        </div>
    """, unsafe_allow_html=True)

    day_type = st.radio("Select Training Day Target:", ["Standard Lift Day", "Leg Day Peak", "Rest Day Recovery"], horizontal=True)
    if day_type == "Standard Lift Day":
        kcal, p, c, f = 2800, 200, 315, 80
    elif day_type == "Leg Day Peak":
        kcal, p, c, f = 2900, 200, 340, 75
    else:
        kcal, p, c, f = 2400, 200, 180, 90

    m1, m2, m3, m4 = st.columns(4)
    m1.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Calories</h4><h2>{kcal} kcal</h2></div>', unsafe_allow_html=True)
    m2.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Protein</h4><h2>{p} g</h2></div>', unsafe_allow_html=True)
    m3.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Carbs</h4><h2>{c} g</h2></div>', unsafe_allow_html=True)
    m4.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Fats</h4><h2>{f} g</h2></div>', unsafe_allow_html=True)

# ==========================================
# MODULE 4: PEPTIDE PROTOCOL & TRACKER
# ==========================================
elif menu == "Peptide Protocol & Tracker":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Protocol Tracker</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Peptide Protocol & Daily Injection Tracker</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">BPC-157 / TB-500 Tissue Repair & Joint Regeneration Protocol.</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        admin_date = st.date_input("Administration Date", datetime.date.today())
        dose_mcg = st.number_input("Dosage (mcg)", value=250, step=50)
        site = st.selectbox("Injection Site / Focus Area", [
            "Left Shoulder / Rotator Cuff", "Right Shoulder / Rotator Cuff",
            "Left Knee / Patellar Tendon", "Right Knee / Patellar Tendon",
            "Lower Back / Lumbar", "Subcutaneous Abdomen (Systemic)"
        ])
    with c2:
        fasted = st.checkbox("Administered Fasted (Morning)", value=True)
        joint_pain = st.slider("Joint Pain / Stiffness Level (1 = None, 10 = Severe)", 1, 10, 3)
        pep_notes = st.text_input("Protocol Notes", value="Felt great, minor tendon relief.")

    if st.button("💉 Log Peptide Administration"):
        pep_entry = {"Date": admin_date.strftime("%Y-%m-%d"), "Dose (mcg)": dose_mcg, "Site": site, "Fasted": fasted, "Pain Level": joint_pain, "Notes": pep_notes}
        df_pep = pd.DataFrame([pep_entry])
        df_pep.to_csv(PEPTIDE_HISTORY_FILE, mode='a', header=not os.path.exists(PEPTIDE_HISTORY_FILE), index=False)
        st.success("Peptide dose logged successfully!")

    if os.path.exists(PEPTIDE_HISTORY_FILE):
        st.markdown("### Peptide Protocol History")
        st.dataframe(pd.read_csv(PEPTIDE_HISTORY_FILE), use_container_width=True)

# ==========================================
# MODULE 5: DAILY REVIEW & FAITH LOG
# ==========================================
elif menu == "Daily Review & Faith Log":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Faith Log</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Daily Review & Faith Reflection Log</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">End-of-day spiritual and mental debrief. Align heart and mind with the mission.</p>
        </div>
    """, unsafe_allow_html=True)

    wins = st.text_area("1. What were today's biggest victories?")
    battles = st.text_area("2. Where did I face friction or temptation?")
    gratitude = st.text_area("3. What am I deeply grateful for today?")
    tomorrow_goal = st.text_input("4. One primary mission for tomorrow:", value="Attack 5 AM workout with lionhearted intensity.")

    if st.button("💾 Save Daily Reflection"):
        rev_entry = {"Date": datetime.date.today().strftime("%Y-%m-%d"), "Victories": wins, "Battles": battles, "Gratitude": gratitude, "Tomorrow's Mission": tomorrow_goal}
        df_rev = pd.DataFrame([rev_entry])
        df_rev.to_csv(REVIEW_HISTORY_FILE, mode='a', header=not os.path.exists(REVIEW_HISTORY_FILE), index=False)
        st.success("Daily Reflection saved successfully!")

    if os.path.exists(REVIEW_HISTORY_FILE):
        st.markdown("### Reflection History")
        st.dataframe(pd.read_csv(REVIEW_HISTORY_FILE), use_container_width=True)

# ==========================================
# MODULE 6: GOOGLE CALENDAR & SCHEDULE
# ==========================================
elif menu == "Google Calendar & Schedule":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Schedule</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Google Calendar & Daily Tactical Timeline</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">The Lionhearted Daily Routine Schedule.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="tactical-card">
            <h3>🦁 The Lionhearted Daily Routine</h3>
            <ul>
                <li><strong>4:15 AM — Wake Up & Fuel:</strong> Pre-workout meal + electrolytes.</li>
                <li><strong>5:00 AM — Iron Temple:</strong> Execute daily training block.</li>
                <li><strong>6:30 AM — Recovery & Shower:</strong> Protein breakfast & hydration.</li>
                <li><strong>7:30 AM — Personal Devotional:</strong> Core Rule 1 & Bible reading.</li>
                <li><strong>8:00 AM — Professional Mission:</strong> Deep work blocks.</li>
                <li><strong>12:30 PM — Midday Fuel:</strong> Meal 3 + sunlight walk.</li>
                <li><strong>6:30 PM — Anabolic Dinner:</strong> Evening family connection.</li>
                <li><strong>9:00 PM — Wind Down:</strong> Review scorecard and prepare for tomorrow.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("TX_Pierce Chase The Lion Ecosystem | High-Performance Tactical Architecture")
