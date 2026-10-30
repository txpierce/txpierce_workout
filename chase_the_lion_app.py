<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TXP ✝ Chase The Lion — Tactical Habit & Lift Ecosystem</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        hyrox: {
                            yellow: '#FFCC00',
                            dark: '#121212',
                            card: '#1E1E1E',
                            border: '#2D2D2D',
                            hover: '#333333'
                        }
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #121212; color: #E5E7EB; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        input[type="date"], input[type="text"], input[type="number"], select, textarea {
            background-color: #1E1E1E; border: 1px solid #374151; color: #F3F4F6;
        }
        input:focus, select:focus, textarea:focus {
            border-color: #FFCC00; outline: none; ring: 2px; ring-color: #FFCC00;
        }
        .set-checkbox:checked + span {
            background-color: #FFCC00; color: #000; border-color: #FFCC00; text-decoration: line-through;
        }
        .scripture-box {
            background: linear-gradient(135deg, #1a1f2c 0%, #11141d 100%);
            border-left: 4px solid #FFCC00;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">

    <!-- Top Navigation / Header -->
    <header class="bg-black border-b border-gray-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center space-x-3">
                <div class="bg-hyrox-yellow text-black font-black px-3 py-1.5 text-xl tracking-wider rounded">TXP</div>
                <div>
                    <h1 class="text-lg font-bold text-white tracking-wide">CHASE THE LION ECOSYSTEM</h1>
                    <p class="text-xs text-gray-400">Daily Discipline | 12-Week Lift Engine | Peptides & Faith</p>
                </div>
            </div>
            <!-- Navigation Tabs -->
            <div class="flex items-center gap-2 flex-wrap justify-center">
                <nav class="flex flex-wrap justify-center gap-1.5 bg-gray-900 p-1 rounded-lg border border-gray-800">
                    <button onclick="switchTab('dashboard')" id="btn-dashboard" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded bg-hyrox-yellow text-black transition">Dashboard</button>
                    <button onclick="switchTab('lift')" id="btn-lift" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">12-Week Lift Engine</button>
                    <button onclick="switchTab('nutrition')" id="btn-nutrition" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Nutrition & Macros</button>
                    <button onclick="switchTab('peptides')" id="btn-peptides" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Peptide Tracker</button>
                    <button onclick="switchTab('review')" id="btn-review" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Faith Reflection</button>
                    <button onclick="switchTab('schedule')" id="btn-schedule" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Daily Schedule</button>
                </nav>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 py-6 w-full flex-grow space-y-6">

        <!-- ================= TAB 1: DASHBOARD ================= -->
        <div id="tab-dashboard" class="tab-content active space-y-6">
            <!-- Scripture Banner -->
            <div class="scripture-box p-6 rounded-xl shadow-xl flex flex-col md:flex-row items-center justify-between gap-6 border border-gray-800">
                <div class="space-y-2">
                    <span class="bg-hyrox-yellow/10 text-hyrox-yellow border border-hyrox-yellow/30 text-xs px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">Lionhearted Creed</span>
                    <h2 class="text-xl md:text-2xl font-black text-white italic">"The wicked flee when no one pursues, but the righteous are bold as a lion."</h2>
                    <p class="text-xs text-hyrox-yellow font-bold">— Proverbs 28:1</p>
                </div>
                <div class="bg-black/60 border border-gray-800 px-5 py-4 rounded-xl text-center min-w-[180px]">
                    <div id="today-date-display" class="text-xs text-gray-400 uppercase font-semibold">Today's Discipline</div>
                    <div id="discipline-score-display" class="text-3xl font-black text-hyrox-yellow mt-1">0 / 4</div>
                    <div class="text-[10px] text-gray-400 uppercase tracking-widest mt-0.5">Core Rules Completed</div>
                </div>
            </div>

            <!-- Daily Discipline Scorecard Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Core Rules Checklist -->
                <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-shield-halved text-hyrox-yellow"></i> Core Discipline Rules
                    </h3>
                    <p class="text-xs text-gray-400">Check off your daily non-negotiable mission rules.</p>
                    <div class="space-y-3 pt-2">
                        <label class="flex items-center gap-3 bg-black/40 p-3 rounded-xl border border-gray-800 cursor-pointer hover:border-gray-700 transition">
                            <input type="checkbox" id="rule-devotional" onchange="saveDashboardData()" class="w-5 h-5 rounded accent-yellow-400">
                            <div>
                                <div class="text-xs font-bold text-white">Rule 1: Personal Devotional</div>
                                <div class="text-[10px] text-gray-400">Morning scripture & prayer alignment</div>
                            </div>
                        </label>
                        <label class="flex items-center gap-3 bg-black/40 p-3 rounded-xl border border-gray-800 cursor-pointer hover:border-gray-700 transition">
                            <input type="checkbox" id="rule-lift" onchange="saveDashboardData()" class="w-5 h-5 rounded accent-yellow-400">
                            <div>
                                <div class="text-xs font-bold text-white">Rule 2: Lift Session Executed</div>
                                <div class="text-[10px] text-gray-400">Attack scheduled 12-week workout</div>
                            </div>
                        </label>
                        <label class="flex items-center gap-3 bg-black/40 p-3 rounded-xl border border-gray-800 cursor-pointer hover:border-gray-700 transition">
                            <input type="checkbox" id="rule-water" onchange="saveDashboardData()" class="w-5 h-5 rounded accent-yellow-400">
                            <div>
                                <div class="text-xs font-bold text-white">Rule 3: Gallon Water (128 oz)</div>
                                <div class="text-[10px] text-gray-400">Optimal hydration & tissue recovery</div>
                            </div>
                        </label>
                        <label class="flex items-center gap-3 bg-black/40 p-3 rounded-xl border border-gray-800 cursor-pointer hover:border-gray-700 transition">
                            <input type="checkbox" id="rule-bible" onchange="saveDashboardData()" class="w-5 h-5 rounded accent-yellow-400">
                            <div>
                                <div class="text-xs font-bold text-white">Rule 4: Year In Bible Reading</div>
                                <div class="text-[10px] text-gray-400">Daily chronological chapters</div>
                            </div>
                        </label>
                    </div>
                </div>

                <!-- Health Metrics & Biometrics -->
                <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-heart-pulse text-hyrox-yellow"></i> Biometrics & Vitals
                    </h3>
                    <p class="text-xs text-gray-400">Log sleep, HRV, and resting heart rate.</p>
                    <div class="space-y-3 pt-1 text-xs">
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Sleep Duration (Hours)</label>
                            <input type="number" step="0.5" id="bio-sleep" value="7.5" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Heart Rate Variability (HRV ms)</label>
                            <input type="number" id="bio-hrv" value="65" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Resting Heart Rate (RHR bpm)</label>
                            <input type="number" id="bio-rhr" value="54" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Current Body Weight (lbs)</label>
                            <input type="number" step="0.1" id="bio-weight" value="192.5" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                    </div>
                </div>

                <!-- Daily Notes & Mood Focus -->
                <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-brain text-hyrox-yellow"></i> Mental & Spiritual Focus
                    </h3>
                    <p class="text-xs text-gray-400">Daily mindset and tactical intentions.</p>
                    <div class="space-y-3 text-xs">
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Daily Mood / Energy Focus</label>
                            <select id="bio-mood" onchange="saveDashboardData()" class="w-full p-2 rounded bg-black text-white">
                                <option>Driven 🦁</option>
                                <option>Focused ⚡</option>
                                <option>Sore 💪</option>
                                <option>Fatigued 😴</option>
                                <option>Reflective 🙏</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Devotional Passage Focus</label>
                            <input type="text" id="bio-devo" value="Proverbs 28 / Lionhearted Faith" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Year in Bible Passages Read</label>
                            <input type="text" id="bio-bible-notes" value="Genesis 1-3 / Matthew 1" oninput="saveDashboardData()" class="w-full p-2 rounded">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 2: 12-WEEK LIFT ENGINE ================= -->
        <div id="tab-lift" class="tab-content space-y-6">
            <!-- Overall Progress Meter Banner -->
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-3">
                <div class="flex justify-between items-center">
                    <div>
                        <h2 class="text-xl font-bold text-white">12-Week Ultimate Lift Engine</h2>
                        <p class="text-xs text-gray-400">Select phase, week, and day. Check off sets in real-time as you train.</p>
                    </div>
                    <div class="text-right">
                        <span id="lift-progress-text" class="text-sm font-black text-hyrox-yellow">0% Completed</span>
                        <div class="text-[10px] text-gray-400 uppercase">Engine Progress</div>
                    </div>
                </div>
                <div class="w-full bg-black/70 border border-gray-800 rounded-full h-3 overflow-hidden">
                    <div id="lift-progress-bar" class="bg-hyrox-yellow h-full transition-all duration-300" style="width: 0%;"></div>
                </div>
            </div>

            <!-- Selector Controls -->
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-4 shadow-lg grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                    <label class="block text-[10px] text-gray-400 uppercase font-semibold mb-1">Training Phase</label>
                    <select id="lift-phase-select" onchange="updateLiftWeekOptions()" class="w-full rounded px-3 py-2 text-xs font-bold bg-black text-white">
                        <option value="phase1">Phase 1: Base Phase (Weeks 1-4)</option>
                        <option value="phase2">Phase 2: Structural Shift (Weeks 5-8)</option>
                        <option value="phase3">Phase 3: Peak Hypertrophy (Weeks 9-12)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-[10px] text-gray-400 uppercase font-semibold mb-1">Select Week</label>
                    <select id="lift-week-select" onchange="renderLiftWorkout()" class="w-full rounded px-3 py-2 text-xs font-bold bg-black text-white">
                        <!-- Populated by JS -->
                    </select>
                </div>
                <div>
                    <label class="block text-[10px] text-gray-400 uppercase font-semibold mb-1">Training Day</label>
                    <select id="lift-day-select" onchange="renderLiftWorkout()" class="w-full rounded px-3 py-2 text-xs font-bold bg-black text-white">
                        <option value="0">Day 1: Push (Chest / Shoulders / Triceps)</option>
                        <option value="1">Day 2: Pull (Back / Rear Delts / Biceps)</option>
                        <option value="2">Day 3: Lower Hypertrophy (Quads / Hams / Calves)</option>
                        <option value="3">Day 4: Active Recovery & Mobility</option>
                        <option value="4">Day 5: Upper Hypertrophy / Pump</option>
                        <option value="5">Day 6: Arms, Calves & Core</option>
                        <option value="6">Day 7: Off & Regeneration</option>
                    </select>
                </div>
            </div>

            <!-- Workout Render Container -->
            <div id="lift-workout-container" class="space-y-4"></div>
        </div>

        <!-- ================= TAB 3: NUTRITION & MACROS ================= -->
        <div id="tab-nutrition" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-6">
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-gray-800 pb-4">
                    <div>
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-utensils text-hyrox-yellow"></i> Nutrition & Macro Engine
                        </h2>
                        <p class="text-xs text-gray-400">Target macros and daily meal execution checklist.</p>
                    </div>
                    <div class="flex items-center gap-2">
                        <label class="text-xs text-gray-300 font-semibold">Day Target Profile:</label>
                        <select id="macro-profile-select" onchange="updateMacroTargets()" class="rounded px-3 py-1.5 text-xs font-bold bg-black text-white">
                            <option value="standard">Standard Lift Day (2800 kcal)</option>
                            <option value="leg">Leg Day Peak (2900 kcal)</option>
                            <option value="rest">Rest Day Recovery (2400 kcal)</option>
                        </select>
                    </div>
                </div>

                <!-- Macro Badges -->
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-black/60 border border-gray-800 p-4 rounded-xl">
                        <div id="macro-kcal" class="text-2xl font-black text-hyrox-yellow">2,800</div>
                        <div class="text-[10px] text-gray-400 uppercase mt-1">Daily Calories (kcal)</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 p-4 rounded-xl">
                        <div id="macro-protein" class="text-2xl font-black text-white">200g</div>
                        <div class="text-[10px] text-gray-400 uppercase mt-1">Protein Target</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 p-4 rounded-xl">
                        <div id="macro-carbs" class="text-2xl font-black text-white">315g</div>
                        <div class="text-[10px] text-gray-400 uppercase mt-1">Carbohydrates</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 p-4 rounded-xl">
                        <div id="macro-fats" class="text-2xl font-black text-white">80g</div>
                        <div class="text-[10px] text-gray-400 uppercase mt-1">Healthy Fats</div>
                    </div>
                </div>

                <!-- Meal Blocks Checklist -->
                <div class="border-t border-gray-800 pt-4 space-y-3">
                    <h3 class="text-sm font-bold text-white uppercase tracking-wider text-hyrox-yellow">Daily Meal & Fuel Blocks</h3>
                    <div id="meal-blocks-container" class="space-y-3">
                        <!-- Populated via JS -->
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 4: PEPTIDE PROTOCOL ================= -->
        <div id="tab-peptides" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-6">
                <div class="border-b border-gray-800 pb-3">
                    <h2 class="text-xl font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-syringe text-hyrox-yellow"></i> Peptide Protocol & Daily Injection Tracker
                    </h2>
                    <p class="text-xs text-gray-400 mt-1">BPC-157 / TB-500 regenerative tissue repair and joint health protocol.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-4 text-xs bg-black/40 p-5 rounded-xl border border-gray-800">
                        <h3 class="text-sm font-bold text-hyrox-yellow">New Administration Entry</h3>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Date</label>
                            <input type="date" id="pep-date" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Dosage (mcg)</label>
                            <input type="number" id="pep-dose" value="250" class="w-full p-2 rounded">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Injection Site / Target Joint</label>
                            <select id="pep-site" class="w-full p-2 rounded bg-black text-white">
                                <option>Left Shoulder / Rotator Cuff</option>
                                <option>Right Shoulder / Rotator Cuff</option>
                                <option>Left Knee / Patellar Tendon</option>
                                <option>Right Knee / Patellar Tendon</option>
                                <option>Lower Back / Lumbar</option>
                                <option>Subcutaneous Abdomen (Systemic)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Joint Pain / Stiffness Level (1 = None, 10 = Severe)</label>
                            <input type="range" min="1" max="10" value="3" id="pep-pain" oninput="document.getElementById('pain-val').innerText=this.value" class="w-full accent-yellow-400">
                            <div class="text-center font-bold text-hyrox-yellow mt-1">Current Rating: <span id="pain-val">3</span> / 10</div>
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-1 font-semibold">Protocol Notes</label>
                            <input type="text" id="pep-notes" placeholder="Felt great, minor tendon relief." class="w-full p-2 rounded">
                        </div>
                        <button onclick="logPeptideEntry()" class="w-full bg-hyrox-yellow text-black font-bold py-2.5 rounded-lg hover:bg-yellow-400 transition">
                            Log Administration
                        </button>
                    </div>

                    <div class="space-y-4">
                        <h3 class="text-sm font-bold text-white">Permanent Administration History</h3>
                        <div class="overflow-x-auto max-h-96 overflow-y-auto border border-gray-800 rounded-lg">
                            <table class="w-full text-left text-xs">
                                <thead class="bg-black/60 text-gray-400 uppercase text-[10px] sticky top-0">
                                    <tr>
                                        <th class="p-2.5">Date</th>
                                        <th class="p-2.5">Dose</th>
                                        <th class="p-2.5">Site</th>
                                        <th class="p-2.5">Pain</th>
                                        <th class="p-2.5">Notes</th>
                                    </tr>
                                </thead>
                                <tbody id="peptide-history-tbody" class="divide-y divide-gray-800 text-gray-300">
                                    <tr><td colspan="5" class="p-4 text-center text-gray-500">No peptide logs recorded yet.</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 5: DAILY REVIEW & FAITH ================= -->
        <div id="tab-review" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                <div class="border-b border-gray-800 pb-3 flex justify-between items-center">
                    <div>
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-hands-praying text-hyrox-yellow"></i> Daily Review & Faith Reflection Log
                        </h2>
                        <p class="text-xs text-gray-400 mt-1">End-of-day spiritual and mental debrief. Align your heart and mind with the mission.</p>
                    </div>
                    <button onclick="saveDailyReview()" class="bg-hyrox-yellow text-black px-4 py-2 rounded-lg font-bold text-xs hover:bg-yellow-400 transition">Save Reflection</button>
                </div>
                <div class="space-y-4 text-xs">
                    <div>
                        <label class="block text-gray-400 mb-1 font-semibold">1. What were today's biggest victories (physical, spiritual, or mental)?</label>
                        <textarea id="rev-wins" rows="2" placeholder="e.g., Hit heavy overhead press, maintained 100% clean nutrition." class="w-full p-2.5 rounded"></textarea>
                    </div>
                    <div>
                        <label class="block text-gray-400 mb-1 font-semibold">2. Where did I face friction, temptation, or weakness today?</label>
                        <textarea id="rev-battles" rows="2" placeholder="e.g., Felt fatigue during afternoon slump, but pushed through work." class="w-full p-2.5 rounded"></textarea>
                    </div>
                    <div>
                        <label class="block text-gray-400 mb-1 font-semibold">3. What am I deeply grateful for today?</label>
                        <textarea id="rev-gratitude" rows="2" placeholder="e.g., Strength, health, family, and God's unwavering grace." class="w-full p-2.5 rounded"></textarea>
                    </div>
                    <div>
                        <label class="block text-gray-400 mb-1 font-semibold">4. One primary mission for tomorrow:</label>
                        <input type="text" id="rev-mission" value="Attack 5 AM workout with lionhearted intensity and zero excuses." class="w-full p-2.5 rounded">
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 6: SCHEDULE & CALENDAR ================= -->
        <div id="tab-schedule" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                <h2 class="text-xl font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-calendar-days text-hyrox-yellow"></i> Google Calendar & Daily Tactical Schedule
                </h2>
                <p class="text-xs text-gray-400">Align your daily calendar events with your high-performance routine.</p>
                <div class="bg-black/50 border border-gray-800 p-5 rounded-xl space-y-3 text-xs text-gray-300">
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">4:15 AM</strong> <span>Wake Up & Fuel (Pre-workout meal + Electrolytes)</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">5:00 AM</strong> <span>Iron Temple (12-Week Lift Engine Workout Block)</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">6:30 AM</strong> <span>Post-Workout Recovery & Shower (Protein breakfast)</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">7:30 AM</strong> <span>Personal Devotional & Bible Reading</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">8:00 AM</strong> <span>Professional Mission / Deep Work Focus</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">12:30 PM</strong> <span>Midday Fuel & 15-Minute Sunlight Walk</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-2"><strong class="text-hyrox-yellow">6:30 PM</strong> <span>Anabolic Dinner & Family Time</span></div>
                    <div class="flex justify-between"><strong class="text-hyrox-yellow">9:00 PM</strong> <span>Wind Down, Daily Review, & Sleep Preparation (7.5 hrs)</span></div>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-black border-t border-gray-800 py-4 text-center text-xs text-gray-500">
        <p>TXP ✝ Chase The Lion — Habit & Lift Ecosystem | High-Performance Tactical Suite</p>
    </footer>

    <!-- JavaScript Application Logic -->
    <script>
        // Tab Navigation Switcher
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => {
                el.classList.remove('bg-hyrox-yellow', 'text-black');
                el.classList.add('text-gray-300', 'hover:bg-gray-800');
            });
            document.getElementById('tab-' + tabId).classList.add('active');
            const btn = document.getElementById('btn-' + tabId);
            if(btn) {
                btn.classList.remove('text-gray-300', 'hover:bg-gray-800');
                btn.classList.add('bg-hyrox-yellow', 'text-black');
            }
        }

        // Today's Date Setup
        const todayStr = new Date().toISOString().split('T')[0];
        document.getElementById('today-date-display').innerText = `Today (${new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })})`;

        // Dashboard LocalStorage Persistence & Scoring
        function saveDashboardData() {
            const data = {
                devotional: document.getElementById('rule-devotional').checked,
                lift: document.getElementById('rule-lift').checked,
                water: document.getElementById('rule-water').checked,
                bible: document.getElementById('rule-bible').checked,
                sleep: document.getElementById('bio-sleep').value,
                hrv: document.getElementById('bio-hrv').value,
                rhr: document.getElementById('bio-rhr').value,
                weight: document.getElementById('bio-weight').value,
                mood: document.getElementById('bio-mood').value,
                devo: document.getElementById('bio-devo').value,
                bibleNotes: document.getElementById('bio-bible-notes').value
            };
            localStorage.setItem(`ctl_dash_${todayStr}`, JSON.stringify(data));
            updateDisciplineScore();
        }

        function loadDashboardData() {
            const saved = JSON.parse(localStorage.getItem(`ctl_dash_${todayStr}`));
            if (!saved) return;
            document.getElementById('rule-devotional').checked = saved.devotional || false;
            document.getElementById('rule-lift').checked = saved.lift || false;
            document.getElementById('rule-water').checked = saved.water || false;
            document.getElementById('rule-bible').checked = saved.bible || false;
            if(saved.sleep) document.getElementById('bio-sleep').value = saved.sleep;
            if(saved.hrv) document.getElementById('bio-hrv').value = saved.hrv;
            if(saved.rhr) document.getElementById('bio-rhr').value = saved.rhr;
            if(saved.weight) document.getElementById('bio-weight').value = saved.weight;
            if(saved.mood) document.getElementById('bio-mood').value = saved.mood;
            if(saved.devo) document.getElementById('bio-devo').value = saved.devo;
            if(saved.bibleNotes) document.getElementById('bio-bible-notes').value = saved.bibleNotes;
            updateDisciplineScore();
        }

        function updateDisciplineScore() {
            const count = [
                document.getElementById('rule-devotional').checked,
                document.getElementById('rule-lift').checked,
                document.getElementById('rule-water').checked,
                document.getElementById('rule-bible').checked
            ].filter(Boolean).length;
            document.getElementById('discipline-score-display').innerText = `${count} / 4`;
        }

        // ================= 12-WEEK LIFT ENGINE DATA & LOGIC ================= //
        const liftPhases = {
            phase1: {
                name: "Phase 1: Base Phase",
                weeks: {
                    "Week 1 (Baseline)": { title: "WEEK 1 — BASELINE WEEK: Movement Quality", focus: "Build movement quality, tissue tolerance, and structural balance." },
                    "Week 2 (Progression)": { title: "WEEK 2 — PROGRESSION WEEK: Volume & Harder Variations", focus: "Increase volume by adding +1 set across B-Series exercises." },
                    "Week 3 (Peak Base Volume)": { title: "WEEK 3 — COMPLEXITY WEEK: Higher Intensity", focus: "A-Series shifts to 6x4 @ RPE 8-9 for power and precision." },
                    "Week 4 (Deload & Test)": { title: "WEEK 4 — PEAK BASE WEEK: Peak Volume & Deload", focus: "Deload A-Series load (4x8 @ RPE 7-8) to protect joints." }
                }
            },
            phase2: {
                name: "Phase 2: Structural Shift",
                weeks: {
                    "Week 5 (Structural Intro)": { title: "WEEK 5 — STRUCTURAL SHIFT: New Patterns & Angles", focus: "Introduces new primary A-Series lifts and angles." },
                    "Week 6 (Eccentric Tempo)": { title: "WEEK 6 — VOLUME & TEMPO: 3-Second Negative", focus: "Controlled tempo: 3-second eccentric + 1-second stretch pause." },
                    "Week 7 (Density Peak)": { title: "WEEK 7 — HIGH-DENSITY SHOCK: Tri-Sets", focus: "B-Series supersets convert into non-competing tri-sets." },
                    "Week 8 (Deload)": { title: "WEEK 8 — PEAK HYPERTROPHY WEEK", focus: "Peak hypertrophy stimulus, mechanical drop sets." }
                }
            },
            phase3: {
                name: "Phase 3: Peak Hypertrophy",
                weeks: {
                    "Week 9 (Hypertrophy Intro)": { title: "WEEK 9 — PEAK HYPERTROPHY: Block 3", focus: "Maximize motor unit recruitment and mechanical tension." },
                    "Week 10 (Double Supersets)": { title: "WEEK 10 — INTENSITY SHOCK: Double Supersets", focus: "Zero rest transitions between accessory supersets." },
                    "Week 11 (Peak Fiber Recruitment)": { title: "WEEK 11 — PEAK FIBER RECRUITMENT", focus: "Heavy compound loading coupled with pump finishers." },
                    "Week 12 (Pump Deload & Test)": { title: "WEEK 12 — FINAL CAPSTONE & DELOAD", focus: "Celebrate the journey, test mobility and pump quality." }
                }
            }
        };

        function updateLiftWeekOptions() {
            const phaseKey = document.getElementById('lift-phase-select').value;
            const weekSelect = document.getElementById('lift-week-select');
            const weeksObj = liftPhases[phaseKey].weeks;
            
            let html = '';
            for (const [wKey, wVal] of Object.entries(weeksObj)) {
                html += `<option value="${wKey}">${wKey}</option>`;
            }
            weekSelect.innerHTML = html;
            renderLiftWorkout();
        }

        function getWorkoutExercises(dayIdx) {
            if (dayIdx === 3) {
                return [
                    { series: "Recovery", exercise: "Thoracic & Hip Mobility Circuit", sets: 3, reps: "10 mins", rpe: "4", rest: "None", defaultWt: 0 },
                    { series: "Recovery", exercise: "Diaphragmatic Breathing & Foam Rolling", sets: 1, reps: "15 mins", rpe: "3", rest: "None", defaultWt: 0 },
                    { series: "Recovery", exercise: "45-Min Outdoor Zone 2 Walk", sets: 1, reps: "45 mins", rpe: "5", rest: "None", defaultWt: 0 }
                ];
            } else if (dayIdx === 6) {
                return [
                    { series: "Rest", exercise: "Full Body Rest & Joint Recovery", sets: 1, reps: "Full Day", rpe: "0", rest: "N/A", defaultWt: 0 }
                ];
            } else if (dayIdx === 0) {
                return [
                    { series: "A-Series", exercise: "Barbell Bench Press / Incline Press", sets: 4, reps: "6-8", rpe: "8", rest: "2 min", defaultWt: 185 },
                    { series: "B1", exercise: "Seated Overhead Dumbbell Press", sets: 3, reps: "8-10", rpe: "8", rest: "90 sec", defaultWt: 60 },
                    { series: "B2", exercise: "Weighted Dips", sets: 3, reps: "8-12", rpe: "8", rest: "90 sec", defaultWt: 45 },
                    { series: "C-Series", exercise: "Cable Lateral Raises", sets: 3, reps: "12-15", rpe: "9", rest: "60 sec", defaultWt: 25 },
                    { series: "C-Series", exercise: "Tricep Overhead Rope Extension", sets: 3, reps: "12-15", rpe: "9", rest: "60 sec", defaultWt: 50 }
                ];
            } else if (dayIdx === 1) {
                return [
                    { series: "A-Series", exercise: "Weighted Pull-Ups / Barbell Row", sets: 4, reps: "6-8", rpe: "8", rest: "2 min", defaultWt: 135 },
                    { series: "B1", exercise: "Chest-Supported T-Bar Row", sets: 3, reps: "8-10", rpe: "8", rest: "90 sec", defaultWt: 115 },
                    { series: "B2", exercise: "Lat Pulldown (Neutral Grip)", sets: 3, reps: "10-12", rpe: "8", rest: "90 sec", defaultWt: 140 },
                    { series: "C-Series", exercise: "Face Pulls", sets: 3, reps: "15-20", rpe: "8", rest: "60 sec", defaultWt: 40 },
                    { series: "C-Series", exercise: "Incline Dumbbell Bicep Curls", sets: 3, reps: "10-12", rpe: "9", rest: "60 sec", defaultWt: 35 }
                ];
            }
            return [
                { series: "A-Series", exercise: "Primary Compound Movement", sets: 4, reps: "8-10", rpe: "8", rest: "2 min", defaultWt: 100 },
                { series: "B1", exercise: "Secondary Accessory Lift", sets: 3, reps: "10-12", rpe: "8", rest: "90 sec", defaultWt: 75 }
            ];
        }

        function renderLiftWorkout() {
            const phaseKey = document.getElementById('lift-phase-select').value;
            const weekKey = document.getElementById('lift-week-select').value;
            const dayIdx = parseInt(document.getElementById('lift-day-select').value) || 0;
            const weekObj = liftPhases[phaseKey].weeks[weekKey] || { title: weekKey, focus: "Execute with high precision." };
            const exercises = getWorkoutExercises(dayIdx);

            const container = document.getElementById('lift-workout-container');
            let html = `
                <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                    <div class="border-b border-gray-800 pb-3">
                        <h3 class="text-base font-black text-hyrox-yellow">${weekObj.title}</h3>
                        <p class="text-xs text-gray-400 mt-1"><strong class="text-white">Focus:</strong> ${weekObj.focus}</p>
                    </div>
                    <div class="space-y-4">
            `;

            exercises.forEach((ex, exIdx) => {
                let setsHtml = '';
                for (let s = 1; s <= ex.sets; s++) {
                    const chkId = `lift_${phaseKey}_${weekKey}_d${dayIdx}_e${exIdx}_s${s}`;
                    setsHtml += `
                        <label class="cursor-pointer inline-flex items-center">
                            <input type="checkbox" class="set-checkbox hidden" id="${chkId}" onchange="saveLiftProgress()">
                            <span class="w-7 h-7 rounded border border-gray-700 bg-black text-xs font-bold flex items-center justify-center text-gray-300 hover:border-hyrox-yellow transition">${s}</span>
                        </label>
                    `;
                }

                html += `
                    <div class="bg-black/40 border border-gray-800 p-4 rounded-xl space-y-3">
                        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                            <div>
                                <span class="bg-hyrox-yellow/10 text-hyrox-yellow border border-hyrox-yellow/30 text-[10px] px-2 py-0.5 rounded font-bold uppercase">${ex.series}</span>
                                <div class="text-sm font-bold text-white mt-1">${ex.exercise}</div>
                                <div class="text-[11px] text-gray-400">Target Reps: ${ex.reps} | RPE: ${ex.rpe} | Rest: ${ex.rest}</div>
                            </div>
                            <div class="flex items-center gap-2">
                                <input type="number" step="5" value="${ex.defaultWt}" id="wt_${phaseKey}_w${weekKey}_d${dayIdx}_e${exIdx}" placeholder="Weight (lbs)" class="w-28 p-1.5 rounded text-xs font-bold text-center">
                            </div>
                        </div>
                        <div class="flex items-center justify-between pt-2 border-t border-gray-800">
                            <span class="text-[10px] text-gray-400 uppercase font-bold">Check Completed Sets:</span>
                            <div class="flex items-center gap-2 flex-wrap justify-end">
                                ${setsHtml}
                            </div>
                        </div>
                    </div>
                `;
            });

            html += `</div></div>`;
            container.innerHTML = html;
            loadLiftProgress();
            updateLiftOverallProgress();
        }

        function saveLiftProgress() {
            const progress = {};
            document.querySelectorAll('input[type="checkbox"][id^="lift_"]').forEach(chk => {
                progress[chk.id] = chk.checked;
            });
            localStorage.setItem('ctl_lift_progress', JSON.stringify(progress));
            updateLiftOverallProgress();
        }

        function loadLiftProgress() {
            const saved = JSON.parse(localStorage.getItem('ctl_lift_progress'));
            if (!saved) return;
            for (const [id, val] of Object.entries(saved)) {
                const el = document.getElementById(id);
                if (el) el.checked = val;
            }
        }

        function updateLiftOverallProgress() {
            const checkboxes = document.querySelectorAll('input[type="checkbox"][id^="lift_"]');
            let checked = 0;
            checkboxes.forEach(chk => { if (chk.checked) checked++; });
            const total = checkboxes.length;
            const pct = total > 0 ? Math.round((checked / total) * 100) : 0;
            document.getElementById('lift-progress-text').innerText = `${pct}% Completed (${checked}/${total} sets)`;
            document.getElementById('lift-progress-bar').style.width = `${pct}%`;
        }

        // ================= NUTRITION & MACROS ================= //
        const macroProfiles = {
            standard: { kcal: 2800, p: 200, c: 315, f: 80 },
            leg: { kcal: 2900, p: 200, c: 340, f: 75 },
            rest: { kcal: 2400, p: 200, c: 180, f: 90 }
        };

        const mealBlocks = [
            { time: "4:15 AM", title: "Wake Up, Hydrate & Pre-Workout Fuel 🥣", desc: "Drink 16-20 oz water + pre-workout meal (Oats / Whey / Banana)." },
            { time: "5:00 AM", title: "12-Week Lift Session 🏋️‍♂️", desc: "Execute scheduled 12-week Lift Engine workout with high intensity." },
            { time: "6:30 AM", title: "Post-Workout Recovery Breakfast & Devotional 🍳📖", desc: "High-protein meal + Personal Devotional & Bible Plan reading." },
            { time: "8:00 AM", title: "High-Focus Deep Work Block ⚡", desc: "Peak cognitive energy window — attack priority work goals." },
            { time: "12:30 PM", title: "High-Performance Fuel Lunch & Hydration 🍗", desc: "Lean protein + complex carbs + continue 1-gallon water goal." },
            { time: "5:00 PM", title: "Evening Mobility, Active Recovery & Family Time 🏃‍♂️", desc: "Zone 2 walk, stretching, joint health & family connection." },
            { time: "6:30 PM", title: "Anabolic Dinner 🥩", desc: "Nutrient-dense dinner supporting muscle synthesis." },
            { time: "9:30 PM", title: "Peptide Protocol & Night Wind Down 💤", desc: "BPC-157 administration on empty stomach + 7.5 hrs sleep focus." }
        ];

        function updateMacroTargets() {
            const profileKey = document.getElementById('macro-profile-select').value;
            const prof = macroProfiles[profileKey];
            document.getElementById('macro-kcal').innerText = prof.kcal.toLocaleString();
            document.getElementById('macro-protein').innerText = prof.p + 'g';
            document.getElementById('macro-carbs').innerText = prof.c + 'g';
            document.getElementById('macro-fats').innerText = prof.f + 'g';
        }

        function renderMealBlocks() {
            const container = document.getElementById('meal-blocks-container');
            let html = '';
            mealBlocks.forEach((meal, idx) => {
                const chkId = `meal_block_${idx}_${todayStr}`;
                html += `
                    <label class="flex items-start gap-3 bg-black/40 p-3.5 rounded-xl border border-gray-800 cursor-pointer hover:border-gray-700 transition">
                        <input type="checkbox" id="${chkId}" onchange="saveMealProgress()" class="w-5 h-5 rounded accent-yellow-400 mt-0.5">
                        <div class="space-y-0.5">
                            <div class="flex items-center gap-2">
                                <span class="bg-hyrox-yellow/20 text-hyrox-yellow text-[10px] font-bold px-2 py-0.5 rounded">${meal.time}</span>
                                <span class="text-xs font-bold text-white">${meal.title}</span>
                            </div>
                            <div class="text-[11px] text-gray-400">${meal.desc}</div>
                        </div>
                    </label>
                `;
            });
            container.innerHTML = html;
            loadMealProgress();
        }

        function saveMealProgress() {
            const prog = {};
            mealBlocks.forEach((_, idx) => {
                const id = `meal_block_${idx}_${todayStr}`;
                const el = document.getElementById(id);
                if (el) prog[id] = el.checked;
            });
            localStorage.setItem('ctl_meal_progress', JSON.stringify(prog));
        }

        function loadMealProgress() {
            const saved = JSON.parse(localStorage.getItem('ctl_meal_progress'));
            if (!saved) return;
            for (const [id, val] of Object.entries(saved)) {
                const el = document.getElementById(id);
                if (el) el.checked = val;
            }
        }

        // ================= PEPTIDE PROTOCOL LOGIC ================= //
        function logPeptideEntry() {
            const entry = {
                date: document.getElementById('pep-date').value || todayStr,
                dose: document.getElementById('pep-dose').value + ' mcg',
                site: document.getElementById('pep-site').value,
                pain: document.getElementById('pep-pain').value + '/10',
                notes: document.getElementById('pep-notes').value || 'None'
            };

            let history = JSON.parse(localStorage.getItem('ctl_peptide_history')) || [];
            history.unshift(entry);
            localStorage.setItem('ctl_peptide_history', JSON.stringify(history));
            renderPeptideHistory();
            alert('Peptide administration logged successfully!');
        }

        function renderPeptideHistory() {
            const history = JSON.parse(localStorage.getItem('ctl_peptide_history')) || [];
            const tbody = document.getElementById('peptide-history-tbody');
            if (history.length === 0) {
                tbody.innerHTML = `<tr><td colspan="5" class="p-4 text-center text-gray-500">No peptide logs recorded yet.</td></tr>`;
                return;
            }
            let html = '';
            history.forEach(item => {
                html += `
                    <tr>
                        <td class="p-2.5 font-bold text-hyrox-yellow">${item.date}</td>
                        <td class="p-2.5">${item.dose}</td>
                        <td class="p-2.5">${item.site}</td>
                        <td class="p-2.5">${item.pain}</td>
                        <td class="p-2.5 text-gray-400">${item.notes}</td>
                    </tr>
                `;
            });
            tbody.innerHTML = html;
        }

        // ================= DAILY REVIEW LOGIC ================= //
        function saveDailyReview() {
            const review = {
                date: todayStr,
                wins: document.getElementById('rev-wins').value,
                battles: document.getElementById('rev-battles').value,
                gratitude: document.getElementById('rev-gratitude').value,
                mission: document.getElementById('rev-mission').value
            };
            localStorage.setItem(`ctl_review_${todayStr}`, JSON.stringify(review));
            alert('Daily reflection & review saved successfully!');
        }

        function loadDailyReview() {
            const saved = JSON.parse(localStorage.getItem(`ctl_review_${todayStr}`));
            if (!saved) return;
            if (saved.wins) document.getElementById('rev-wins').value = saved.wins;
            if (saved.battles) document.getElementById('rev-battles').value = saved.battles;
            if (saved.gratitude) document.getElementById('rev-gratitude').value = saved.gratitude;
            if (saved.mission) document.getElementById('rev-mission').value = saved.mission;
        }

        // Initialization on Load
        document.getElementById('pep-date').valueAsDate = new Date();
        loadDashboardData();
        updateLiftWeekOptions();
        renderMealBlocks();
        renderPeptideHistory();
        loadDailyReview();
    </script>
</body>
</html>
