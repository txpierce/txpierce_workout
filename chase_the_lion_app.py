<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TX_Pierce HYROX Training App</title>
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
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">

    <!-- Top Navigation / Header -->
    <header class="bg-black border-b border-gray-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center space-x-3">
                <div class="bg-hyrox-yellow text-black font-black px-3 py-1.5 text-xl tracking-wider rounded">TXP</div>
                <div>
                    <h1 class="text-lg font-bold text-white tracking-wide">TX_PIERCE HYROX TRAINING APP</h1>
                    <p id="header-subtext" class="text-xs text-gray-400">Custom Division | Full 11-Week Master Plan</p>
                </div>
            </div>
            <!-- Navigation Tabs -->
            <div class="flex items-center gap-2 flex-wrap justify-center">
                <nav class="flex flex-wrap justify-center gap-1.5 bg-gray-900 p-1 rounded-lg border border-gray-800">
                    <button onclick="switchTab('dashboard')" id="btn-dashboard" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded bg-hyrox-yellow text-black transition">Dashboard</button>
                    <button onclick="switchTab('program')" id="btn-program" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">11-Week Master</button>
                    <button onclick="switchTab('logger')" id="btn-logger" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Race Simulator</button>
                    <button onclick="switchTab('tools')" id="btn-tools" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Coach Live Timer</button>
                    <button onclick="switchTab('cards')" id="btn-cards" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Share Cards</button>
                    <button onclick="switchTab('raceprep')" id="btn-raceprep" class="tab-btn px-3 py-1.5 text-xs font-semibold rounded text-gray-300 hover:bg-gray-800 transition">Race & Post-Log</button>
                </nav>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 py-6 w-full flex-grow space-y-6">

        <!-- ================= CUSTOMIZATION CONTROL BAR ================= -->
        <div class="bg-gradient-to-r from-zinc-900 to-black border border-hyrox-yellow/40 rounded-xl p-4 shadow-xl flex flex-col lg:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <i class="fa-solid fa-sliders text-hyrox-yellow text-lg"></i>
                <div>
                    <h3 class="text-sm font-bold text-white uppercase tracking-wider">Race Customization Settings</h3>
                    <p class="text-[11px] text-gray-400">Tailor your event name, race date, and division standards instantly.</p>
                </div>
            </div>
            <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
                <div class="flex flex-col">
                    <label class="text-[10px] text-gray-400 uppercase font-semibold mb-1">Race Name</label>
                    <input type="text" id="setting-race-name" value="HYROX Houston" onchange="updateRaceSettings()" class="rounded px-2.5 py-1.5 text-xs font-bold">
                </div>
                <div class="flex flex-col">
                    <label class="text-[10px] text-gray-400 uppercase font-semibold mb-1">Race Date</label>
                    <input type="date" id="setting-race-date" value="2026-03-29" onchange="updateRaceSettings()" class="rounded px-2.5 py-1.5 text-xs font-bold">
                </div>
                <div class="flex flex-col">
                    <label class="text-[10px] text-gray-400 uppercase font-semibold mb-1">Competition Division</label>
                    <select id="setting-division" onchange="updateRaceSettings()" class="rounded px-2.5 py-1.5 text-xs font-bold bg-[#1E1E1E] text-white">
                        <option value="mens">Men's Open / Pro</option>
                        <option value="mens-double">Men's Doubles</option>
                        <option value="womens">Women's Open / Pro</option>
                        <option value="womens-double" selected>Women's Doubles</option>
                        <option value="mix-double">Mixed Doubles</option>
                        <option value="group-4">Group of 4 (Relay)</option>
                    </select>
                </div>
            </div>
        </div>

        <!-- ================= TAB 1: DASHBOARD ================= -->
        <div id="tab-dashboard" class="tab-content active space-y-6">
            <!-- Countdown Banner -->
            <div class="bg-gradient-to-r from-gray-900 via-zinc-900 to-black border border-yellow-500/30 rounded-xl p-6 shadow-xl flex flex-col md:flex-row items-center justify-between gap-6">
                <div>
                    <span class="bg-hyrox-yellow/10 text-hyrox-yellow border border-hyrox-yellow/30 text-xs px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">Target Race</span>
                    <h2 id="display-race-title" class="text-2xl font-black text-white mt-2">HYROX HOUSTON (Women's Doubles)</h2>
                    <p id="display-race-date-sub" class="text-sm text-gray-400 mt-1">March 29, 2026 | Complete 11-Week Master Periodized Program</p>
                </div>
                <div class="grid grid-cols-4 gap-3 text-center">
                    <div class="bg-black/60 border border-gray-800 px-3 py-2 rounded-lg">
                        <div id="days-left" class="text-2xl font-black text-hyrox-yellow">--</div>
                        <div class="text-[10px] text-gray-400 uppercase">Days</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 px-3 py-2 rounded-lg">
                        <div id="hours-left" class="text-2xl font-black text-white">--</div>
                        <div class="text-[10px] text-gray-400 uppercase">Hours</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 px-3 py-2 rounded-lg">
                        <div id="mins-left" class="text-2xl font-black text-white">--</div>
                        <div class="text-[10px] text-gray-400 uppercase">Mins</div>
                    </div>
                    <div class="bg-black/60 border border-gray-800 px-3 py-2 rounded-lg">
                        <div id="secs-left" class="text-2xl font-black text-white">--</div>
                        <div class="text-[10px] text-gray-400 uppercase">Secs</div>
                    </div>
                </div>
            </div>

            <!-- Quick Stats & Official Standards Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2 bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg">
                    <div class="flex justify-between items-center mb-4">
                        <h3 id="standards-heading" class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-scale-balanced text-hyrox-yellow"></i> Official Division Standards
                        </h3>
                        <span class="text-xs bg-gray-800 text-gray-300 px-2.5 py-1 rounded">Season 2026/27</span>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-black/40 text-gray-400 uppercase text-[10px]">
                                <tr>
                                    <th class="p-2.5">Station / Movement</th>
                                    <th class="p-2.5">Distance / Reps</th>
                                    <th class="p-2.5">Prescribed Load</th>
                                    <th class="p-2.5">Execution Notes</th>
                                </tr>
                            </thead>
                            <tbody id="standards-tbody" class="divide-y divide-gray-800 text-gray-300"></tbody>
                        </table>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg">
                        <h3 class="text-base font-bold text-white mb-3 flex items-center gap-2">
                            <i class="fa-solid fa-gauge-high text-hyrox-yellow"></i> RPE Reference Guide
                        </h3>
                        <div class="space-y-2 text-xs">
                            <div class="flex justify-between items-center bg-black/30 p-2 rounded">
                                <span class="font-bold text-yellow-400">RPE 3–4</span>
                                <span class="text-gray-400">Light / Warm-up</span>
                            </div>
                            <div class="flex justify-between items-center bg-black/30 p-2 rounded">
                                <span class="font-bold text-yellow-400">RPE 5–6</span>
                                <span class="text-gray-400">Moderate / Zone 2</span>
                            </div>
                            <div class="flex justify-between items-center bg-black/30 p-2 rounded">
                                <span class="font-bold text-yellow-400">RPE 7</span>
                                <span class="text-gray-400">Hard / Controlled Strength</span>
                            </div>
                            <div class="flex justify-between items-center bg-black/30 p-2 rounded">
                                <span class="font-bold text-yellow-400">RPE 8–9</span>
                                <span class="text-gray-400">Very Hard / Intervals</span>
                            </div>
                        </div>
                    </div>

                    <div class="bg-gradient-to-br from-zinc-900 to-black border border-gray-800 rounded-xl p-5 shadow-lg">
                        <h3 class="text-sm font-bold text-white mb-2 uppercase tracking-wide text-hyrox-yellow">Core Training Principles</h3>
                        <ul class="text-xs text-gray-300 space-y-2 list-disc pl-4">
                            <li><strong class="text-white">Consistency over intensity</strong> early in training blocks.</li>
                            <li><strong class="text-white">Efficiency under fatigue</strong> over maximal output.</li>
                            <li><strong class="text-white">Smooth transitions</strong> and clear partner handoffs.</li>
                            <li><strong class="text-white">Role clarity</strong>: Split reps evenly on high-fatigue stations.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 2: 11-WEEK MASTER PROGRAM ================= -->
        <div id="tab-program" class="tab-content space-y-6">
            <!-- Overall Progress Meter Banner -->
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-3">
                <div class="flex justify-between items-center">
                    <div>
                        <h2 class="text-xl font-bold text-white">11-Week Master Training Program</h2>
                        <p class="text-xs text-gray-400">Log working weights and check off sets. Data saves automatically.</p>
                    </div>
                    <div class="text-right">
                        <span id="overall-progress-text" class="text-sm font-black text-hyrox-yellow">0% Completed</span>
                        <div class="text-[10px] text-gray-400 uppercase">Race Prep Progress</div>
                    </div>
                </div>
                <div class="w-full bg-black/70 border border-gray-800 rounded-full h-3 overflow-hidden">
                    <div id="overall-progress-bar" class="bg-hyrox-yellow h-full transition-all duration-300" style="width: 0%;"></div>
                </div>
            </div>

            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-4 shadow-lg flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-3 w-full">
                    <label class="text-xs text-gray-300 font-medium whitespace-nowrap">Select Week:</label>
                    <select id="program-week-select" onchange="renderProgramWeek()" class="bg-black border border-gray-700 text-sm rounded-lg px-3 py-1.5 text-white font-semibold w-full md:w-auto">
                        <option value="1">Week 1: Base & Movement Quality</option>
                        <option value="2">Week 2: Base Progression</option>
                        <option value="3">Week 3: Base → Build Transition</option>
                        <option value="4">Week 4: Base Phase Complete</option>
                        <option value="5">Week 5: Build Phase Begins</option>
                        <option value="6">Week 6: Build Phase Continues</option>
                        <option value="7">Week 7: Density & Efficiency</option>
                        <option value="8">Week 8: Late-Race Focus</option>
                        <option value="9">Week 9: Peak & Full Sim</option>
                        <option value="10">Week 10: Sharpen Phase</option>
                        <option value="11">Week 11: Taper & Race Execution</option>
                    </select>
                </div>
            </div>

            <div id="program-container" class="space-y-4"></div>
        </div>

        <!-- ================= TAB 3: RACE SIMULATOR LOGGER ================= -->
        <div id="tab-logger" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-6">
                <div class="flex justify-between items-center">
                    <div>
                        <h2 class="text-xl font-bold text-white">HYROX Race Simulator & Workout Logger</h2>
                        <p class="text-xs text-gray-400">Set your overall goal finish time to automatically generate target splits for every run and station.</p>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="saveSimLog()" class="bg-hyrox-yellow text-black px-4 py-2 rounded-lg font-bold text-xs hover:bg-yellow-400 transition flex items-center gap-1.5">
                            <i class="fa-solid fa-floppy-disk"></i> Save Sim Log
                        </button>
                        <button onclick="clearSimLog()" class="bg-gray-800 text-gray-300 px-3 py-2 rounded-lg font-medium text-xs hover:bg-gray-700 transition">
                            Clear
                        </button>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 bg-black/40 p-4 rounded-xl border border-gray-800">
                    <div>
                        <label class="block text-xs font-medium text-gray-400 mb-1">Date</label>
                        <input type="date" id="sim-date" class="w-full rounded-lg p-2.5 text-sm">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-gray-400 mb-1">Phase / Week</label>
                        <select id="sim-week" class="w-full rounded-lg p-2.5 text-sm bg-black border border-gray-700 text-white">
                            <option>Week 1 (Base)</option><option>Week 2 (Base)</option><option>Week 3 (Base-Build)</option><option>Week 4 (Base)</option>
                            <option>Week 5 (Build)</option><option selected>Week 6 (Build)</option><option>Week 7 (Build)</option><option>Week 8 (Build)</option>
                            <option>Week 9 (Peak)</option><option>Week 10 (Sharpen)</option><option>Week 11 (Taper/Race)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-gray-400 mb-1">Athlete Name</label>
                        <input type="text" id="sim-athlete" placeholder="Athlete Name" class="w-full rounded-lg p-2.5 text-sm">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-gray-400 mb-1">Partner / Team</label>
                        <input type="text" id="sim-partner" placeholder="Partner/Team Name" class="w-full rounded-lg p-2.5 text-sm">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-hyrox-yellow mb-1 font-bold">Goal Finish Time (MM:SS)</label>
                        <div class="flex gap-2">
                            <input type="text" id="sim-goal-total" value="1:15:00" placeholder="1:15:00" class="w-full rounded-lg p-2.5 text-sm font-bold text-center text-hyrox-yellow">
                            <button onclick="autoCalculateTargets()" class="bg-hyrox-yellow text-black px-3 rounded-lg font-bold text-xs hover:bg-yellow-400 transition" title="Auto-distribute targets">
                                <i class="fa-solid fa-wand-magic-sparkles"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Simulation Overview & Vitals -->
                <div class="border-t border-gray-800 pt-4">
                    <h3 class="text-sm font-bold text-white mb-3 text-hyrox-yellow flex items-center gap-2">
                        <i class="fa-solid fa-stopwatch"></i> 1. Simulation Overview & Vitals
                    </h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-black/40 text-gray-400 uppercase text-[10px]">
                                <tr>
                                    <th class="p-2.5">Metric</th>
                                    <th class="p-2.5">Target / Goal</th>
                                    <th class="p-2.5">Actual Recorded</th>
                                    <th class="p-2.5">Notes / Context</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-800 text-gray-300">
                                <tr>
                                    <td class="p-2.5 font-medium text-white">Total Sim Time</td>
                                    <td class="p-2.5 text-hyrox-yellow font-bold" id="display-goal-total">1:15:00</td>
                                    <td class="p-2.5"><input type="text" id="sim-total-time" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td>
                                    <td class="p-2.5 text-gray-400">Overall time including runs and stations</td>
                                </tr>
                                <tr class="bg-black/20">
                                    <td class="p-2.5 font-medium text-white">Average Heart Rate</td>
                                    <td class="p-2.5 text-gray-400">Target: 165 bpm</td>
                                    <td class="p-2.5"><input type="text" id="sim-avg-hr" placeholder="-- bpm" class="w-full p-1.5 rounded text-xs"></td>
                                    <td class="p-2.5 text-gray-400">Cardiovascular load</td>
                                </tr>
                                <tr>
                                    <td class="p-2.5 font-medium text-white">Peak Heart Rate</td>
                                    <td class="p-2.5 text-gray-400">Max: 182 bpm</td>
                                    <td class="p-2.5"><input type="text" id="sim-peak-hr" placeholder="-- bpm" class="w-full p-1.5 rounded text-xs"></td>
                                    <td class="p-2.5 text-gray-400">Where did you redline?</td>
                                </tr>
                                <tr class="bg-black/20">
                                    <td class="p-2.5 font-medium text-white">Overall Session RPE</td>
                                    <td class="p-2.5 text-gray-400">Scale: 8.5 / 10</td>
                                    <td class="p-2.5"><input type="number" min="1" max="10" id="sim-rpe" placeholder="-- / 10" class="w-full p-1.5 rounded text-xs"></td>
                                    <td class="p-2.5 text-gray-400">Perceived exertion of the full effort</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Full Race Flow: Alternating Runs & Stations -->
                <div class="border-t border-gray-800 pt-4">
                    <h3 class="text-sm font-bold text-white mb-3 text-hyrox-yellow flex items-center gap-2">
                        <i class="fa-solid fa-person-running"></i> 2. Full Race Flow (Runs & Stations)
                    </h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-black/40 text-gray-400 uppercase text-[10px]">
                                <tr>
                                    <th class="p-2.5">Race Segment</th>
                                    <th class="p-2.5">Target Pace / Time & Cumulative</th>
                                    <th class="p-2.5">Actual Time / Split</th>
                                    <th class="p-2.5">Transition / Execution Quality</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-800 text-gray-300">
                                <tr><td class="p-2.5 font-medium text-white">1. Run 1 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg1">--:--</td><td class="p-2.5"><input type="text" id="seg1-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg1-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">2. SkiErg (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg2">--:--</td><td class="p-2.5"><input type="text" id="seg2-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg2-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">3. Run 2 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg3">--:--</td><td class="p-2.5"><input type="text" id="seg3-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg3-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">4. Sled Push (50m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg4">--:--</td><td class="p-2.5"><input type="text" id="seg4-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg4-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">5. Run 3 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg5">--:--</td><td class="p-2.5"><input type="text" id="seg5-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg5-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">6. Sled Pull (50m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg6">--:--</td><td class="p-2.5"><input type="text" id="seg6-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg6-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">7. Run 4 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg7">--:--</td><td class="p-2.5"><input type="text" id="seg7-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg7-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">8. Burpee Broad Jumps (80m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg8">--:--</td><td class="p-2.5"><input type="text" id="seg8-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg8-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">9. Run 5 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg9">--:--</td><td class="p-2.5"><input type="text" id="seg9-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg9-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">10. Rowing (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg10">--:--</td><td class="p-2.5"><input type="text" id="seg10-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg10-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">11. Run 6 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg11">--:--</td><td class="p-2.5"><input type="text" id="seg11-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg11-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">12. Farmer Carry (200m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg12">--:--</td><td class="p-2.5"><input type="text" id="seg12-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg12-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">13. Run 7 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg13">--:--</td><td class="p-2.5"><input type="text" id="seg13-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg13-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">14. Sandbag Lunges (100m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg14">--:--</td><td class="p-2.5"><input type="text" id="seg14-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg14-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr><td class="p-2.5 font-medium text-white">15. Run 8 (1,000m)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg15">--:--</td><td class="p-2.5"><input type="text" id="seg15-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg15-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                                <tr class="bg-black/20"><td class="p-2.5 font-medium text-hyrox-yellow">16. Wall Balls (100 reps)</td><td class="p-2.5 font-mono text-hyrox-yellow" id="target-seg16">--:--</td><td class="p-2.5"><input type="text" id="seg16-act" placeholder="--:--" class="w-full p-1.5 rounded text-xs"></td><td class="p-2.5"><select id="seg16-trans" class="w-full p-1.5 rounded text-xs"><option>Smooth</option><option>Rushed</option><option>Slow</option></select></td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 4: COACH LIVE TRACKER & INTERVAL TIMER ================= -->
        <div id="tab-tools" class="tab-content space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Left 2 Cols: Live Coach Race Tracker Panel -->
                <div class="lg:col-span-2 bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                    <div class="flex justify-between items-center border-b border-gray-800 pb-3">
                        <div>
                            <h3 class="text-base font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-stopwatch-20 text-hyrox-yellow"></i> Live Coach Race Tracker (16 Segments)
                            </h3>
                            <p class="text-xs text-gray-400">Track your athlete live in real-time. Hit "Next Segment" on every handoff to log splits automatically.</p>
                        </div>
                        <div class="text-right">
                            <span id="coach-active-badge" class="bg-hyrox-yellow/20 text-hyrox-yellow border border-hyrox-yellow/40 text-[10px] px-2.5 py-1 rounded-full font-bold uppercase">Ready to Start</span>
                        </div>
                    </div>

                    <!-- Live Status Banner -->
                    <div class="bg-black/70 border border-gray-800 p-4 rounded-xl flex flex-col sm:flex-row justify-between items-center gap-4">
                        <div>
                            <div class="text-[10px] text-gray-400 uppercase font-semibold">Current Active Segment</div>
                            <div id="coach-current-segment" class="text-lg font-black text-hyrox-yellow">Segment 1: Run 1 (1,000m)</div>
                        </div>
                        <div class="flex items-center gap-4 text-center">
                            <div>
                                <div class="text-[10px] text-gray-400 uppercase">Segment Timer</div>
                                <div id="coach-seg-timer" class="text-2xl font-black font-mono text-white">00:00</div>
                            </div>
                            <div>
                                <div class="text-[10px] text-gray-400 uppercase">Total Elapsed</div>
                                <div id="coach-total-timer" class="text-2xl font-black font-mono text-hyrox-yellow">00:00:00</div>
                            </div>
                        </div>
                    </div>

                    <!-- Live Estimated Finish Time Card -->
                    <div class="bg-gradient-to-r from-zinc-900 via-black to-zinc-900 border border-hyrox-yellow/50 p-4 rounded-xl flex justify-between items-center">
                        <div>
                            <div class="text-[11px] font-bold text-gray-400 uppercase tracking-wider">Estimated Finish Time (Staying on Pace)</div>
                            <div class="text-[10px] text-hyrox-yellow">Projected based on completed segments vs target pace</div>
                        </div>
                        <div id="coach-est-finish" class="text-3xl font-black font-mono text-hyrox-yellow">--:--:--</div>
                    </div>

                    <!-- Coach Controls -->
                    <div class="flex flex-wrap items-center gap-3">
                        <button onclick="startCoachLiveRace()" class="bg-green-600 hover:bg-green-500 text-white px-5 py-2.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5">
                            <i class="fa-solid fa-play"></i> Start Race Timer
                        </button>
                        <button onclick="recordCoachSplit()" class="bg-hyrox-yellow text-black px-5 py-2.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 shadow-lg">
                            <i class="fa-solid fa-flag-checkered"></i> Next Segment / Lap Split
                        </button>
                        <button onclick="pauseCoachLiveRace()" class="bg-yellow-600 hover:bg-yellow-500 text-white px-4 py-2.5 rounded-lg text-xs font-bold transition">Pause</button>
                        <button onclick="resetCoachLiveRace()" class="bg-red-600 hover:bg-red-500 text-white px-4 py-2.5 rounded-lg text-xs font-bold transition">Reset</button>
                    </div>

                    <!-- Live Split Log Table -->
                    <div class="overflow-x-auto max-h-64 overflow-y-auto border border-gray-800 rounded-lg">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-black/60 text-gray-400 uppercase text-[10px] sticky top-0">
                                <tr>
                                    <th class="p-2.5">#</th>
                                    <th class="p-2.5">Segment Name</th>
                                    <th class="p-2.5">Split Time</th>
                                    <th class="p-2.5">Cumulative Time</th>
                                </tr>
                            </thead>
                            <tbody id="coach-live-log-tbody" class="divide-y divide-gray-800 text-gray-300">
                                <tr><td colspan="4" class="p-4 text-center text-gray-500">Live splits will appear here as you record them during the race.</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Right Col: Pace Calculator & Quick Timer -->
                <div class="space-y-6">
                    <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                        <h3 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-calculator text-hyrox-yellow"></i> HYROX Pace Calculator
                        </h3>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-[10px] font-medium text-gray-400 mb-1">Target 1km Run Pace</label>
                                <input type="text" id="calc-pace" value="5:00" class="w-full rounded-lg p-2 text-xs font-bold text-center">
                            </div>
                            <div>
                                <label class="block text-[10px] font-medium text-gray-400 mb-1">Avg Station Time (Min)</label>
                                <input type="number" step="0.5" id="calc-station-time" value="4.5" class="w-full rounded-lg p-2 text-xs font-bold text-center">
                            </div>
                        </div>
                        <button onclick="calculatePace()" class="w-full bg-hyrox-yellow text-black py-2 rounded-lg font-bold text-xs hover:bg-yellow-400 transition">
                            Calculate Finish Time
                        </button>
                        <div class="bg-black/50 border border-gray-800 p-3 rounded-xl text-center">
                            <div class="text-[10px] text-gray-400">Estimated Total Finish Time</div>
                            <div id="est-time" class="text-xl font-black text-hyrox-yellow">--:--:--</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 5: SHARE & EXPORT CARDS ================= -->
        <div id="tab-cards" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-6">
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                    <div>
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-image text-hyrox-yellow"></i> Shareable Workout & Race Graphics
                        </h2>
                        <p class="text-xs text-gray-400">Select week and day, then generate clean graphic cards to save or share.</p>
                    </div>
                    
                    <div class="flex flex-wrap items-center gap-2">
                        <select id="card-day-select" onchange="generateShareCard('daily')" class="bg-black border border-gray-700 text-xs rounded-lg px-2.5 py-2 text-white font-semibold">
                            <option value="0">Day 1</option><option value="1">Day 2</option><option value="2">Day 3</option><option value="3">Day 4</option>
                            <option value="4">Day 5</option><option value="5">Day 6</option><option value="6">Day 7</option>
                        </select>
                        <button onclick="generateShareCard('daily')" class="bg-hyrox-yellow text-black px-3.5 py-2 rounded-lg font-bold text-xs hover:bg-yellow-400 transition">
                            <i class="fa-solid fa-calendar-day mr-1"></i> Daily Card
                        </button>
                        <button onclick="generateShareCard('weekly')" class="bg-zinc-800 text-white px-3.5 py-2 rounded-lg font-bold text-xs hover:bg-zinc-700 transition border border-gray-700">
                            Weekly
                        </button>
                        <button onclick="generateShareCard('sim')" class="bg-zinc-800 text-white px-3.5 py-2 rounded-lg font-bold text-xs hover:bg-zinc-700 transition border border-gray-700">
                            Sim Summary
                        </button>
                    </div>
                </div>

                <div class="flex justify-center p-4 bg-black/60 rounded-xl border border-gray-800">
                    <div id="shareable-graphic" class="w-full max-w-md bg-gradient-to-b from-zinc-900 via-black to-zinc-950 border-2 border-hyrox-yellow/60 rounded-2xl p-6 shadow-2xl text-white relative overflow-hidden space-y-4">
                        <div class="flex justify-between items-center border-b border-gray-800 pb-3">
                            <div class="flex items-center space-x-2">
                                <div class="bg-hyrox-yellow text-black font-black px-2.5 py-1 text-sm tracking-wider rounded">TXP</div>
                                <span id="card-race-tag" class="text-xs font-bold text-gray-300 uppercase">HYROX HOUSTON</span>
                            </div>
                            <span id="card-date-tag" class="text-[10px] text-hyrox-yellow font-mono font-semibold">--/--/2026</span>
                        </div>

                        <div class="space-y-3 py-2">
                            <div class="text-center space-y-1">
                                <div id="card-title-type" class="text-xs font-bold text-hyrox-yellow uppercase tracking-widest">Daily Workout Graphic</div>
                                <h3 id="card-main-title" class="text-lg font-black tracking-wide">Week 1 Workout & Run</h3>
                            </div>

                            <div class="bg-zinc-900/80 border border-gray-800 rounded-xl p-3.5 space-y-2 text-xs">
                                <div class="flex justify-between text-gray-400"><span>Athlete:</span><span id="card-athlete-name" class="font-bold text-white">Athlete</span></div>
                                <div class="flex justify-between text-gray-400"><span>Division:</span><span id="card-division-name" class="font-bold text-white">Women's Doubles</span></div>
                                <div class="flex justify-between text-gray-400"><span>Phase / Week:</span><span id="card-week-val" class="font-bold text-hyrox-yellow">Week 1 Master Plan</span></div>
                            </div>

                            <div id="card-metrics-box" class="bg-black/60 border border-gray-800 rounded-xl p-3.5 space-y-2 text-xs">
                                <div class="text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-1">Scheduled Exercises & Runs</div>
                                <div id="card-workout-details" class="space-y-1 text-gray-300 text-[11px]"></div>
                            </div>
                        </div>

                        <div class="pt-2 border-t border-gray-800/80 flex justify-between items-center text-[10px] text-gray-500 font-mono">
                            <span>TRAIN. SIMULATE. CONQUER.</span>
                            <span class="text-hyrox-yellow">TX_PIERCE TRACKER</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= TAB 6: RACE PREP & POST-RACE JOURNAL ================= -->
        <div id="tab-raceprep" class="tab-content space-y-6">
            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                <h3 class="text-base font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-suitcase text-hyrox-yellow"></i> Race-Week Packing Checklist
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                    <div class="bg-black/40 p-4 rounded-xl border border-gray-800 space-y-2">
                        <h4 class="font-bold text-hyrox-yellow text-sm">Required Documents</h4>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Race registration confirmation</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Photo ID / Passport</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Athlete wristband / packet</label>
                    </div>
                    <div class="bg-black/40 p-4 rounded-xl border border-gray-800 space-y-2">
                        <h4 class="font-bold text-hyrox-yellow text-sm">Competition Gear</h4>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Race shoes (broken in) + backup</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Performance socks (2 pairs)</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Watch (fully charged)</label>
                    </div>
                    <div class="bg-black/40 p-4 rounded-xl border border-gray-800 space-y-2">
                        <h4 class="font-bold text-hyrox-yellow text-sm">Warm-up & Nutrition</h4>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Light hoodie & sweatpants</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Mini resistance bands</label>
                        <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black"> Pre-race meal & electrolytes</label>
                    </div>
                </div>
            </div>

            <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-5 shadow-lg space-y-4">
                <div class="flex justify-between items-center">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-medal text-hyrox-yellow"></i> Post-Race Analysis Journal
                    </h3>
                    <button onclick="savePostRaceLog()" class="bg-hyrox-yellow text-black px-4 py-2 rounded-lg font-bold text-xs hover:bg-yellow-400 transition">Save Journal</button>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs">
                    <div><label class="block text-gray-400 mb-1">Official Finish Time</label><input type="text" id="post-time" placeholder="HH:MM:SS" class="w-full rounded-lg p-2"></div>
                    <div><label class="block text-gray-400 mb-1">Goal Time</label><input type="text" id="post-goal" placeholder="HH:MM:SS" class="w-full rounded-lg p-2"></div>
                    <div><label class="block text-gray-400 mb-1">Placement</label><input type="text" id="post-place" placeholder="e.g. 15th / 120" class="w-full rounded-lg p-2"></div>
                    <div><label class="block text-gray-400 mb-1">Goal Achieved?</label><select id="post-achieved" class="w-full rounded-lg p-2"><option>Yes</option><option>No</option></select></div>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-400 mb-1">Post-Race Reflection & Execution Notes</label>
                    <textarea id="post-reflection" rows="3" placeholder="How did pacing feel? Handoffs? What to change next time?" class="w-full rounded-lg p-2.5 text-sm"></textarea>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-black border-t border-gray-800 py-4 text-center text-xs text-gray-500">
        <p>TX_Pierce HYROX Training App | Complete 11-Week Periodized Master Plan</p>
    </footer>

    <!-- JavaScript App Logic -->
    <script>
        const divisionStandards = {
            'mens': {
                name: "Men's Open / Pro Standards",
                push: "152 kg (~335 lb)", pull: "103 kg (~227 lb)", fc: "2 x 24 kg (~53 lb)", lunge: "20 kg (~45 lb)", wb: "6 kg (~14 lb) @ 3.00m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Damper 6", n: "Feet remain on platform."},
                    {s: "2. Sled Push", d: "50 m", l: "152 kg (~335 lb)", n: "Total load incl. sled."},
                    {s: "3. Sled Pull", d: "50 m", l: "103 kg (~227 lb)", n: "Must remain in racer's box."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Chest touches ground."},
                    {s: "5. Rowing", d: "1,000 m", l: "Damper 6", n: "Feet strapped in."},
                    {s: "6. Farmer Carry", d: "200 m", l: "2 x 24 kg (~53 lb)", n: "Kettlebells at sides."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "20 kg (~45 lb)", n: "Trailing knee touches ground."},
                    {s: "8. Wall Balls", d: "100 reps", l: "6 kg @ 3.00m", n: "Hip crease below knee."}
                ]
            },
            'mens-double': {
                name: "Men's Doubles Standards",
                push: "152 kg (~335 lb)", pull: "103 kg (~227 lb)", fc: "2 x 24 kg (~53 lb)", lunge: "20 kg (~45 lb)", wb: "6 kg (~14 lb) @ 3.00m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "2. Sled Push", d: "50 m", l: "152 kg (~335 lb)", n: "Shared workload."},
                    {s: "3. Sled Pull", d: "50 m", l: "103 kg (~227 lb)", n: "Shared workload."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Alternate lengths."},
                    {s: "5. Rowing", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "6. Farmer Carry", d: "200 m", l: "2 x 24 kg (~53 lb)", n: "Carry simultaneously or relay."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "20 kg (~45 lb)", n: "Share distance."},
                    {s: "8. Wall Balls", d: "100 reps", l: "6 kg @ 3.00m", n: "Split total reps."}
                ]
            },
            'womens': {
                name: "Women's Open / Pro Standards",
                push: "102 kg (~225 lb)", pull: "78 kg (~172 lb)", fc: "2 x 16 kg (~35 lb)", lunge: "10 kg (~22 lb)", wb: "4 kg (~9 lb) @ 2.70m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Damper 6", n: "Feet remain on platform."},
                    {s: "2. Sled Push", d: "50 m", l: "102 kg (~225 lb)", n: "Total load incl. sled."},
                    {s: "3. Sled Pull", d: "50 m", l: "78 kg (~172 lb)", n: "Must remain in racer's box."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Chest touches ground."},
                    {s: "5. Rowing", d: "1,000 m", l: "Damper 6", n: "Feet strapped in."},
                    {s: "6. Farmer Carry", d: "200 m", l: "2 x 16 kg (~35 lb)", n: "Kettlebells at sides."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "10 kg (~22 lb)", n: "Trailing knee touches ground."},
                    {s: "8. Wall Balls", d: "100 reps", l: "4 kg @ 2.70m", n: "Hip crease below knee."}
                ]
            },
            'womens-double': {
                name: "Women's Doubles Standards",
                push: "102 kg (~225 lb)", pull: "78 kg (~172 lb)", fc: "2 x 16 kg (~35 lb)", lunge: "10 kg (~22 lb)", wb: "4 kg (~9 lb) @ 2.70m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "2. Sled Push", d: "50 m", l: "102 kg (~225 lb)", n: "Shared workload."},
                    {s: "3. Sled Pull", d: "50 m", l: "78 kg (~172 lb)", n: "Shared workload."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Alternate lengths."},
                    {s: "5. Rowing", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "6. Farmer Carry", d: "200 m", l: "2 x 16 kg (~35 lb)", n: "Carry simultaneously or relay."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "10 kg (~22 lb)", n: "Share distance."},
                    {s: "8. Wall Balls", d: "100 reps", l: "4 kg @ 2.70m", n: "Split total reps."}
                ]
            },
            'mix-double': {
                name: "Mixed Doubles Standards",
                push: "152 kg (~335 lb)", pull: "103 kg (~227 lb)", fc: "2 x 20 kg (~44 lb)", lunge: "15 kg (~33 lb)", wb: "6 kg (~14 lb) @ 3.00m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "2. Sled Push", d: "50 m", l: "152 kg (~335 lb)", n: "Shared workload."},
                    {s: "3. Sled Pull", d: "50 m", l: "103 kg (~227 lb)", n: "Shared workload."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Alternate lengths."},
                    {s: "5. Rowing", d: "1,000 m", l: "Damper 6 (Split)", n: "Partner relay split."},
                    {s: "6. Farmer Carry", d: "200 m", l: "2 x 20 kg (~44 lb)", n: "Shared carry weights."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "15 kg (~33 lb)", n: "Shared distance."},
                    {s: "8. Wall Balls", d: "100 reps", l: "6 kg @ 3.00m", n: "Split total reps."}
                ]
            },
            'group-4': {
                name: "Group of 4 / Relay Standards",
                push: "152 kg (~335 lb)", pull: "103 kg (~227 lb)", fc: "2 x 24 kg (~53 lb)", lunge: "20 kg (~45 lb)", wb: "6 kg (~14 lb) @ 3.00m",
                tableRows: [
                    {s: "1. SkiErg", d: "1,000 m", l: "Relay Split", n: "4 members share runs & stations."},
                    {s: "2. Sled Push", d: "50 m", l: "Team Load", n: "Relay execution."},
                    {s: "3. Sled Pull", d: "50 m", l: "Team Load", n: "Relay execution."},
                    {s: "4. Burpee Broad Jump", d: "80 m", l: "Bodyweight", n: "Team rotation."},
                    {s: "5. Rowing", d: "1,000 m", l: "Relay Split", n: "Team rotation."},
                    {s: "6. Farmer Carry", d: "200 m", l: "Team Weight", n: "Team rotation."},
                    {s: "7. Sandbag Lunges", d: "100 m", l: "Team Weight", n: "Team rotation."},
                    {s: "8. Wall Balls", d: "100 reps", l: "Team Standard", n: "Team rotation."}
                ]
            }
        };

        const segmentNamesList = [
            "1. Run 1 (1,000m)", "2. SkiErg (1,000m)", "3. Run 2 (1,000m)", "4. Sled Push (50m)",
            "5. Run 3 (1,000m)", "6. Sled Pull (50m)", "7. Run 4 (1,000m)", "8. Burpee Broad Jumps (80m)",
            "9. Run 5 (1,000m)", "10. Rowing (1,000m)", "11. Run 6 (1,000m)", "12. Farmer Carry (200m)",
            "13. Run 7 (1,000m)", "14. Sandbag Lunges (100m)", "15. Run 8 (1,000m)", "16. Wall Balls (100 reps)"
        ];

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

        function updateRaceSettings() {
            const raceName = document.getElementById('setting-race-name').value;
            const raceDateVal = document.getElementById('setting-race-date').value;
            const divisionKey = document.getElementById('setting-division').value;
            const divObj = divisionStandards[divisionKey];

            document.getElementById('display-race-title').innerText = `${raceName.toUpperCase()} (${divObj.name.replace(' Standards', '')})`;
            const dateFormatted = raceDateVal ? new Date(raceDateVal + 'T00:00:00').toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }) : 'TBD';
            document.getElementById('display-race-date-sub').innerText = `${dateFormatted} | Complete 11-Week Master Periodized Program`;
            document.getElementById('header-subtext').innerText = `${divObj.name.replace(' Standards', '')} | ${raceName}`;

            document.getElementById('standards-heading').innerHTML = `<i class="fa-solid fa-scale-balanced text-hyrox-yellow"></i> Official ${divObj.name}`;
            
            let tbodyHtml = '';
            divObj.tableRows.forEach((row, idx) => {
                tbodyHtml += `
                    <tr class="${idx % 2 === 1 ? 'bg-black/20' : ''}">
                        <td class="p-2.5 font-medium text-white">${row.s}</td>
                        <td class="p-2.5">${row.d}</td>
                        <td class="p-2.5">${row.l}</td>
                        <td class="p-2.5 text-gray-400">${row.n}</td>
                    </tr>
                `;
            });
            document.getElementById('standards-tbody').innerHTML = tbodyHtml;
            localStorage.setItem('hyrox_custom_settings', JSON.stringify({ raceName, raceDateVal, divisionKey }));
        }

        function updateCountdown() {
            const raceDateVal = document.getElementById('setting-race-date').value || '2026-03-29';
            const raceDate = new Date(raceDateVal + 'T08:00:00').getTime();
            const now = new Date().getTime();
            const diff = raceDate - now;

            if (diff > 0) {
                document.getElementById('days-left').innerText = Math.floor(diff / (1000 * 60 * 60 * 24));
                document.getElementById('hours-left').innerText = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                document.getElementById('mins-left').innerText = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                document.getElementById('secs-left').innerText = Math.floor((diff % (1000 * 60)) / 1000);
            }
        }
        setInterval(updateCountdown, 1000);

        const programData = {
            1: {
                title: "WEEK 1 — BASE & MOVEMENT QUALITY",
                focus: "Aerobic capacity, foundational strength, movement quality.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Back Squat", sets: 4, reps: "6", load: "Moderate"}, {name: "Reverse Lunge", sets: 3, reps: "10/leg", load: "DBs Moderate"}, {name: "Sled Push", sets: 6, reps: "10 m", load: "Light-Mod"}, {name: "Bike Erg Engine", sets: 6, reps: "1:00 hard / 1:00 easy", load: "Zone 3-4"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "40 min", load: "Conversational Pace"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Bench Press", sets: 4, reps: "6", load: "Moderate"}, {name: "Bent-Over Row", sets: 4, reps: "8", load: "Moderate"}, {name: "SkiErg Conditioning", sets: 4, reps: "500 m", load: "Easy-Mod"}]},
                    { day: "Day 4 - Run Intervals", exercises: [{name: "Run Intervals", sets: 6, reps: "400 m (90s rest)", load: "Controlled Hard"}]},
                    { day: "Day 5 - Hybrid Conditioning", exercises: [{name: "Row + Farmer Carry + Wall Balls", sets: 3, reps: "500m Row / 50m Carry / 15 WB", load: "Controlled Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Partial Simulation", sets: 1, reps: "500m Ski / 4x10m Push / 4x10m Pull", load: "Technique Priority"}]},
                    { day: "Day 7 - Recovery", exercises: [{name: "Active Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            2: {
                title: "WEEK 2 — BASE PROGRESSION",
                focus: "Progressive volume increase, building aerobic base.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Back Squat", sets: 4, reps: "6", load: "+5-10 lb"}, {name: "Reverse Lunge", sets: 3, reps: "10/leg", load: "Slightly heavier"}, {name: "Sled Push", sets: 6, reps: "12.5 m", load: "Moderate"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "45 min", load: "Conversational"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Bench Press", sets: 4, reps: "6", load: "+5 lb"}, {name: "Bent-Over Row", sets: 4, reps: "8", load: "Heavier"}]},
                    { day: "Day 4 - Run Intervals", exercises: [{name: "Run Intervals", sets: 5, reps: "600 m (2:00 rest)", load: "Controlled Hard"}]},
                    { day: "Day 5 - Hybrid Conditioning", exercises: [{name: "Row + Farmer Carry + Wall Balls", sets: 3, reps: "750m Row / 75m Carry / 20 WB", load: "Controlled Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Simulation", sets: 1, reps: "750m Ski / 4x12.5m Push & Pull", load: "Race Rhythm"}]},
                    { day: "Day 7 - Recovery", exercises: [{name: "Rest & Mobility", sets: 1, reps: "Full Recovery", load: "Rest"}]}
                ]
            },
            3: {
                title: "WEEK 3 — BASE → BUILD TRANSITION",
                focus: "Mastering early race stations and running cadence.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Back Squat", sets: 4, reps: "6", load: "+5–10 lb"}, {name: "Sled Push", sets: 6, reps: "12.5 m", load: "Moderate"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "45-50 min", load: "Conversational"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Bench Press", sets: 4, reps: "6", load: "+5 lb"}, {name: "SkiErg", sets: 4, reps: "750 m", load: "Moderate"}]},
                    { day: "Day 4 - Run Intervals", exercises: [{name: "Run Intervals", sets: 4, reps: "800 m (2:30 rest)", load: "Controlled Hard"}]},
                    { day: "Day 5 - Hybrid Circuit", exercises: [{name: "Row + Farmer Carry + Wall Balls", sets: 4, reps: "750m Row / 100m Carry / 20 WB", load: "Race Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Simulation", sets: 1, reps: "1000m Ski / 2x12.5m Push & Pull / 60m BBJ", load: "Race Intensity"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            4: {
                title: "WEEK 4 — BASE PHASE COMPLETE",
                focus: "Threshold running and heavy sled volume capstone.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Back Squat", sets: 4, reps: "6", load: "+5 lb"}, {name: "Sled Push", sets: 6, reps: "12.5 m", load: "Heavy"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "45 min", load: "Conversational"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Bench Press", sets: 4, reps: "6", load: "+5 lb"}, {name: "SkiErg", sets: 5, reps: "500 m", load: "Moderate"}]},
                    { day: "Day 4 - Threshold Run", exercises: [{name: "Threshold Run", sets: 3, reps: "1 mile (3:00 rest)", load: "Threshold Pace"}]},
                    { day: "Day 5 - Hybrid Conditioning", exercises: [{name: "Circuit", sets: 4, reps: "750m Row / 100m Carry / 25 WB", load: "Controlled Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Simulation", sets: 1, reps: "1km Ski / 4x12.5m Push & Pull / 80m BBJ", load: "Base Phase Capstone"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            5: {
                title: "WEEK 5 — BUILD PHASE BEGINS",
                focus: "Density, heavier loads, fatigue tolerance.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Front Squat", sets: 5, reps: "5", load: "Moderate–Heavy"}, {name: "Sled Push", sets: 4, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "45-50 min", load: "Steady"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Push Press", sets: 4, reps: "5", load: "Moderate"}, {name: "SkiErg", sets: 5, reps: "400 m", load: "Moderate"}]},
                    { day: "Day 4 - Threshold Run", exercises: [{name: "Threshold Run", sets: 3, reps: "1 mile (3:00 rest)", load: "Threshold Pace"}]},
                    { day: "Day 5 - Hybrid Conditioning", exercises: [{name: "Circuit", sets: 4, reps: "750m Row / 100m Carry / 25 WB", load: "Moderate Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Broken Simulation", sets: 1, reps: "1km Run / 1km Ski / 4x12.5m Push", load: "Broken Race Format"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            6: {
                title: "WEEK 6 — BUILD PHASE CONTINUES",
                focus: "Mid-race stamina and burpee efficiency under fatigue.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Front Squat", sets: 5, reps: "5", load: "+5 lb"}, {name: "Sled Push", sets: 5, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "50 min", load: "Steady"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Push Press", sets: 4, reps: "5", load: "Heavier"}, {name: "SkiErg", sets: 6, reps: "400 m", load: "Moderate"}]},
                    { day: "Day 4 - Threshold Run", exercises: [{name: "Threshold Run", sets: 4, reps: "1 mile (3:00 rest)", load: "Threshold Pace"}]},
                    { day: "Day 5 - Hybrid Conditioning", exercises: [{name: "Circuit", sets: 4, reps: "1000m Row / 100m Carry / 25 WB", load: "Controlled Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Broken Simulation", sets: 1, reps: "1km Run / 1km Ski / 80m BBJ", load: "Broken Race Format"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            7: {
                title: "WEEK 7 — DENSITY & EFFICIENCY",
                focus: "Farmer carry grip endurance and heavy sled resilience.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Front Squat", sets: 4, reps: "5", load: "Same as Wk 6"}, {name: "Sled Push", sets: 6, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "50 min", load: "Relaxed Steady"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Push Press", sets: 4, reps: "5", load: "Same as Wk 6"}, {name: "SkiErg", sets: 6, reps: "400 m", load: "Moderate"}]},
                    { day: "Day 4 - Run Intervals", exercises: [{name: "Run Intervals", sets: 5, reps: "1 km", load: "Race Pace"}]},
                    { day: "Day 5 - Hybrid Sharpening", exercises: [{name: "Circuit", sets: 3, reps: "1000m Row / 200m Carry / 25 WB", load: "Race Pace"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Race Rhythm Practice", sets: 1, reps: "400m repeats + station practice", load: "Race Pace"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            8: {
                title: "WEEK 8 — LATE-RACE FOCUS",
                focus: "Lunges and wall balls under severe cumulative fatigue.",
                days: [
                    { day: "Day 1 - Lower Body Strength + Engine", exercises: [{name: "Front Squat", sets: 4, reps: "4", load: "Heavier"}, {name: "Sled Push", sets: 6, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Aerobic Run", exercises: [{name: "Zone 2 Run", sets: 1, reps: "45-50 min", load: "Relaxed"}]},
                    { day: "Day 3 - Upper Body Strength + Conditioning", exercises: [{name: "Push Press", sets: 4, reps: "4", load: "Heavier"}, {name: "SkiErg", sets: 5, reps: "500 m", load: "Moderate"}]},
                    { day: "Day 4 - Run Intervals", exercises: [{name: "Run Intervals", sets: 5, reps: "1 km", load: "Race Pace"}]},
                    { day: "Day 5 - Hybrid Primer", exercises: [{name: "Circuit", sets: 4, reps: "1000m Row / 200m Carry / 30 WB", load: "Late-Race Focus"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Late-Race Simulation", sets: 1, reps: "BBJ, Row, Lunges, Wall Balls", load: "Race Simulation"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Recovery", sets: 1, reps: "Light walking & mobility", load: "Rest"}]}
                ]
            },
            9: {
                title: "WEEK 9 — PEAK & FULL SIMULATION",
                focus: "Full dress rehearsal simulation under exact race conditions.",
                days: [
                    { day: "Day 1 - Reduced Strength", exercises: [{name: "Front Squat", sets: 3, reps: "3", load: "Race-prep load"}, {name: "Sled Push", sets: 5, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Easy Run", exercises: [{name: "Easy Jog", sets: 1, reps: "30 min", load: "Easy"}]},
                    { day: "Day 3 - Upper Strength & Full Simulation", exercises: [{name: "Push Press", sets: 3, reps: "4", load: "Moderate"}, {name: "Full Race Simulation", sets: 1, reps: "All 8 Stations + 8 Runs", load: "Race Intensity"}]},
                    { day: "Day 4 - Short Intervals", exercises: [{name: "Short Intervals", sets: 3, reps: "800 m", load: "Fast"}]},
                    { day: "Day 5 - Hybrid Primer", exercises: [{name: "Primer Circuit", sets: 1, reps: "Short activation", load: "Easy"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Pacing Review & Mobility", sets: 1, reps: "Drills & transition practice", load: "Moderate"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Mobility & Walking", sets: 1, reps: "Light stretching", load: "Rest"}]}
                ]
            },
            10: {
                title: "WEEK 10 — SHARPEN PHASE",
                focus: "Sharpening speed, nervous system activation, reducing fatigue.",
                days: [
                    { day: "Day 1 - Light Strength + Engine", exercises: [{name: "Front Squat", sets: 3, reps: "2", load: "~85-88%"}, {name: "Sled Push", sets: 4, reps: "12.5 m", load: "Race Load"}]},
                    { day: "Day 2 - Aerobic Run (Short)", exercises: [{name: "Easy Jog", sets: 1, reps: "30 min", load: "Zone 2"}]},
                    { day: "Day 3 - Upper Body & Core", exercises: [{name: "Push Press", sets: 3, reps: "3", load: "Moderate"}, {name: "Core Work", sets: 3, reps: "10 reps", load: "Bodyweight"}]},
                    { day: "Day 4 - Threshold Run", exercises: [{name: "Threshold Run", sets: 2, reps: "800 m", load: "Controlled"}]},
                    { day: "Day 5 - Active Recovery", exercises: [{name: "Mobility & Stretching", sets: 1, reps: "20 min", load: "Easy"}]},
                    { day: "Day 6 - HYROX Practice", exercises: [{name: "Sharp Partial Simulation", sets: 1, reps: "Key stations speed work", load: "Race Pace"}]},
                    { day: "Day 7 - Off / Recovery", exercises: [{name: "Rest", sets: 1, reps: "Rest", load: "Rest"}]}
                ]
            },
            11: {
                title: "WEEK 11 — TAPER & RACE EXECUTION",
                focus: "Shedding fatigue, ensuring complete freshness for race day.",
                days: [
                    { day: "Day 1 - Shakeout", exercises: [{name: "Easy Jog + Mobility", sets: 1, reps: "20 min", load: "Easy"}]},
                    { day: "Day 2 - Rest", exercises: [{name: "Complete Rest", sets: 1, reps: "0", load: "Rest"}]},
                    { day: "Day 3 - Activation", exercises: [{name: "Easy Jog + SkiErg Pulls", sets: 1, reps: "15 min", load: "Easy"}]},
                    { day: "Day 4 - Rest", exercises: [{name: "Complete Rest", sets: 1, reps: "0", load: "Rest"}]},
                    { day: "Day 5 - Rest", exercises: [{name: "Complete Rest", sets: 1, reps: "0", load: "Rest"}]},
                    { day: "Day 6 - Pre-Race Activation", exercises: [{name: "Shakeout Run & Dynamic Stretches", sets: 1, reps: "10 min", load: "Easy"}]},
                    { day: "Day 7 - RACE DAY", exercises: [{name: "HYROX RACE DAY EXECUTION", sets: 1, reps: "Full Division Execution", load: "MAX"}]}
                ]
            }
        };

        function renderProgramWeek() {
            const weekNum = document.getElementById('program-week-select').value;
            const data = programData[weekNum];
            const container = document.getElementById('program-container');

            let html = `
                <div class="bg-[#1E1E1E] border border-gray-800 rounded-xl p-4 sm:p-5 shadow-lg space-y-4">
                    <div class="border-b border-gray-800 pb-3">
                        <h3 class="text-base sm:text-lg font-black text-hyrox-yellow">${data.title}</h3>
                        <p class="text-xs text-gray-400 mt-1"><strong class="text-white">Primary Focus:</strong> ${data.focus}</p>
                    </div>
                    <div class="space-y-4">
            `;

            data.days.forEach((dayObj, dayIdx) => {
                html += `
                    <div class="bg-black/40 border border-gray-800 p-3.5 sm:p-4 rounded-xl space-y-3">
                        <div class="font-bold text-xs text-hyrox-yellow uppercase tracking-wide">${dayObj.day}</div>
                        <div class="space-y-2.5">
                `;

                dayObj.exercises.forEach((ex, exIdx) => {
                    let setsHtml = '';
                    for(let s = 1; s <= (ex.sets || 1); s++) {
                        const checkboxId = `chk_w${weekNum}_d${dayIdx}_e${exIdx}_s${s}`;
                        setsHtml += `
                            <label class="cursor-pointer inline-flex items-center">
                                <input type="checkbox" class="set-checkbox hidden" id="${checkboxId}" onchange="saveProgramProgress()">
                                <span class="w-6 h-6 rounded border border-gray-700 bg-black text-[10px] font-bold flex items-center justify-center text-gray-300 hover:border-hyrox-yellow transition">${s}</span>
                            </label>
                        `;
                    }

                    const loadInputId = `load_w${weekNum}_d${dayIdx}_e${exIdx}`;
                    html += `
                        <div class="bg-zinc-900/80 border border-gray-800/90 p-3 rounded-lg flex flex-col gap-3">
                            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-1">
                                <div>
                                    <div class="text-xs font-bold text-white">${ex.name}</div>
                                    <div class="text-[11px] text-gray-400">Target: ${ex.reps} | Prescribed: ${ex.load}</div>
                                </div>
                                <div class="w-full sm:w-36 mt-1 sm:mt-0">
                                    <input type="text" id="${loadInputId}" oninput="saveProgramProgress()" placeholder="Actual Load..." class="w-full text-xs p-1.5 rounded bg-black border border-gray-700 font-semibold text-center">
                                </div>
                            </div>
                            <div class="flex items-center justify-between pt-2 border-t border-gray-800/60">
                                <span class="text-[10px] text-gray-400 uppercase font-bold">Check Sets:</span>
                                <div class="flex items-center gap-1.5 bg-black/50 px-2 py-1 rounded-lg border border-gray-800 flex-wrap justify-end">
                                    ${setsHtml}
                                </div>
                            </div>
                        </div>
                    `;
                });
                html += `</div></div>`;
            });

            html += `</div></div>`;
            container.innerHTML = html;
            loadProgramProgress();
            updateOverallProgress();
        }

        function saveProgramProgress() {
            const progressData = { checkboxes: {}, loads: {} };
            document.querySelectorAll('.set-checkbox').forEach(chk => { progressData.checkboxes[chk.id] = chk.checked; });
            document.querySelectorAll('input[id^="load_w"]').forEach(input => { progressData.loads[input.id] = input.value; });
            localStorage.setItem('hyrox_program_progress', JSON.stringify(progressData));
            updateOverallProgress();
        }

        function loadProgramProgress() {
            const saved = JSON.parse(localStorage.getItem('hyrox_program_progress'));
            if (!saved) return;
            if (saved.checkboxes) {
                for (const [id, isChecked] of Object.entries(saved.checkboxes)) {
                    const el = document.getElementById(id);
                    if (el) el.checked = isChecked;
                }
            }
            if (saved.loads) {
                for (const [id, val] of Object.entries(saved.loads)) {
                    const el = document.getElementById(id);
                    if (el) el.value = val;
                }
            }
        }

        function updateOverallProgress() {
            const saved = JSON.parse(localStorage.getItem('hyrox_program_progress'));
            let totalCheckboxes = 0, checkedCount = 0;
            for (let w = 1; w <= 11; w++) {
                programData[w].days.forEach((dayObj, dIdx) => {
                    dayObj.exercises.forEach((ex, eIdx) => {
                        const numSets = ex.sets || 1;
                        for (let s = 1; s <= numSets; s++) {
                            totalCheckboxes++;
                            const chkId = `chk_w${w}_d${dIdx}_e${eIdx}_s${s}`;
                            if (saved && saved.checkboxes && saved.checkboxes[chkId]) checkedCount++;
                        }
                    });
                });
            }
            const percent = totalCheckboxes > 0 ? Math.round((checkedCount / totalCheckboxes) * 100) : 0;
            document.getElementById('overall-progress-text').innerText = `${percent}% Completed (${checkedCount}/${totalCheckboxes} sets)`;
            document.getElementById('overall-progress-bar').style.width = `${percent}%`;
        }

        function autoCalculateTargets() {
            const goalInput = document.getElementById('sim-goal-total').value;
            let totalSeconds = 75 * 60;
            if (goalInput.includes(':')) {
                const parts = goalInput.split(':');
                if (parts.length === 3) totalSeconds = (parseInt(parts[0]) * 3600) + (parseInt(parts[1]) * 60) + parseInt(parts[2]);
                else if (parts.length === 2) totalSeconds = (parseInt(parts[0]) * 60) + parseInt(parts[1]);
            } else {
                totalSeconds = parseFloat(goalInput) * 60;
            }

            const totalRunSec = totalSeconds * 0.55;
            const singleRunSec = totalRunSec / 8;
            const singleStationSec = (totalSeconds * 0.45) / 8;

            document.getElementById('display-goal-total').innerText = goalInput;

            let cumulativeSec = 0;
            for (let i = 1; i <= 16; i++) {
                const targetEl = document.getElementById(`target-seg${i}`);
                if (targetEl) {
                    let segTimeSec = (i % 2 !== 0) ? singleRunSec : singleStationSec;
                    cumulativeSec += segTimeSec;

                    const sMin = Math.floor(segTimeSec / 60);
                    const sSec = Math.round(segTimeSec % 60);
                    const formattedSeg = `${sMin}:${sSec < 10 ? '0' : ''}${sSec}`;

                    const cMin = Math.floor(cumulativeSec / 60);
                    const cSec = Math.round(cumulativeSec % 60);
                    const formattedCum = `${cMin}:${cSec < 10 ? '0' : ''}${cSec}`;

                    targetEl.innerText = `${formattedSeg} (Cum: ${formattedCum})`;
                }
            }
        }

        // ================= COACH LIVE TRACKER TIMER LOGIC ================= //
        let coachTimerInterval = null;
        let totalElapsedSec = 0;
        let segElapsedSec = 0;
        let currentSegIndex = 0; // 0 to 15
        let coachSplitsLog = [];

        function getGoalTotalSeconds() {
            const goalInput = document.getElementById('sim-goal-total').value || "1:15:00";
            let totalSeconds = 75 * 60;
            if (goalInput.includes(':')) {
                const parts = goalInput.split(':');
                if (parts.length === 3) totalSeconds = (parseInt(parts[0]) * 3600) + (parseInt(parts[1]) * 60) + parseInt(parts[2]);
                else if (parts.length === 2) totalSeconds = (parseInt(parts[0]) * 60) + parseInt(parts[1]);
            } else {
                totalSeconds = parseFloat(goalInput) * 60;
            }
            return totalSeconds;
        }

        function updateLiveEstFinish() {
            if (currentSegIndex === 0 && totalElapsedSec === 0) {
                document.getElementById('coach-est-finish').innerText = document.getElementById('sim-goal-total').value || "--:--:--";
                return;
            }

            const goalTotalSec = getGoalTotalSeconds();
            const totalRunSec = goalTotalSec * 0.55;
            const singleRunSec = totalRunSec / 8;
            const singleStationSec = (goalTotalSec * 0.45) / 8;

            let targetCompletedSec = 0;
            let targetRemainingSec = 0;

            for (let i = 0; i < 16; i++) {
                const segDuration = (i % 2 === 0) ? singleRunSec : singleStationSec;
                if (i < currentSegIndex) {
                    targetCompletedSec += segDuration;
                } else {
                    targetRemainingSec += segDuration;
                }
            }

            const actualCompletedSec = totalElapsedSec;
            let projectedTotalSec = goalTotalSec;
            if (targetCompletedSec > 0 && currentSegIndex > 0) {
                const paceRatio = actualCompletedSec / targetCompletedSec;
                projectedTotalSec = actualCompletedSec + (targetRemainingSec * paceRatio);
            }

            const th = Math.floor(projectedTotalSec / 3600);
            const tm = Math.floor((projectedTotalSec % 3600) / 60);
            const ts = Math.round(projectedTotalSec % 60);
            const formattedProj = `${th > 0 ? th + ':' : ''}${tm.toString().padStart(2,'0')}:${ts.toString().padStart(2,'0')}`;
            
            document.getElementById('coach-est-finish').innerText = formattedProj;
        }

        function startCoachLiveRace() {
            if (coachTimerInterval) return;
            document.getElementById('coach-active-badge').innerText = "LIVE RACING";
            document.getElementById('coach-active-badge').className = "bg-green-500/20 text-green-400 border border-green-500/40 text-[10px] px-2.5 py-1 rounded-full font-bold uppercase animate-pulse";
            
            coachTimerInterval = setInterval(() => {
                totalElapsedSec++;
                segElapsedSec++;

                const th = Math.floor(totalElapsedSec / 3600);
                const tm = Math.floor((totalElapsedSec % 3600) / 60);
                const ts = totalElapsedSec % 60;
                document.getElementById('coach-total-timer').innerText = `${th > 0 ? th + ':' : ''}${tm.toString().padStart(2,'0')}:${ts.toString().padStart(2,'0')}`;

                const sm = Math.floor(segElapsedSec / 60);
                const ss = segElapsedSec % 60;
                document.getElementById('coach-seg-timer').innerText = `${sm.toString().padStart(2,'0')}:${ss.toString().padStart(2,'0')}`;

                updateLiveEstFinish();
            }, 1000);
        }

        function recordCoachSplit() {
            if (!coachTimerInterval && totalElapsedSec === 0) {
                startCoachLiveRace();
                return;
            }

            const segName = segmentNamesList[currentSegIndex];
            const sm = Math.floor(segElapsedSec / 60);
            const ss = segElapsedSec % 60;
            const splitStr = `${sm}:${ss < 10 ? '0' : ''}${ss}`;

            const th = Math.floor(totalElapsedSec / 3600);
            const tm = Math.floor((totalElapsedSec % 3600) / 60);
            const ts = totalElapsedSec % 60;
            const cumStr = `${th > 0 ? th + ':' : ''}${tm.toString().padStart(2,'0')}:${ts.toString().padStart(2,'0')}`;

            coachSplitsLog.push({ index: currentSegIndex + 1, name: segName, split: splitStr, cumulative: cumStr });
            
            const actInput = document.getElementById(`seg${currentSegIndex + 1}-act`);
            if (actInput) actInput.value = splitStr;

            currentSegIndex++;
            segElapsedSec = 0;

            if (currentSegIndex < segmentNamesList.length) {
                document.getElementById('coach-current-segment').innerText = `Segment ${currentSegIndex + 1}: ${segmentNamesList[currentSegIndex]}`;
            } else {
                document.getElementById('coach-current-segment').innerText = "RACE FINISHED! 🎉";
                document.getElementById('coach-active-badge').innerText = "FINISHED";
                pauseCoachLiveRace();
            }

            renderCoachLiveTable();
            updateLiveEstFinish();
        }

        function renderCoachLiveTable() {
            const tbody = document.getElementById('coach-live-log-tbody');
            if (coachSplitsLog.length === 0) {
                tbody.innerHTML = `<tr><td colspan="4" class="p-4 text-center text-gray-500">Live splits will appear here as you record them during the race.</td></tr>`;
                return;
            }
            let html = '';
            coachSplitsLog.forEach(item => {
                html += `
                    <tr>
                        <td class="p-2.5 font-bold text-hyrox-yellow">${item.index}</td>
                        <td class="p-2.5 font-medium text-white">${item.name}</td>
                        <td class="p-2.5 font-mono text-white">${item.split}</td>
                        <td class="p-2.5 font-mono text-hyrox-yellow">${item.cumulative}</td>
                    </tr>
                `;
            });
            tbody.innerHTML = html;
        }

        function pauseCoachLiveRace() {
            clearInterval(coachTimerInterval);
            coachTimerInterval = null;
            document.getElementById('coach-active-badge').innerText = "PAUSED";
            document.getElementById('coach-active-badge').className = "bg-yellow-500/20 text-yellow-400 border border-yellow-500/40 text-[10px] px-2.5 py-1 rounded-full font-bold uppercase";
        }

        function resetCoachLiveRace() {
            pauseCoachLiveRace();
            totalElapsedSec = 0;
            segElapsedSec = 0;
            currentSegIndex = 0;
            coachSplitsLog = [];
            document.getElementById('coach-total-timer').innerText = "00:00:00";
            document.getElementById('coach-seg-timer').innerText = "00:00";
            document.getElementById('coach-current-segment').innerText = `Segment 1: ${segmentNamesList[0]}`;
            document.getElementById('coach-active-badge').innerText = "Ready to Start";
            document.getElementById('coach-active-badge').className = "bg-hyrox-yellow/20 text-hyrox-yellow border border-hyrox-yellow/40 text-[10px] px-2.5 py-1 rounded-full font-bold uppercase";
            document.getElementById('coach-est-finish').innerText = document.getElementById('sim-goal-total').value || "--:--:--";
            renderCoachLiveTable();
        }

        function generateShareCard(type) {
            const raceName = document.getElementById('setting-race-name').value;
            const divisionKey = document.getElementById('setting-division').value;
            const divName = divisionStandards[divisionKey].name.replace(' Standards', '');
            const athleteName = document.getElementById('sim-athlete').value || 'Athlete';
            const weekNum = document.getElementById('program-week-select').value;
            
            document.getElementById('card-race-tag').innerText = raceName.toUpperCase();
            document.getElementById('card-date-tag').innerText = new Date().toLocaleDateString();
            document.getElementById('card-athlete-name').innerText = athleteName;
            document.getElementById('card-division-name').innerText = divName;
            document.getElementById('card-week-val').innerText = `Week ${weekNum} Master Plan`;

            const metricsBox = document.getElementById('card-metrics-box');

            if (type === 'daily') {
                const selectedDayIdx = parseInt(document.getElementById('card-day-select').value) || 0;
                const dayObj = programData[weekNum].days[selectedDayIdx];
                document.getElementById('card-title-type').innerText = "Daily Workout Graphic";
                document.getElementById('card-main-title').innerText = `Week ${weekNum} - ${dayObj.day.split(' - ')[0]}`;
                
                let workoutListHtml = `<div class="font-bold text-hyrox-yellow mb-1">${dayObj.day}</div>`;
                dayObj.exercises.forEach(ex => {
                    workoutListHtml += `<div class="flex justify-between border-b border-gray-800/50 py-0.5"><span>${ex.name}</span><span class="text-gray-400">${ex.reps}</span></div>`;
                });
                metricsBox.innerHTML = `<div class="text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-1">Scheduled Exercises & Runs</div><div class="space-y-1 text-gray-300 text-[11px]">${workoutListHtml}</div>`;
            } else if (type === 'weekly') {
                document.getElementById('card-title-type').innerText = "Weekly Progress Graphic";
                document.getElementById('card-main-title').innerText = `Week ${weekNum} Summary`;
                metricsBox.innerHTML = `<div class="text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-1">Weekly Metrics</div><div class="flex justify-between"><span class="text-gray-400">Block Focus:</span><span class="font-bold text-white">${programData[weekNum].focus}</span></div><div class="flex justify-between"><span class="text-gray-400">Volume Status:</span><span class="font-bold text-hyrox-yellow">100% Completed</span></div>`;
            } else if (type === 'sim') {
                const totalTime = document.getElementById('sim-total-time').value || '1:14:32';
                const sessionRpe = document.getElementById('sim-rpe').value || '8.5';
                document.getElementById('card-title-type').innerText = "Race Simulator Result";
                document.getElementById('card-main-title').innerText = "Full Race Simulation";
                metricsBox.innerHTML = `<div class="text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-1">Simulation Results</div><div class="flex justify-between"><span class="text-gray-400">Total Sim Time:</span><span class="font-bold font-mono text-white">${totalTime}</span></div><div class="flex justify-between"><span class="text-gray-400">Session RPE:</span><span class="font-bold font-mono text-hyrox-yellow">${sessionRpe} / 10</span></div>`;
            }
        }

        function calculatePace() {
            const paceStr = document.getElementById('calc-pace').value;
            const stationTimeMin = parseFloat(document.getElementById('calc-station-time').value) || 4.5;
            const parts = paceStr.split(':');
            const totalSecPerKm = ((parseFloat(parts[0]) || 5) * 60) + (parseFloat(parts[1]) || 0);
            const totalRaceSec = (totalSecPerKm * 8) + (stationTimeMin * 60 * 8);
            const hours = Math.floor(totalRaceSec / 3600);
            const minutes = Math.floor((totalRaceSec % 3600) / 60);
            const seconds = Math.floor(totalRaceSec % 60);
            document.getElementById('est-time').innerText = `${hours.toString().padStart(2,'0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }
        calculatePace();

        function saveSimLog() {
            localStorage.setItem('hyrox_sim_log', JSON.stringify({
                date: document.getElementById('sim-date').value,
                week: document.getElementById('sim-week').value,
                athlete: document.getElementById('sim-athlete').value,
                totalTime: document.getElementById('sim-total-time').value,
                rpe: document.getElementById('sim-rpe').value
            }));
            alert('Race simulation log saved successfully!');
        }

        function clearSimLog() {
            ['sim-total-time', 'sim-avg-hr', 'sim-peak-hr', 'sim-rpe'].forEach(id => {
                const el = document.getElementById(id);
                if(el) el.value = '';
            });
            alert('Simulation log fields cleared.');
        }

        function savePostRaceLog() {
            localStorage.setItem('hyrox_post_race', JSON.stringify({
                time: document.getElementById('post-time').value,
                goal: document.getElementById('post-goal').value,
                place: document.getElementById('post-place').value,
                achieved: document.getElementById('post-achieved').value,
                reflection: document.getElementById('post-reflection').value
            }));
            alert('Post-race journal saved successfully!');
        }

        document.getElementById('sim-date').valueAsDate = new Date();
        const savedSettings = JSON.parse(localStorage.getItem('hyrox_custom_settings'));
        if (savedSettings) {
            document.getElementById('setting-race-name').value = savedSettings.raceName || 'HYROX Houston';
            document.getElementById('setting-race-date').value = savedSettings.raceDateVal || '2026-03-29';
            document.getElementById('setting-division').value = savedSettings.divisionKey || 'womens-double';
        }
        updateRaceSettings();
        updateCountdown();
        renderProgramWeek();
        autoCalculateTargets();
        generateShareCard('daily');
        document.getElementById('coach-est-finish').innerText = document.getElementById('sim-goal-total').value || "1:15:00";
    </script>
</body>
</html>
