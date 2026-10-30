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
    page_title="TXP ✝ Chase The Lion — Ecosystem",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

### Custom CSS Styling matching exact Hyrox Top Navigation & Clean Dark Cards
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .tactical-card {
        background-color: #1E1E1E;
        border: 1px solid #2D2D2D;
        padding: 1.25rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
    }
    .scripture-box {
        background-color: #1a1f2c;
        border-left: 4px solid #FFCC00;
        padding: 1rem;
        border-radius: 4px;
        margin-bottom: 1.25rem;
    }
    .scripture-text {
        font-style: italic;
        color: #e2e8f0;
        font-size: 1.05rem;
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
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #e6b800;
    }
    /* Hide Streamlit default hamburger menu & footer for app-like mobile view */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive stacking fixes for mobile devices */
    @media(max-width: 768px) {
        .stColumns {
            flex-direction: column !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

### Initialize Session State
if 'completed_sets_store' not in st.session_state:
    st.session_state.completed_sets_store = {}
if 'workout_logs' not in st.session_state:
    st.session_state.workout_logs = []
if 'peptide_logs' not in st.session_state:
    st.session_state.peptide_logs = {}
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Dashboard"

### Top Header Bar with Horizontal Navigation Tabs (matching the Hyrox UI style)
st.markdown("""
    <div style="background-color: #000000; border-bottom: 1px solid #2D2D2D; padding: 12px 15px; display: flex; flex-direction: column; justify-content: space-between; align-items: center; margin-bottom: 20px; border-radius: 8px; gap: 10px;">
        <div style="display: flex; align-items: center; gap: 12px; width: 100%;">
            <div style="background-color: #FFCC00; color: #000000; font-weight: 900; padding: 6px 12px; font-size: 1.1rem; letter-spacing: 1px; border-radius: 6px;">TXP</div>
            <div>
                <h1 style="font-size: 1rem; font-weight: bold; color: #FFFFFF; margin: 0; letter-spacing: 0.5px;">CHASE THE LION ECOSYSTEM</h1>
                <p style="font-size: 0.7rem; color: #9CA3AF; margin: 0;">Daily Discipline | 12-Week Lift Engine | Peptides & Faith</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Horizontal Navigation Tabs (matching your Hyrox Tracker UI)
tabs = [
    "Dashboard", 
    "11-Week Master", 
    "Nutrition & Macros", 
    "Peptide Tracker", 
    "Faith Reflection", 
    "Daily Schedule"
]

tab_cols = st.columns(len(tabs))
for idx, tab_name in enumerate(tabs):
    with tab_cols[idx]:
        is_selected = (st.session_state.active_tab == tab_name)
        if st.button(tab_name, key=f"tab_btn_{idx}", use_container_width=True):
            st.session_state.active_tab = tab_name
            st.rerun()

current_tab = st.session_state.active_tab
st.markdown("---")

# Sidebar Google Sheets Integration Settings (collapsed)
with st.sidebar.expander("📊 Google Sheets Live Sync Setup", expanded=False):
    st.write("**Save workouts directly to Google Sheets!**")
    webhook_url = st.text_input("Google Web App URL:", value="https://script.google.com/macros/s/AKfycbyTr1VtWCvnb6_4IwMi64pDvTy-uDtL4DtHYls1wRq8s0rzOJLl7DD30_6IQZkajktfUQ/exec", key="gsheet_url")
    st.markdown("""
    **3-Step Setup:**
    1. Open a blank Google Sheet.
    2. Click **Extensions > Apps Script**, paste this code:
    ```javascript
    function doPost(e) {
      var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
      var data = JSON.parse(e.postData.contents);
      sheet.appendRow([data.Date, data.Phase, data.Week, data.Day, data.SetsCompleted, data.Progress, data.Notes]);
      return ContentService.createTextOutput("Success");
    }
    ```
    3. Click **Deploy > New deployment**, select **Web app**, set access to **Anyone**, and paste the URL above!
    """)


# ==========================================
# TAB 1: DASHBOARD
# ==========================================
if current_tab == "Dashboard":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Command Center</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Daily Discipline Tracker & Vitals</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Execute your daily core rules, track vitals, and anchor your mind in Scripture.</p>
        </div>
    """, unsafe_allow_html=True)
    
    scriptures = {
        "Proverbs 28:1": '"The wicked flee when no one pursues, but the righteous are bold as a lion."',
        "2 Samuel 23:20": '"Benaiah son of Jehoiada was a valiant fighter... He also went down into a pit on a snowy day and killed a lion."',
        "Joshua 1:9": '"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go."',
        "1 Corinthians 16:13": '"Be on your guard; stand firm in the faith; be courageous; be strong."',
        "2 Timothy 1:7": '"For God has not given us a spirit of fear, but of power and of love and of a sound mind."'
    }
    
    selected_ref = st.selectbox("📖 Select Daily Scripture Focus:", list(scriptures.keys()))
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
            "sleep_hrs": 7.5, "hrv": 65, "rhr": 54, "mood": "Driven 🦁", "weight": 192.5,
            "devo_notes": "Proverbs 28 / Lionhearted Faith", "chapters_read": "Genesis 1-3 / Matthew 1"
        }
        save_json_file(HABITS_FILE, all_habits_data)

    today_data = all_habits_data[today_str]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Core Rules")
        st.caption("⏳ *Selections auto-save daily.*")
        devotional = st.checkbox("Rule 1: Personal Devotional", value=today_data.get("devotional", False))
        lift = st.checkbox("Rule 2: Lift Session", value=today_data.get("lift", False))
        water = st.checkbox("Rule 3: Gallon Water (128 oz)", value=today_data.get("water", False))
        bible = st.checkbox("Rule 4: Year In Bible Reading", value=today_data.get("bible", False))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Health Metrics")
        sleep_hrs = st.number_input("Sleep Duration (Hours)", min_value=0.0, max_value=12.0, value=float(today_data.get("sleep_hrs", 7.5)))
        hrv = st.number_input("HRV (ms)", value=int(today_data.get("hrv", 65)))
        rhr = st.number_input("Resting Heart Rate (BPM)", value=int(today_data.get("rhr", 54)))
        mood = st.selectbox("Daily Mood Focus", ["Driven 🦁", "Focused ⚡", "Sore 💪", "Fatigued 😴", "Reflective 🙏"], index=0)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="tactical-card">', unsafe_allow_html=True)
        st.subheader("Physical & Spiritual Log")
        weight = st.number_input("Current Weight (lbs)", value=float(today_data.get("weight", 192.5)))
        devo_notes = st.text_input("Devotional / Passage Focus", value=str(today_data.get("devo_notes", "Proverbs 28")))
        chapters_read = st.text_input("Bible Reading Passages", value=str(today_data.get("chapters_read", "Genesis 1-3")))
        st.markdown('</div>', unsafe_allow_html=True)

    today_data.update({"devotional": devotional, "lift": lift, "water": water, "bible": bible, "sleep_hrs": sleep_hrs, "hrv": hrv, "rhr": rhr, "mood": mood, "weight": weight, "devo_notes": devo_notes, "chapters_read": chapters_read})
    all_habits_data[today_str] = today_data
    save_json_file(HABITS_FILE, all_habits_data)

    completed = sum([devotional, lift, water, bible])
    progress_pct = completed / 4.0
    st.markdown(f"""
        <div class="tactical-card">
            <h3>Discipline Scorecard Summary</h3>
            <p><strong>Completed:</strong> {completed} / 4 Core Rules Completed Today ({int(progress_pct * 100)}%)</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("💾 Log Daily Scorecard to History"):
        df_log = pd.DataFrame([{
            "Date": today_str, "Devotional": devotional, "Lift": lift, "Water": water, "Bible": bible,
            "Discipline Score": f"{completed}/4", "Weight": weight, "Sleep (hrs)": sleep_hrs, "HRV": hrv, "RHR": rhr, "Mood": mood
        }])
        df_log.to_csv("chase_the_lion_daily_history.csv", mode='a', header=not os.path.exists("chase_the_lion_daily_history.csv"), index=False)
        st.success("✅ Daily Scorecard saved successfully!")

    if os.path.exists("chase_the_lion_daily_history.csv"):
        st.subheader("📜 Daily Scorecard History")
        st.dataframe(pd.read_csv("chase_the_lion_daily_history.csv"), use_container_width=True)


# ==========================================
# TAB 2: 11-WEEK MASTER (LIFT ENGINE)
# ==========================================
elif current_tab == "11-Week Master":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Lift Engine</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">11-Week Master Training Program & Set Tracker</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Log working weights and check off sets. Data saves automatically in the tactical card layout.</p>
        </div>
    """, unsafe_allow_html=True)

    col_phase, col_week, col_day = st.columns(3)
    with col_phase:
        phase = st.selectbox("Select Training Phase:", [
            "Phase 1: Base Phase (Weeks 1-4)",
            "Phase 2: Structural Shift (Weeks 5-8)",
            "Phase 3: Peak Hypertrophy (Weeks 9-12)"
        ])
    with col_week:
        if "Phase 1" in phase:
            week = st.selectbox("Select Week:", ["Week 1 (Baseline)", "Week 2 (Progression)", "Week 3 (Peak Base Volume)", "Week 4 (Deload & Test)"])
        elif "Phase 2" in phase:
            week = st.selectbox("Select Week:", ["Week 5 (Structural Intro)", "Week 6 (Eccentric Tempo)", "Week 7 (Density Peak)", "Week 8 (Deload)"])
        else:
            week = st.selectbox("Select Week:", ["Week 9 (Hypertrophy Intro)", "Week 10 (Double Supersets)", "Week 11 (Peak Fiber Recruitment)", "Week 12 (Pump Deload)"])
    with col_day:
        day = st.selectbox("Select Training Day:", [
            "Day 1: Push (Chest / Shoulders / Triceps)",
            "Day 2: Pull (Back / Rear Delts / Biceps)",
            "Day 3: Lower Hypertrophy (Quads / Hamstrings / Calves)",
            "Day 4: Active Recovery & Mobility",
            "Day 5: Upper Hypertrophy / Pump",
            "Day 6: Arms, Calves & Core (Optional)",
            "Day 7: Off & Regeneration"
        ])

    st.markdown("---")

    def get_workout_for_week(week_str, day_str):
        if "Day 4" in day_str:
            return [
                {"series": "Recovery", "exercise": "Thoracic & Hip Mobility Circuit", "sets": 3, "reps": "10 mins", "rpe": "4", "rest": "None", "default_wt": 0},
                {"series": "Recovery", "exercise": "Diaphragmatic Breathing & Foam Rolling", "sets": 1, "reps": "15 mins", "rpe": "3", "rest": "None", "default_wt": 0}
            ]
        elif "Day 7" in day_str:
            return [
                {"series": "Rest", "exercise": "Full Body Rest & Joint Recovery", "sets": 1, "reps": "Full Day", "rpe": "0", "rest": "N/A", "default_wt": 0}
            ]
        elif "Push" in day_str:
            return [
                {"series": "A-Series", "exercise": "Back / Incline Press", "sets": 4, "reps": "6", "rpe": "8", "rest": "2 min", "default_wt": 185},
                {"series": "B1", "exercise": "Reverse Lunge", "sets": 3, "reps": "10/leg", "rpe": "8", "rest": "90 sec", "default_wt": 60},
                {"series": "B2", "exercise": "Sled Push", "sets": 6, "reps": "10 m", "rpe": "8", "rest": "90 sec", "default_wt": 150},
                {"series": "C-Series", "exercise": "Bike Erg Engine", "sets": 6, "reps": "1:00 hard / 1:00 easy", "rpe": "9", "rest": "60 sec", "default_wt": 0}
            ]
        elif "Pull" in day_str:
            return [
                {"series": "A-Series", "exercise": "Weighted Pull-Ups / Barbell Row", "sets": 4, "reps": "6-8", "rpe": "8", "rest": "2 min", "default_wt": 135},
                {"series": "B1", "exercise": "Chest-Supported T-Bar Row", "sets": 3, "reps": "8-10", "rpe": "8", "rest": "90 sec", "default_wt": 115},
                {"series": "B2", "exercise": "Lat Pulldown (Neutral Grip)", "sets": 3, "reps": "10-12", "rpe": "8", "rest": "90 sec", "default_wt": 140}
            ]
        return [
            {"series": "A-Series", "exercise": "Primary Compound Movement", "sets": 4, "reps": "8-10", "rpe": "8", "rest": "2 min", "default_wt": 100},
            {"series": "B1", "exercise": "Secondary Compound Movement", "sets": 3, "reps": "10-12", "rpe": "8", "rest": "90 sec", "default_wt": 80}
        ]

    current_workout = get_workout_for_week(week, day)
    total_target_sets = sum([ex["sets"] for ex in current_workout])
    completed_sets_count = 0
    workout_key_prefix = f"{phase}_{week}_{day}"

    for idx, ex in enumerate(current_workout):
        for s in range(1, ex["sets"] + 1):
            set_key = f"{workout_key_prefix}_ex{idx}_set{s}"
            if st.session_state.get(set_key, False):
                completed_sets_count += 1

    progress_pct = completed_sets_count / total_target_sets if total_target_sets > 0 else 0.0

    st.markdown(f"""
        <div class="tactical-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h3 style="margin: 0;">11-Week Master Training Program</h3>
                <span style="color: #FFCC00; font-weight: bold;">{int(progress_pct * 100)}% Completed ({completed_sets_count}/{total_target_sets} sets)</span>
            </div>
            <div style="background-color: #000; border-radius: 4px; height: 8px; width: 100%; overflow: hidden;">
                <div style="background-color: #FFCC00; width: {int(progress_pct * 100)}%; height: 100%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    for idx, ex in enumerate(current_workout):
        st.markdown(f"""
            <div class="tactical-card">
                <div style="margin-bottom: 4px; font-weight: bold; color: #FFFFFF; font-size: 1.05rem;">{ex['exercise']}</div>
                <div style="color: #9CA3AF; font-size: 0.85rem; margin-bottom: 10px;">Target: {ex['sets']} | Prescribed: {ex['reps']} (RPE {ex['rpe']})</div>
        """, unsafe_allow_html=True)
        
        col_input, col_sets = st.columns([1, 2])
        with col_input:
            wt_key = f"{workout_key_prefix}_ex{idx}_wt"
            st.text_input(f"Actual Load...", value=str(ex['default_wt']), key=wt_key, label_visibility="collapsed")
        with col_sets:
            st.markdown("<span style='font-size:0.8rem; color:#9CA3AF;'>CHECK SETS:</span>", unsafe_allow_html=True)
            set_cols = st.columns(ex['sets'])
            for s in range(1, ex['sets'] + 1):
                set_key = f"{workout_key_prefix}_ex{idx}_set{s}"
                with set_cols[s - 1]:
                    st.checkbox(f"{s}", key=set_key)
        st.markdown('</div>', unsafe_allow_html=True)

    session_notes = st.text_area("Session Notes (Pump Quality, Joint Health, Energy Level):")

    if st.button("💾 Save Completed Workout Session"):
        new_log = {
            "Date": datetime.date.today().strftime("%Y-%m-%d"),
            "Phase": phase, "Week": week, "Day": day,
            "Sets Completed": f"{completed_sets_count}/{total_target_sets}",
            "Progress": f"{int(progress_pct * 100)}%",
            "Notes": session_notes
        }
        df_new = pd.DataFrame([new_log])
        df_new.to_csv(WORKOUT_HISTORY_FILE, mode='a', header=not os.path.exists(WORKOUT_HISTORY_FILE), index=False)

        gs_url = st.session_state.get("gsheet_url", "").strip()
        if gs_url:
            try:
                payload = json.dumps(new_log).encode('utf-8')
                req = urllib.request.Request(gs_url, data=payload, headers={'Content-Type': 'application/json'})
                urllib.request.urlopen(req, timeout=3)
            except Exception:
                pass
        st.success(f"✅ Workout logged successfully! ({completed_sets_count}/{total_target_sets} sets)")

    if os.path.exists(WORKOUT_HISTORY_FILE):
        st.subheader("📜 Permanent Workout History")
        st.dataframe(pd.read_csv(WORKOUT_HISTORY_FILE), use_container_width=True)


# ==========================================
# TAB 3: NUTRITION & MACROS
# ==========================================
elif current_tab == "Nutrition & Macros":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Nutrition Engine</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Nutrition & Macro Engine</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Precision daily fuel targets optimized for muscle growth and recovery.</p>
        </div>
    """, unsafe_allow_html=True)

    day_type = st.radio("Select Day Type Target:", ["Standard Lift Day", "Leg Day Peak", "Rest Day Recovery"], horizontal=True)

    if day_type == "Standard Lift Day":
        target_kcal, target_p, target_c, target_f = 2800, 200, 315, 80
    elif day_type == "Leg Day Peak":
        target_kcal, target_p, target_c, target_f = 2900, 200, 340, 75
    else:
        target_kcal, target_p, target_c, target_f = 2400, 200, 180, 90

    m1, m2, m3, m4 = st.columns(4)
    m1.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Calories</h4><h2>{target_kcal} kcal</h2></div>', unsafe_allow_html=True)
    m2.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Protein</h4><h2>{target_p} g</h2></div>', unsafe_allow_html=True)
    m3.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Carbs</h4><h2>{target_c} g</h2></div>', unsafe_allow_html=True)
    m4.markdown(f'<div class="tactical-card" style="text-align:center;"><h4>Fats</h4><h2>{target_f} g</h2></div>', unsafe_allow_html=True)


# ==========================================
# TAB 4: PEPTIDE TRACKER
# ==========================================
elif current_tab == "Peptide Tracker":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Protocol Tracker</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Peptide Protocol & Daily Injection Tracker</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">BPC-157 / TB-500 Tissue Repair & Joint Regeneration Protocol.</p>
        </div>
    """, unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        admin_date = st.date_input("Administration Date", datetime.date.today())
        dose_mcg = st.number_input("Dosage (mcg)", value=250, step=50)
        site = st.selectbox(
            "Injection Site / Focus Area", 
            [
                "Left Shoulder / Rotator Cuff", 
                "Right Shoulder / Rotator Cuff", 
                "Left Knee / Patellar Tendon", 
                "Right Knee / Patellar Tendon", 
                "Lower Back / Lumbar", 
                "Subcutaneous Abdomen (Systemic)"
            ]
        )
    with p_col2:
        fasted = st.checkbox("Administered Fasted (Morning)", value=True)
        joint_pain_scale = st.slider("Joint Pain / Stiffness Level (1 = None, 10 = Severe)", min_value=1, max_value=10, value=3)
        pep_notes = st.text_input("Protocol Notes:", value="Felt great, minor tendon relief.")
        
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
        df_pep.to_csv(PEPTIDE_HISTORY_FILE, mode='a', header=not os.path.exists(PEPTIDE_HISTORY_FILE), index=False)
        st.success("✅ Peptide dose logged successfully!")
        
    if os.path.exists(PEPTIDE_HISTORY_FILE):
        st.subheader("📜 Peptide Protocol History")
        st.dataframe(pd.read_csv(PEPTIDE_HISTORY_FILE), use_container_width=True)


# ==========================================
# TAB 5: FAITH REFLECTION
# ==========================================
elif current_tab == "Faith Reflection":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Faith Log</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Daily Review & Faith Reflection Log</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">End-of-day spiritual and mental debrief. Align your heart and mind with the mission.</p>
        </div>
    """, unsafe_allow_html=True)
    
    wins = st.text_area("1. What were today's biggest victories (physical, spiritual, or mental)?")
    battles = st.text_area("2. Where did I face friction, temptation, or weakness today?")
    gratitude = st.text_area("3. What am I deeply grateful for today?")
    tomorrow_goal = st.text_input("4. One primary mission for tomorrow:", value="Attack 5 AM workout with lionhearted intensity.")
    
    if st.button("💾 Save Daily Reflection & Review"):
        review_entry = {
            "Date": datetime.date.today().strftime("%Y-%m-%d"),
            "Victories": wins,
            "Battles Fought": battles,
            "Gratitude": gratitude,
            "Tomorrow's Mission": tomorrow_goal
        }
        df_rev = pd.DataFrame([review_entry])
        df_rev.to_csv(REVIEW_HISTORY_FILE, mode='a', header=not os.path.exists(REVIEW_HISTORY_FILE), index=False)
        st.success("✅ Daily Reflection saved successfully!")
        
    if os.path.exists(REVIEW_HISTORY_FILE):
        st.subheader("📜 Past Daily Reflections")
        st.dataframe(pd.read_csv(REVIEW_HISTORY_FILE), use_container_width=True)


# ==========================================
# TAB 6: DAILY SCHEDULE
# ==========================================
elif current_tab == "Daily Schedule":
    st.markdown("""
        <div class="tactical-card">
            <span style="background-color: rgba(255,204,0,0.1); color: #FFCC00; border: 1px solid rgba(255,204,0,0.3); font-size: 11px; padding: 4px 10px; border-radius: 9999px; font-weight: bold; text-transform: uppercase;">Schedule</span>
            <h2 style="margin-top: 10px; margin-bottom: 5px;">Google Calendar & Daily Tactical Schedule</h2>
            <p style="color: #9CA3AF; font-size: 13px; margin: 0;">Align your daily calendar events with your high-performance routine.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="tactical-card">
            <h3>🦁 Daily Routine Timeline (The Lionhearted Schedule)</h3>
            <ul>
                <li><strong>4:15 AM — Wake Up & Fuel:</strong> Pre-workout meal + electrolytes.</li>
                <li><strong>5:00 AM — Iron Temple (Lift Engine):</strong> Execute daily training block.</li>
                <li><strong>6:30 AM — Recovery & Shower:</strong> Protein-rich breakfast & hydration.</li>
                <li><strong>7:30 AM — Personal Devotional:</strong> Core Rule 1 & Bible reading.</li>
                <li><strong>8:00 AM — Professional Mission:</strong> High-focus deep work blocks.</li>
                <li><strong>12:30 PM — Midday Fuel:</strong> Meal 3 + 15-minute sunlight walk.</li>
                <li><strong>6:30 PM — Anabolic Dinner:</strong> Evening connection.</li>
                <li><strong>9:00 PM — Wind Down & Reflection:</strong> Review scorecard and prepare for tomorrow.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("TX_Pierce Chase The Lion Ecosystem — High-Performance Tactical Suite")
