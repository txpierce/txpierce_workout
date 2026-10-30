import streamlit as st
import pandas as pd
import datetime
import json
import os

# ==============================================================================
# CONFIGURATION & STYLING (Hyrox Tactical Dark Theme)
# ==============================================================================
st.set_page_config(
    page_title="TXP ✝ Chase The Lion — Habit & Lift Ecosystem",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Main Background & Typography */
    .main {
        background-color: #121212;
        color: #E5E7EB;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .stApp {
        background-color: #121212;
    }
    h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-weight: 800;
        letter-spacing: -0.025em;
    }
    
    /* Tactical Card Containers */
    .tactical-card {
        background-color: #1E1E1E;
        border: 1px solid #2D2D2D;
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    /* Scripture Callout Box */
    .scripture-box {
        background: linear-gradient(135deg, #1a1f2c 0%, #11141d 100%);
        border-left: 4px solid #FFCC00;
        border-top: 1px solid #2D2D2D;
        border-right: 1px solid #2D2D2D;
        border-bottom: 1px solid #2D2D2D;
        padding: 1.25rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .scripture-text {
        font-style: italic;
        color: #F3F4F6;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    .scripture-ref {
        text-align: right;
        font-weight: bold;
        color: #FFCC00;
        margin-top: 0.5rem;
    }

    /* Custom Buttons & Inputs */
    .stButton>button {
        background-color: #FFCC00;
        color: #000000;
        border-radius: 0.5rem;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: 800;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #e6b800;
        color: #000000;
    }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] {
        color: #FFCC00 !important;
        font-weight: 900 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #9CA3AF !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #2D2D2D;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# PERSISTENT STORAGE FUNCTIONS
# ==============================================================================
HABITS_FILE = "chase_the_lion_daily_habits.json"
PEPTIDE_FILE = "chase_the_lion_peptide_history.csv"
WORKOUT_FILE = "chase_the_lion_workout_history.csv"
REVIEW_FILE = "chase_the_lion_daily_reviews.csv"

def load_json_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_json_file(filepath, data):
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

# Initialize Session States
if 'workout_logs' not in st.session_state:
    st.session_state.workout_logs = []

# ==============================================================================
# HEADER BRANDING (Hyrox-Style Top Bar)
# ==============================================================================
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.markdown("""
        <div style="background-color: #FFCC00; color: #000000; font-weight: 900; font-size: 1.5rem; text-align: center; padding: 0.6rem; border-radius: 0.5rem; letter-spacing: 0.05em;">
            TXP
        </div>
    """, unsafe_allow_html=True)
with col_title:
    st.markdown("""
        <div style="padding-top: 0.1rem;">
            <h2 style="margin: 0; font-size: 1.35rem; color: #FFFFFF;">CHASE THE LION ECOSYSTEM</h2>
            <p style="margin: 0; color: #9CA3AF; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em;">Tactical Daily Discipline | 12-Week Lift Engine | Peptides & Faith</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: #2D2D2D; margin-top: 1rem; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

# ==============================================================================
# HORIZONTAL TAB NAVIGATION (Hyrox Tracker Layout)
# ==============================================================================
tab_dash, tab_lift, tab_nutr, tab_pep, tab_rev, tab_sched = st.tabs([
    "📊 Daily Dashboard", 
    "🏋️‍♂️ 12-Week Lift Engine", 
    "🍽️ Nutrition & Macros", 
    "💉 Peptide Protocol", 
    "🙏 Faith & Review", 
    "📅 Daily Schedule"
])

# ==============================================================================
# TAB 1: DAILY DISCIPLINE DASHBOARD
# ==============================================================================
with tab_dash:
    st.markdown("### Daily Discipline & Biometrics Dashboard")
    st.caption("Execute your daily non-negotiable mission rules and track vital recovery metrics.")
    
    scriptures = {
        "Proverbs 28:1": '"The wicked flee when no one pursues, but the righteous are bold as a lion."',
        "2 Samuel 23:20": '"Benaiah son of Jehoiada was a valiant fighter... He also went down into a pit on a snowy day and killed a lion."',
        "Joshua 1:9": '"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go."',
        "1 Corinthians 16:13": '"Be on your guard; stand firm in the faith; be courageous; be strong."',
        "2 Timothy 1:7": '"For God has not given us a spirit of fear, but of power and of love and of a sound mind."',
        "Isaiah 40:31": '"But those who trust in the LORD will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint."'
    }
    
    selected_ref = st.selectbox("📖 Select Daily Scripture Creed:", list(scriptures.keys()))
    verse_text = scriptures[selected_ref]
    
    st.markdown(f"""
    <div class="scripture-box">
        <div class="scripture-text">{verse_text}</div>
        <div class="scripture-ref">— {selected_ref}</div>
    </div>
    """, unsafe_allow_html=True)

    today_date = st.date_input("Today's Date", datetime.date.today())
    today_str = today_date.strftime("%Y-%m-%d")

    all_habits = load_json_file(HABITS_FILE)
    if today_str not in all_habits:
        all_habits[today_str] = {
            "devotional": False, "lift": False, "water": False, "bible": False,
            "sleep_hrs": 7.5, "hrv": 65, "rhr": 54, "mood": "Driven 🦁",
            "weight": 192.5, "devo_notes": "Proverbs 28 / Lionhearted Faith",
            "chapters_read": "Genesis 1-3 / Matthew 1"
        }
        save_json_file(HABITS_FILE, all_habits)

    td = all_habits[today_str]

    col_d1, col_d2, col_d3 = st.columns(3)
    
    with col_d1:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("🛡️ Core Rules")
        st.caption("Non-daily discipline checkboxes")
        
        devotional = st.checkbox("Rule 1: Personal Devotional", value=td.get("devotional", False), key=f"dev_{today_str}")
        lift = st.checkbox("Rule 2: Lift Session Executed", value=td.get("lift", False), key=f"lft_{today_str}")
        water = st.checkbox("Rule 3: Gallon Water (128 oz)", value=td.get("water", False), key=f"wtr_{today_str}")
        bible = st.checkbox("Rule 4: Year In Bible Reading", value=td.get("bib_{today_str}", False), key=f"bib_{today_str}")
        
        td["devotional"] = devotional
        td["lift"] = lift
        td["water"] = water
        td["bible"] = bible
        save_json_file(HABITS_FILE, all_habits)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_d2:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("❤️ Health Metrics")
        st.caption("Recovery and biometrics tracking")
        
        sleep_hrs = st.number_input("Sleep Duration (Hours)", min_value=0.0, max_value=12.0, value=float(td.get("sleep_hrs", 7.5)), step=0.5, key=f"slp_{today_str}")
        hrv = st.number_input("HRV (ms)", value=int(td.get("hrv", 65)), key=f"hrv_{today_str}")
        rhr = st.number_input("Resting Heart Rate (BPM)", value=int(td.get("rhr", 54)), key=f"rhr_{today_str}")
        
        mood_opts = ["Driven 🦁", "Focused ⚡", "Sore 💪", "Fatigued 😴", "Reflective 🙏"]
        cur_mood = td.get("mood", "Driven 🦁")
        mood_idx = mood_opts.index(cur_mood) if cur_mood in mood_opts else 0
        mood = st.selectbox("Daily Mood Focus", mood_opts, index=mood_idx, key=f"mod_{today_str}")
        
        td["sleep_hrs"] = sleep_hrs
        td["hrv"] = hrv
        td["rhr"] = rhr
        td["mood"] = mood
        save_json_file(HABITS_FILE, all_habits)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_d3:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("📝 Physical & Spiritual")
        st.caption("Weight and scripture reading notes")
        
        weight = st.number_input("Current Weight (lbs)", value=float(td.get("weight", 192.5)), step=0.1, key=f"wt_{today_str}")
        devo_notes = st.text_input("Devotional Focus", value=str(td.get("devo_notes", "Proverbs 28 / Lionhearted Faith")), key=f"nts_{today_str}")
        chapters_read = st.text_input("Bible Plan Passages", value=str(td.get("chapters_read", "Genesis 1-3 / Matthew 1")), key=f"pln_{today_str}")
        
        td["weight"] = weight
        td["devo_notes"] = devo_notes
        td["chapters_read"] = chapters_read
        save_json_file(HABITS_FILE, all_habits)
        st.markdown("</div>", unsafe_allow_html=True)

    # Scorecard Summary Card
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    completed = sum([devotional, lift, water, bible])
    score_pct = completed / 4.0
    st.subheader(f"Scorecard Summary: {completed} / 4 Rules Completed ({int(score_pct * 100)}%)")
    st.progress(score_pct)
    
    if completed == 4:
        st.success("🔥 LION DOMINANCE DAY! All 4 Core Rules Completed!")
    elif completed >= 2:
        st.info("⚡ Good Momentum! Keep pushing to complete your mission before 11:59 PM.")
    else:
        st.warning("🦁 The day is young. Attack your core discipline rules!")
        
    if st.button("💾 Log Daily Scorecard to History"):
        log_entry = {
            "Date": today_str, "Devotional": devotional, "Lift": lift, "Water": water, "Bible": bible,
            "Score": f"{completed}/4", "Weight": weight, "Sleep": sleep_hrs, "HRV": hrv, "RHR": rhr, "Mood": mood
        }
        df_log = pd.DataFrame([log_entry])
        if os.path.exists("chase_the_lion_daily_history.csv"):
            df_log.to_csv("chase_the_lion_daily_history.csv", mode='a', header=False, index=False)
        else:
            df_log.to_csv("chase_the_lion_daily_history.csv", mode='w', header=True, index=False)
        st.success("✅ Daily Scorecard committed to history log!")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: 12-WEEK LIFT ENGINE
# ==============================================================================
with tab_lift:
    st.markdown("### 12-Week Ultimate Lift Engine — Real-Time Tracker")
    st.caption("Select your training phase, week, and day to execute progressive overload matrices.")

    col_p, col_w, col_d = st.columns(3)
    with col_p:
        phase = st.selectbox("Training Phase:", [
            "Phase 1: Base Phase (Weeks 1-4)",
            "Phase 2: Structural Shift (Weeks 5-8)",
            "Phase 3: Peak Hypertrophy (Weeks 9-12)"
        ])
    with col_w:
        if "Phase 1" in phase:
            week = st.selectbox("Select Week:", ["Week 1 (Baseline)", "Week 2 (Progression)", "Week 3 (Peak Base Volume)", "Week 4 (Deload & Test)"])
        elif "Phase 2" in phase:
            week = st.selectbox("Select Week:", ["Week 5 (Structural Intro)", "Week 6 (Eccentric Tempo)", "Week 7 (Density Peak)", "Week 8 (Deload)"])
        else:
            week = st.selectbox("Select Week:", ["Week 9 (Hypertrophy Intro)", "Week 10 (Double Supersets)", "Week 11 (Peak Fiber Recruitment)", "Week 12 (Pump Deload)"])
    with col_d:
        day = st.selectbox("Training Day:", [
            "Day 1: Push (Chest / Shoulders / Triceps)",
            "Day 2: Pull (Back / Rear Delts / Biceps)",
            "Day 3: Lower Hypertrophy (Quads / Hams / Calves)",
            "Day 4: Active Recovery & Mobility",
            "Day 5: Upper Hypertrophy / Pump",
            "Day 6: Arms, Calves & Core",
            "Day 7: Off & Regeneration"
        ])

    st.markdown("<hr style='border-color: #2D2D2D;'>", unsafe_allow_html=True)
    
    # Workout routine dictionary generator
    def get_workout_structure(day_str):
        if "Day 4" in day_str:
            return [
                {"series": "Recovery", "exercise": "Thoracic & Hip Mobility Circuit", "sets": 3, "reps": "10 mins", "rpe": "4", "wt": 0},
                {"series": "Recovery", "exercise": "Diaphragmatic Breathing & Foam Rolling", "sets": 1, "reps": "15 mins", "rpe": "3", "wt": 0},
                {"series": "Recovery", "exercise": "45-Min Outdoor Zone 2 Walk", "sets": 1, "reps": "45 mins", "rpe": "5", "wt": 0}
            ]
        elif "Day 7" in day_str:
            return [{"series": "Rest", "exercise": "Full Body Rest & Joint Recovery", "sets": 1, "reps": "Full Day", "rpe": "0", "wt": 0}]
        elif "Push" in day_str:
            return [
                {"series": "A-Series", "exercise": "Barbell Bench Press / Incline Press", "sets": 4, "reps": "6-8", "rpe": "8", "wt": 185},
                {"series": "B1", "exercise": "Seated Overhead Dumbbell Press", "sets": 3, "reps": "8-10", "rpe": "8", "wt": 60},
                {"series": "B2", "exercise": "Weighted Dips", "sets": 3, "reps": "8-12", "rpe": "8", "wt": 45},
                {"series": "C-Series", "exercise": "Cable Lateral Raises", "sets": 3, "reps": "12-15", "rpe": "9", "wt": 25},
                {"series": "C-Series", "exercise": "Tricep Overhead Rope Extension", "sets": 3, "reps": "12-15", "rpe": "9", "wt": 50}
            ]
        elif "Pull" in day_str:
            return [
                {"series": "A-Series", "exercise": "Weighted Pull-Ups / Barbell Row", "sets": 4, "reps": "6-8", "rpe": "8", "wt": 135},
                {"series": "B1", "exercise": "Chest-Supported T-Bar Row", "sets": 3, "reps": "8-10", "rpe": "8", "wt": 115},
                {"series": "B2", "exercise": "Lat Pulldown (Neutral Grip)", "sets": 3, "reps": "10-12", "rpe": "8", "wt": 140},
                {"series": "C-Series", "exercise": "Face Pulls", "sets": 3, "reps": "15-20", "rpe": "8", "wt": 40},
                {"series": "C-Series", "exercise": "Incline Dumbbell Bicep Curls", "sets": 3, "reps": "10-12", "rpe": "9", "wt": 35}
            ]
        return [
            {"series": "A-Series", "exercise": "Primary Compound Movement", "sets": 4, "reps": "8-10", "rpe": "8", "wt": 135},
            {"series": "B1", "exercise": "Secondary Accessory Lift", "sets": 3, "reps": "10-12", "rpe": "8", "wt": 75}
        ]

    exercises = get_workout_structure(day)
    total_sets = sum([ex["sets"] for ex in exercises])
    completed_sets = 0
    workout_prefix = f"{phase}_{week}_{day}"

    for ex_idx, ex in enumerate(exercises):
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        col_e1, col_e2 = st.columns([2, 1])
        with col_e1:
            st.markdown(f"**[{ex['series']}] {ex['exercise']}**")
            st.caption(f"Target Reps: {ex['reps']} | Target RPE: {ex['rpe']}")
        with col_e2:
            used_wt = st.number_input("Weight (lbs)", value=int(ex["wt"]), step=5, key=f"{workout_prefix}_wt_{ex_idx}")
            
        st.write("Mark Completed Sets:")
        set_cols = st.columns(max(ex["sets"], 1))
        for s in range(1, ex["sets"] + 1):
            s_key = f"{workout_prefix}_ex{ex_idx}_set{s}"
            with set_cols[s - 1]:
                if st.checkbox(f"Set {s}", key=s_key):
                    completed_sets += 1
        st.markdown("</div>", unsafe_allow_html=True)

    # Progress Bar
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    prog = completed_sets / total_sets if total_sets > 0 else 1.0
    st.subheader(f"Workout Progress: {completed_sets} / {total_sets} Sets Completed ({int(prog * 100)}%)")
    st.progress(prog)
    
    session_notes = st.text_area("Session Notes (Pump quality, joint health, energy level):", key=f"notes_{workout_prefix}")
    if st.button("💾 Save Completed Workout Session"):
        log_rec = {
            "Date": today_str, "Phase": phase, "Week": week, "Day": day,
            "Sets Completed": f"{completed_sets}/{total_sets}", "Progress": f"{int(prog * 100)}%", "Notes": session_notes
        }
        df_w = pd.DataFrame([log_rec])
        if os.path.exists(WORKOUT_FILE):
            df_w.to_csv(WORKOUT_FILE, mode='a', header=False, index=False)
        else:
            df_w.to_csv(WORKOUT_FILE, mode='w', header=True, index=False)
        st.success("✅ Workout session logged successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: NUTRITION & MACROS
# ==============================================================================
with tab_nutr:
    st.markdown("### Nutrition & Macro Engine")
    st.caption("Target caloric profiles and daily meal execution checklists.")

    profile = st.radio("Select Day Type Target Profile:", ["Standard Lift Day (2,800 kcal)", "Leg Day Peak (2,900 kcal)", "Rest Day Recovery (2,400 kcal)"], horizontal=True)

    if "Standard" in profile:
        kcal, p, c, f = 2800, 200, 315, 80
    elif "Leg" in profile:
        kcal, p, c, f = 2900, 200, 340, 75
    else:
        kcal, p, c, f = 2400, 200, 180, 90

    mc1, mc2, mc3, mc4 = st.columns(4)
    mc1.metric("Calories", f"{kcal} kcal")
    mc2.metric("Protein", f"{p} g")
    mc3.metric("Carbs", f"{c} g")
    mc4.metric("Fats", f"{f} g")

    st.markdown("<hr style='border-color: #2D2D2D;'>", unsafe_allow_html=True)
    st.subheader("🍽️ Daily Fuel & Meal Blocks")

    meals = [
        ("4:15 AM", "Wake Up, Hydrate & Pre-Workout Fuel", "Drink 16-20 oz water + pre-workout meal (Oats / Whey / Banana)."),
        ("5:00 AM", "12-Week Lift Session", "Execute scheduled Lift Engine workout with high intensity."),
        ("6:30 AM", "Post-Workout Recovery Breakfast & Devotional", "High-protein meal + Personal Devotional & Bible Plan reading."),
        ("8:00 AM", "High-Focus Deep Work Block", "Peak cognitive energy window — attack priority work goals."),
        ("12:30 PM", "High-Performance Fuel Lunch & Hydration", "Lean protein + complex carbs + continue 1-gallon water goal."),
        ("5:00 PM", "Evening Mobility & Active Recovery", "Zone 2 walk, stretching, joint health & family connection."),
        ("6:30 PM", "Anabolic Dinner", "Nutrient-dense dinner supporting muscle synthesis."),
        ("9:30 PM", "Peptide Protocol & Night Wind Down", "BPC-157 / CJC administration on empty stomach + 7.5 hrs sleep focus.")
    ]

    completed_meals = 0
    for idx, (m_time, m_title, m_desc) in enumerate(meals):
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        chk = st.checkbox(f"**{m_time} — {m_title}**\n\n_{m_desc}_", key=f"meal_{today_str}_{idx}")
        if chk:
            completed_meals += 1
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    meal_pct = completed_meals / len(meals)
    st.subheader(f"Meal Execution Score: {completed_meals} / {len(meals)} Blocks Completed ({int(meal_pct * 100)}%)")
    st.progress(meal_pct)
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: PEPTIDE PROTOCOL
# ==============================================================================
with tab_pep:
    st.markdown("### Peptide Protocol & Daily Injection Tracker")
    st.caption("BPC-157 / TB-500 regenerative tissue repair and joint health protocol.")

    col_pep1, col_pep2 = st.columns(2)
    with col_pep1:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("New Administration Entry")
        admin_date = st.date_input("Administration Date", datetime.date.today(), key="pep_date")
        dose_mcg = st.number_input("Dosage (mcg)", value=250, step=50, key="pep_dose")
        site = st.selectbox("Injection Site / Target Joint", [
            "Left Shoulder / Rotator Cuff", "Right Shoulder / Rotator Cuff",
            "Left Knee / Patellar Tendon", "Right Knee / Patellar Tendon",
            "Lower Back / Lumbar", "Subcutaneous Abdomen (Systemic)"
        ], key="pep_site")
        fasted = st.checkbox("Administered Fasted (Morning)", value=True, key="pep_fasted")
        pain_scale = st.slider("Joint Pain / Stiffness Level (1 = None, 10 = Severe)", 1, 10, 3, key="pep_pain")
        pep_notes = st.text_input("Protocol Notes", value="Felt great, minor tendon relief.", key="pep_notes")
        
        if st.button("💉 Log Peptide Administration"):
            p_entry = {
                "Date": admin_date.strftime("%Y-%m-%d"), "Dose (mcg)": dose_mcg,
                "Site": site, "Fasted": fasted, "Joint Pain": f"{pain_scale}/10", "Notes": pep_notes
            }
            df_p = pd.DataFrame([p_entry])
            if os.path.exists(PEPTIDE_FILE):
                df_p.to_csv(PEPTIDE_FILE, mode='a', header=False, index=False)
            else:
                df_p.to_csv(PEPTIDE_FILE, mode='w', header=True, index=False)
            st.success("✅ Peptide dose logged successfully to history!")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_pep2:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("Permanent Protocol History")
        if os.path.exists(PEPTIDE_FILE):
            df_pep_hist = pd.read_csv(PEPTIDE_FILE)
            st.dataframe(df_pep_hist, use_container_width=True)
        else:
            st.info("No peptide administration history recorded yet.")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 5: FAITH & REVIEW LOG
# ==============================================================================
with tab_rev:
    st.markdown("### Daily Review & Faith Reflection Log")
    st.caption("End-of-day spiritual and mental debrief. Align your heart and mind with the mission.")

    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    wins = st.text_area("1. What were today's biggest victories (physical, spiritual, or mental)?", placeholder="e.g. Hit heavy overhead press, maintained 100% clean nutrition.")
    battles = st.text_area("2. Where did I face friction, temptation, or weakness today?", placeholder="e.g. Felt fatigue during afternoon slump, but pushed through work.")
    gratitude = st.text_area("3. What am I deeply grateful for today?", placeholder="e.g. Strength, health, family, and God's unwavering grace.")
    tomorrow_goal = st.text_input("4. One primary mission for tomorrow:", value="Attack 5 AM workout with lionhearted intensity and zero excuses.")

    if st.button("💾 Save Daily Reflection & Review"):
        rev_entry = {
            "Date": today_str, "Victories": wins, "Battles Fought": battles,
            "Gratitude": gratitude, "Tomorrow's Mission": tomorrow_goal
        }
        df_rev = pd.DataFrame([rev_entry])
        if os.path.exists(REVIEW_FILE):
            df_rev.to_csv(REVIEW_FILE, mode='a', header=False, index=False)
        else:
            df_rev.to_csv(REVIEW_FILE, mode='w', header=True, index=False)
        st.success("✅ Daily Reflection saved successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

    if os.path.exists(REVIEW_FILE):
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.subheader("📜 Past Daily Reflections")
        df_rev_hist = pd.read_csv(REVIEW_FILE)
        st.dataframe(df_rev_hist, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 6: DAILY SCHEDULE & CALENDAR
# ==============================================================================
with tab_sched:
    st.markdown("### Google Calendar & Daily Tactical Schedule")
    st.caption("Align your daily calendar events with your high-performance routine.")

    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    st.subheader("🦁 The Lionhearted Daily Routine Timeline")
    st.markdown("""
    - **4:15 AM — Wake Up & Fuel:** Pre-workout meal (Oats + Protein / Fruit) + Electrolytes.
    - **5:00 AM — 6:30 AM — Iron Temple (Lift Engine):** Execute daily training block (Phase & Week matrix).
    - **6:30 AM — 7:15 AM — Post-Workout Recovery & Shower:** Protein-rich breakfast & hydration.
    - **7:30 AM — 8:00 AM — Personal Devotional & Bible Reading:** Core Rule 1 & 4 (Year in Bible).
    - **8:00 AM — 5:00 PM — Professional Mission / Deep Work:** High-focus execution blocks.
    - **12:30 PM — Midday Fuel & Walk:** Meal 3 + 15-minute sunlight walk.
    - **6:30 PM — Anabolic Dinner & Family Time:** Meal 4 + evening connection.
    - **9:00 PM — Wind Down & Reflection:** Meal 5, review Daily Discipline Dashboard, prepare for tomorrow.
    """)
    st.info("💡 **Tip:** Copy these time blocks directly into your Google Calendar app or Google Workspace account to keep your day locked in.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr style='border-color: #2D2D2D; margin-top: 2rem;'>", unsafe_allow_html=True)
st.caption("TXP ✝ Chase The Lion — Habit & Lift Ecosystem | High-Performance Tactical Suite v10.0")
