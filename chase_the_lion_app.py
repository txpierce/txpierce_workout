<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TX Pierce Baseball Training | Sequential Baseball</title>
    <!-- Tailwind CSS for modern styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- EmailJS SDK -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    <script type="text/javascript">
        (function() {
            emailjs.init("NBBKHwkytX5n5eJJy");
        })();
    </script>
</head>
<body class="bg-slate-900 text-slate-100 font-sans min-h-screen flex flex-col">

    <!-- Header & Navigation -->
    <header class="bg-slate-950 border-b border-slate-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="flex items-center space-x-3">
                <div class="bg-blue-600 p-2 rounded-lg text-white font-black text-xl tracking-wider shadow-lg shadow-blue-600/30">
                    <i class="fa-solid fa-baseball"></i> TXP
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-white">TX Pierce Baseball Training</h1>
                    <p class="text-xs text-slate-400">Coach Matt Pierce | Houston, TX</p>
                </div>
            </div>
            <nav class="flex flex-wrap justify-center gap-2 md:gap-4">
                <button onclick="switchTab('home')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-blue-600 text-white transition shadow" id="btn-home">Home & Pricing</button>
                <button onclick="switchTab('book')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition" id="btn-book">Book a Session</button>
                <button onclick="switchTab('agenda')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition" id="btn-agenda"><i class="fa-solid fa-calendar-days mr-1"></i> My Schedule</button>
                <button onclick="switchTab('calendar')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition" id="btn-calendar"><i class="fa-solid fa-calendar-alt mr-1"></i> Calendar View</button>
                <button onclick="switchTab('camps')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition" id="btn-camps"><i class="fa-solid fa-campground mr-1"></i> Camps & Clinics</button>
                <button onclick="switchTab('admin')" class="nav-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition" id="btn-admin"><i class="fa-solid fa-lock mr-1"></i> Admin</button>
            </nav>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-grow max-w-6xl w-full mx-auto px-4 py-8">

        <!-- TAB 1: HOME & PRICING -->
        <section id="tab-home" class="space-y-8 max-w-4xl mx-auto">
            <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-blue-900 via-slate-900 to-slate-950 border border-slate-800 p-8 md:p-12 shadow-2xl">
                <div class="max-w-2xl space-y-4">
                    <span class="bg-blue-500/20 text-blue-400 text-xs font-semibold px-3 py-1 rounded-full border border-blue-500/30">Elite Sequencing & Development</span>
                    <h2 class="text-3xl md:text-5xl font-extrabold tracking-tight text-white">WE ARE HERE TO MAKE BETTER HITTERS</h2>
                    <p class="text-slate-300 text-base md:text-lg">
                        Train with Coach Matt Pierce in Houston, TX. For any payment concerns, please contact directly—we will work with you!
                    </p>
                    <div class="pt-2 flex flex-wrap gap-4 text-sm text-slate-300">
                        <span><i class="fa-solid fa-phone text-blue-500 mr-2"></i> 832.443.2715</span>
                        <span><i class="fa-solid fa-envelope text-blue-500 mr-2"></i> Pierce.Matt.C@gmail.com</span>
                    </div>
                </div>
            </div>

            <!-- Pricing Grid -->
            <div class="space-y-4">
                <div class="text-center space-y-1">
                    <h3 class="text-2xl font-bold text-white">Hitting Lesson & Training Pricing</h3>
                    <p class="text-sm text-slate-400">For any payment concerns please contact directly! We will work with you.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
                    <!-- Lessons Pricing Card -->
                    <div class="bg-slate-950 rounded-xl border border-slate-800 p-6 flex flex-col justify-between hover:border-slate-700 transition shadow-lg">
                        <div>
                            <div class="flex justify-between items-center mb-4">
                                <span class="bg-emerald-500/10 text-emerald-400 text-xs font-bold px-2.5 py-1 rounded">PRIVATE LESSONS</span>
                                <span class="text-2xl font-black text-white">$100 <span class="text-xs font-normal text-slate-400">/ 1HR</span></span>
                            </div>
                            <h4 class="text-lg font-bold text-white mb-2">Private Lesson Options</h4>
                            <ul class="text-slate-400 text-sm space-y-1.5 mb-4">
                                <li><i class="fa-solid fa-check text-emerald-500 mr-2"></i> 1-on-1 Lesson: $100 / 1hr</li>
                                <li><i class="fa-solid fa-check text-emerald-500 mr-2"></i> 2-on-1 Lesson: $100 / hr (add both hitters during booking)</li>
                            </ul>
                        </div>
                        <button onclick="switchTab('book')" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-medium py-2.5 rounded-lg transition text-sm shadow">Book Lesson</button>
                    </div>

                    <!-- Youth Group Pricing Card -->
                    <div class="bg-slate-950 rounded-xl border border-slate-800 p-6 flex flex-col justify-between hover:border-slate-700 transition shadow-lg">
                        <div>
                            <div class="flex justify-between items-center mb-4">
                                <span class="bg-purple-500/10 text-purple-400 text-xs font-bold px-2.5 py-1 rounded">YOUTH GROUP (4 PLAYERS)</span>
                                <span class="text-xl font-black text-white">$100 <span class="text-xs font-normal text-slate-400">/ player</span></span>
                            </div>
                            <h4 class="text-lg font-bold text-white mb-2">Youth Duo Hitting & Fielding (1.5 Hours)</h4>
                            <ul class="text-slate-400 text-sm space-y-1.5 mb-4">
                                <li><i class="fa-solid fa-check text-emerald-500 mr-2"></i> Players 1 & 2: Arrive at Start Time (1hr Hitting + 30m Defense)</li>
                                <li><i class="fa-solid fa-check text-emerald-500 mr-2"></i> Players 3 & 4: Arrive 1 Hr After Start (30m Defense + 1hr Hitting)</li>
                            </ul>
                        </div>
                        <button onclick="switchTab('book')" class="w-full bg-slate-800 hover:bg-slate-700 text-white font-medium py-2.5 rounded-lg transition text-sm">Book Group Session</button>
                    </div>
                </div>
            </div>

            <!-- Payment Box -->
            <div class="bg-slate-950 rounded-xl border border-slate-800 p-6 text-center space-y-4 shadow-lg">
                <h4 class="font-bold text-white">Online Hitting Payment Options</h4>
                <p class="text-xs text-slate-400">Payments are requested manually by Coach Matt Pierce (no automatic billing).</p>
                <div class="flex flex-wrap justify-center gap-4">
                    <a href="https://www.paypal.me/TXPierce" target="_blank" class="bg-blue-700 hover:bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg text-sm transition flex items-center gap-2 shadow">
                        <i class="fa-brands fa-paypal"></i> PayPal: paypal.me/TXPierce
                    </a>
                    <div class="bg-slate-800 text-slate-200 px-6 py-3 rounded-lg text-sm font-semibold flex items-center gap-2 border border-slate-700 shadow">
                        <i class="fa-solid fa-mobile-screen text-cyan-400"></i> Venmo: @TX-Pierce
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 2: BOOK A SESSION -->
        <section id="tab-book" class="hidden space-y-6 max-w-4xl mx-auto">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                    <h3 class="text-2xl font-bold text-white">Available Training Slots</h3>
                    <p class="text-sm text-slate-400">Select an open slot or player position below to book your spot. Syncs live across all devices.</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="inline-block w-3 h-3 rounded-full bg-emerald-500"></span> <span class="text-xs text-slate-300 mr-3">Available Spot</span>
                    <span class="inline-block w-3 h-3 rounded-full bg-rose-500"></span> <span class="text-xs text-slate-300">Filled / Booked</span>
                </div>
            </div>

            <!-- Loading Indicator -->
            <div id="loading-spinner" class="text-center py-12 text-slate-400">
                <i class="fa-solid fa-spinner fa-spin text-3xl text-blue-500 mb-2"></i>
                <p class="text-sm">Fetching live schedule status...</p>
            </div>

            <!-- Available Slots Stacked Container -->
            <div id="slots-container" class="space-y-4">
                <!-- Dynamically populated via JavaScript -->
            </div>
        </section>

        <!-- TAB 3: MY SCHEDULE (AGENDA VIEW) -->
        <section id="tab-agenda" class="hidden space-y-6 max-w-4xl mx-auto">
            <div class="space-y-1">
                <h3 class="text-2xl font-bold text-white">Weekly Training Schedule & Agenda</h3>
                <p class="text-sm text-slate-400">View all booked training sessions, team practices, and games in one consolidated timeline.</p>
            </div>
            <div id="agenda-container" class="space-y-4">
                <!-- Populated dynamically via JS -->
            </div>
        </section>

        <!-- TAB 4: CALENDAR VIEW -->
        <section id="tab-calendar" class="hidden space-y-6">
            <div class="flex justify-between items-center bg-slate-950 p-4 rounded-xl border border-slate-800">
                <button onclick="changeMonth(-1)" class="bg-slate-800 hover:bg-slate-700 text-white px-3.5 py-2 rounded text-sm transition font-medium"><i class="fa-solid fa-chevron-left mr-1"></i> Prev</button>
                <h3 id="calendar-month-year" class="text-xl font-bold text-white">November 2026</h3>
                <button onclick="changeMonth(1)" class="bg-slate-800 hover:bg-slate-700 text-white px-3.5 py-2 rounded text-sm transition font-medium">Next <i class="fa-solid fa-chevron-right ml-1"></i></button>
            </div>
            <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 shadow-xl overflow-x-auto">
                <div class="grid grid-cols-7 gap-3 text-center font-bold text-xs text-slate-400 pb-3 border-b border-slate-800 min-w-[700px]">
                    <div>Sun</div><div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div>
                </div>
                <div id="calendar-grid" class="grid grid-cols-7 gap-3 pt-3 min-w-[700px]">
                    <!-- Populated dynamically via JS -->
                </div>
            </div>
        </section>

        <!-- TAB 5: CAMPS & CLINICS -->
        <section id="tab-camps" class="hidden space-y-6 max-w-4xl mx-auto">
            <div class="space-y-2">
                <h3 class="text-2xl font-bold text-white">Upcoming Camps & Clinics</h3>
                <p class="text-sm text-slate-400">Browse active baseball camps, view Google Drive flyers, or register via Google Forms.</p>
            </div>
            <div id="camps-container" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Dynamically populated via JS -->
            </div>
        </section>

        <!-- TAB 6: ADMIN PANEL -->
        <section id="tab-admin" class="hidden space-y-6 max-w-4xl mx-auto">
            <!-- Schedule Manager Card -->
            <div class="bg-slate-950 rounded-xl border border-slate-800 p-6 space-y-6 shadow-xl">
                <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                    <div>
                        <h3 class="text-xl font-bold text-white">Coach Admin Dashboard</h3>
                        <p class="text-xs text-slate-400">Add training slots, team practices, games, or build camps.</p>
                    </div>
                    <span class="bg-blue-500/20 text-blue-400 text-xs px-2.5 py-1 rounded font-semibold">Admin Mode</span>
                </div>

                <!-- Add Slot Form -->
                <form id="add-slot-form" onsubmit="addNewSlot(event)" class="space-y-4 bg-slate-900 p-4 rounded-lg border border-slate-800">
                    <h4 class="font-bold text-sm text-white">Add Schedule Event / Training Slot</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Event / Session Type</label>
                            <select id="admin-type" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                                <option value="1-on-1 Lesson (1HR) - $100">1-on-1 Lesson (1HR) - $100</option>
                                <option value="2-on-1 Lesson (1HR) - $100">2-on-1 Lesson (1HR) - $100</option>
                                <option value="Youth Duo Hitting & Fielding (1.5HR) - $100/player">Youth Duo Hitting & Fielding (1.5HR) - $100/player</option>
                                <option value="Team Practice">⚾ Team Practice</option>
                                <option value="Team Game">🏆 Team Game</option>
                                <option value="Team Scrimmage">⚔️ Team Scrimmage</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Date & Time</label>
                            <input type="datetime-local" id="admin-datetime" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500 [color-scheme:dark]">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Recurring Option (Practices Only)</label>
                            <select id="admin-recurrence" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                                <option value="none">One-time Event (No Repeat)</option>
                                <option value="weekly_4">Repeat Weekly for 4 Weeks</option>
                                <option value="weekly_8">Repeat Weekly for 8 Weeks</option>
                                <option value="weekly_12">Repeat Weekly for 12 Weeks</option>
                                <option value="weekday_2">Weekday Daily (Mon-Fri) for 2 Weeks</option>
                                <option value="weekday_4">Weekday Daily (Mon-Fri) for 4 Weeks</option>
                            </select>
                        </div>
                        <div class="flex items-end">
                            <button type="submit" class="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-medium py-2.5 rounded-lg text-sm transition shadow">Publish Event to Schedule</button>
                        </div>
                    </div>
                </form>

                <!-- Current Bookings Overview -->
                <div class="space-y-3">
                    <h4 class="font-bold text-sm text-white">Manage Active Schedule & Bookings</h4>
                    <div id="admin-bookings-list" class="space-y-2">
                        <!-- Populated via JS -->
                    </div>
                </div>
            </div>

            <!-- Camp Builder Card -->
            <div class="bg-slate-950 rounded-xl border border-slate-800 p-6 space-y-6 shadow-xl">
                <div class="border-b border-slate-800 pb-4">
                    <h3 class="text-xl font-bold text-white"><i class="fa-solid fa-campground text-blue-500 mr-2"></i> Camp & Clinic Builder</h3>
                    <p class="text-xs text-slate-400">Publish camps with Google Drive flyers and Google Form sign-up links.</p>
                </div>

                <form id="add-camp-form" onsubmit="addNewCamp(event)" class="space-y-4 bg-slate-900 p-4 rounded-lg border border-slate-800">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Camp Title</label>
                            <input type="text" id="camp-title" placeholder="e.g. Winter Elite Hitting Camp" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Date & Time / Details</label>
                            <input type="text" id="camp-date" placeholder="e.g. Dec 20-22, 2026 | 9:00 AM - 12:00 PM" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Google Drive Flyer URL</label>
                            <input type="url" id="camp-flyer" placeholder="https://drive.google.com/..." required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Google Form Sign-up URL</label>
                            <input type="url" id="camp-form" placeholder="https://forms.gle/..." required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-medium text-slate-400 mb-1">Camp Description</label>
                        <textarea id="camp-desc" rows="2" placeholder="Brief details about what players will learn..." required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500"></textarea>
                    </div>

                    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-medium py-2.5 rounded-lg text-sm transition shadow">Publish Camp Flyer</button>
                </form>

                <div class="space-y-3">
                    <h4 class="font-bold text-sm text-white">Manage Active Camps</h4>
                    <div id="admin-camps-list" class="space-y-2">
                        <!-- Populated via JS -->
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Booking Modal -->
    <div id="booking-modal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-md w-full p-6 space-y-4 shadow-2xl">
            <div class="flex justify-between items-center">
                <h3 class="text-lg font-bold text-white" id="modal-title">Complete Booking</h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            </div>
            <p id="modal-slot-info" class="text-xs text-blue-400 font-medium"></p>
            <form id="booking-form" onsubmit="confirmBooking(event)" class="space-y-4">
                <input type="hidden" id="modal-slot-id">
                <input type="hidden" id="modal-position-index">
                
                <div>
                    <label class="block text-xs font-medium text-slate-400 mb-1" id="label-hitter-1">Player's Last Name</label>
                    <input type="text" id="player-lastname" placeholder="e.g. Smith" required class="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                </div>

                <div id="hitter-2-container" class="hidden">
                    <label class="block text-xs font-medium text-slate-400 mb-1">Second Hitter's Last Name</label>
                    <input type="text" id="player-lastname-2" placeholder="e.g. Jones" class="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                </div>

                <div>
                    <label class="block text-xs font-medium text-slate-400 mb-1">Parent Venmo Handle (@username)</label>
                    <input type="text" id="parent-venmo" placeholder="e.g. @John-Smith-1" required class="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                </div>

                <div>
                    <label class="block text-xs font-medium text-slate-400 mb-1">Parent Phone Number</label>
                    <input type="tel" id="parent-phone" placeholder="e.g. 832-555-1234" oninput="formatPhoneNumberInput(this)" required class="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-blue-500">
                </div>

                <p class="text-xs text-slate-400">Payment requests will be coordinated manually by Coach Matt Pierce.</p>
                <div class="flex gap-3 pt-2">
                    <button type="button" onclick="closeModal()" class="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-300 py-2.5 rounded-lg text-sm font-medium transition">Cancel</button>
                    <button type="submit" class="flex-1 bg-blue-600 hover:bg-blue-500 text-white py-2.5 rounded-lg text-sm font-medium transition shadow">Confirm & Book</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-950 border-t border-slate-800 py-6 mt-12 text-center text-xs text-slate-500">
        <p>&copy; 2026 TX Pierce Baseball Training (Sequential Baseball Training). All rights reserved.</p>
    </footer>

    <!-- JavaScript Application Logic -->
    <script>
        const BIN_URL = "https://api.jsonbin.io/v3/b/6ae48dc5ac6210605a5eb12c";
        const MASTER_KEY = "2a10$KqVOg/LxrBXCa2B5..s75e9TF3O0kQ1k5kNpOeZPvaewH5x6dBOiu";

        let slots = [];
        let camps = [];
        let currentCalendarDate = new Date(2026, 10, 1); // Default to Nov 2026

        const defaultSlots = [
            { id: 1, type: "1-on-1 Lesson (1HR) - $100", datetime: "Mon, Nov 2, 2026 | 4:00 PM", slotsNeeded: 1, players: [""], phones: [""] },
            { id: 2, type: "2-on-1 Lesson (1HR) - $100", datetime: "Tue, Nov 3, 2026 | 5:00 PM", slotsNeeded: 2, players: ["", ""], phones: ["", ""] },
            { 
                id: 3, 
                type: "Youth Duo Hitting & Fielding (1.5HR) - $100/player", 
                datetime: "Wed, Dec 2, 2026 | 3:30 PM", 
                slotsNeeded: 4, 
                players: ["", "", "", ""],
                phones: ["", "", "", ""],
                isYouthDuoGroup: true
            },
            { id: 4, type: "1-on-1 Lesson (1HR) - $100", datetime: "Thu, Nov 5, 2026 | 4:30 PM", slotsNeeded: 1, players: [""], phones: [""] }
        ];

        const defaultCamps = [
            {
                id: 101,
                title: "Winter Elite Hitting & Mechanics Camp",
                date: "Dec 28 - Dec 30, 2026 | 9:00 AM - 12:00 PM",
                flyer: "https://drive.google.com",
                form: "https://forms.gle",
                desc: "Intensive 3-day hitting sequencing camp focusing on barrel path, rotational acceleration, and game-speed mechanics."
            }
        ];

        // Format phone number live as xxx-xxx-xxxx
        function formatPhoneNumberInput(input) {
            let cleaned = input.value.replace(/\D/g, '').substring(0, 10);
            let match = cleaned.match(/^(\d{0,3})(\d{0,3})(\d{0,4})$/);
            if (match) {
                let formatted = match[1];
                if (match[2]) formatted += '-' + match[2];
                if (match[3]) formatted += '-' + match[3];
                input.value = formatted;
            }
        }

        function formatDateTimeString(dateTimeStr) {
            if (!dateTimeStr || !dateTimeStr.includes('T')) return dateTimeStr;
            const dt = new Date(dateTimeStr);
            if (isNaN(dt.getTime())) return dateTimeStr;
            return dt.toLocaleString('en-US', { 
                weekday: 'short', 
                month: 'short', 
                day: 'numeric', 
                year: 'numeric', 
                hour: 'numeric', 
                minute: '2-digit', 
                hour12: true 
            }).replace(',', ' |');
        }

        function sortSlotsChronologically() {
            slots.sort((a, b) => {
                const dateA = new Date(a.datetime.replace(' |', ','));
                const dateB = new Date(b.datetime.replace(' |', ','));
                return dateA - dateB;
            });
        }

        async function fetchSlots(silent = false) {
            try {
                const response = await fetch(`${BIN_URL}/latest`, {
                    headers: { 'X-Master-Key': MASTER_KEY }
                });
                if (response.ok) {
                    const data = await response.json();
                    if (data.record && data.record.slots) {
                        slots = data.record.slots;
                        slots.forEach(s => {
                            if (!s.phones) s.phones = new Array(s.slotsNeeded).fill("");
                        });
                    }
                    if (data.record && data.record.camps) {
                        camps = data.record.camps;
                    } else if (!camps || camps.length === 0) {
                        camps = defaultCamps;
                    }
                }
            } catch (e) {
                console.log('Using local fallback.');
                if (slots.length === 0) {
                    slots = JSON.parse(localStorage.getItem('tx_pierce_slots_backup')) || defaultSlots;
                }
                if (camps.length === 0) {
                    camps = JSON.parse(localStorage.getItem('tx_pierce_camps_backup')) || defaultCamps;
                }
            }

            sortSlotsChronologically();

            if (!silent) {
                const spinner = document.getElementById('loading-spinner');
                if (spinner) spinner.classList.add('hidden');
            }
            renderSlots();
            renderAgenda();
            renderCalendar();
            renderCamps();
            if (!document.getElementById('tab-admin').classList.contains('hidden')) {
                renderAdminBookings();
                renderAdminCamps();
            }
        }

        async function saveSlots() {
            sortSlotsChronologically();
            localStorage.setItem('tx_pierce_slots_backup', JSON.stringify(slots));
            localStorage.setItem('tx_pierce_camps_backup', JSON.stringify(camps));
            renderSlots();
            renderAgenda();
            renderCalendar();
            renderCamps();

            try {
                await fetch(BIN_URL, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Master-Key': MASTER_KEY
                    },
                    body: JSON.stringify({ slots: slots, camps: camps })
                });
            } catch (err) {
                console.log('Cloud sync error.');
            }
        }

        function switchTab(tabId) {
            document.querySelectorAll('main > section').forEach(sec => sec.classList.add('hidden'));
            document.getElementById('tab-' + tabId).classList.remove('hidden');

            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('bg-blue-600', 'text-white', 'shadow');
                btn.classList.add('bg-slate-800', 'text-slate-300');
            });
            const activeBtn = document.getElementById('btn-' + tabId);
            activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
            activeBtn.classList.add('bg-blue-600', 'text-white', 'shadow');

            if (tabId === 'book' || tabId === 'admin' || tabId === 'agenda' || tabId === 'calendar' || tabId === 'camps') {
                fetchSlots();
            }
        }

        function renderSlots() {
            const container = document.getElementById('slots-container');
            if (!container) return;
            container.innerHTML = '';

            const bookingSlots = slots.filter(slot => !slot.isTeamEvent);

            if (bookingSlots.length === 0) {
                container.innerHTML = '<p class="text-sm text-slate-500 text-center py-6">No training slots available for booking at this time.</p>';
                return;
            }

            bookingSlots.forEach(slot => {
                const card = document.createElement('div');
                const isFullyBooked = slot.players.every(p => p !== "");
                
                card.className = `bg-slate-950 border rounded-xl p-5 flex flex-col justify-between transition shadow-xl w-full ${isFullyBooked ? 'border-rose-900/50 bg-rose-950/10' : 'border-slate-800 hover:border-slate-700'}`;
                
                let playerSlotsHtml = '<div class="space-y-3 mt-3 pt-3 border-t border-slate-800/60 text-xs">';
                
                if (slot.isYouthDuoGroup) {
                    playerSlotsHtml += `<div class="text-blue-400 font-bold uppercase tracking-wider text-[11px] pt-1 border-b border-slate-800/40 pb-1"><i class="fa-solid fa-clock mr-1"></i> Group 1: Arrive at Start Time (1hr Hitting + 30m Defense)</div>`;
                }

                slot.players.forEach((player, idx) => {
                    if (slot.isYouthDuoGroup && idx === 2) {
                        playerSlotsHtml += `<div class="text-purple-400 font-bold uppercase tracking-wider text-[11px] pt-3 border-b border-slate-800/40 pb-1"><i class="fa-solid fa-clock mr-1"></i> Group 2: Arrive 1 Hr After Start (30m Defense + 1hr Hitting)</div>`;
                    }

                    let posName = `Player ${idx + 1}`;
                    if (!slot.isYouthDuoGroup && slot.slotsNeeded === 2) {
                        posName = `Hitter ${idx + 1}`;
                    }

                    if (player) {
                        const phoneDisplay = slot.phones && slot.phones[idx] ? ` <span class="text-slate-400 font-normal">(${slot.phones[idx]})</span>` : '';
                        playerSlotsHtml += `<div class="flex justify-between items-center bg-slate-900 p-2.5 rounded border border-slate-800 text-slate-300">
                            <span><strong class="text-white">${posName}:</strong> player{phoneDisplay}</span>
                            <span class="text-rose-400 font-semibold text-[10px]">Filled</span>
                        </div>`;
                    } else {
                        playerSlotsHtml += `<div class="flex justify-between items-center bg-slate-900 p-2.5 rounded border border-slate-800 text-slate-400">
                            <span><strong class="text-slate-300">${posName}:</strong> Open Slot</span>
                            <button onclick="openBookingModal(${slot.id}, ${idx})" class="bg-blue-600 hover:bg-blue-500 text-white px-3.5 py-1.5 rounded text-xs font-medium transition shadow">Book Spot</button>
                        </div>`;
                    }
                });

                if (slot.isYouthDuoGroup) {
                    playerSlotsHtml += `<div class="mt-3 p-2 bg-blue-950/40 border border-blue-900/50 rounded text-[11px] text-blue-300 text-center">
                        <i class="fa-solid fa-circle-info mr-1"></i> All 4 Players: 30 Mins Combined Defense Together
                    </div>`;
                }

                playerSlotsHtml += '</div>';

                card.innerHTML = `
                    <div class="space-y-3">
                        <div class="flex justify-between items-start">
                            <span class="text-xs font-semibold px-2.5 py-1 rounded ${isFullyBooked ? 'bg-rose-500/10 text-rose-400' : 'bg-emerald-500/10 text-emerald-400'}">
                                ${isFullyBooked ? 'Session Full' : 'Available Spots'}
                            </span>
                            <span class="text-xs text-slate-400"><i class="fa-regular fa-clock mr-1"></i> ${slot.datetime}</span>
                        </div>
                        <h4 class="font-bold text-white text-base">${slot.type}</h4>
                        ${playerSlotsHtml}
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // Agenda / My Schedule View Renderer
        function renderAgenda() {
            const container = document.getElementById('agenda-container');
            if (!container) return;
            container.innerHTML = '';

            if (slots.length === 0) {
                container.innerHTML = '<p class="text-sm text-slate-500 text-center py-6">No scheduled training sessions or events found.</p>';
                return;
            }

            slots.forEach(slot => {
                const card = document.createElement('div');
                card.className = "bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3";

                if (slot.isTeamEvent) {
                    card.innerHTML = `
                        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 border-b border-slate-800 pb-3">
                            <div>
                                <span class="text-xs font-semibold text-purple-400 bg-purple-500/10 border border-purple-500/20 px-2 py-0.5 rounded">${slot.type}</span>
                                <h4 class="text-base font-bold text-white mt-1"><i class="fa-regular fa-calendar text-slate-400 mr-2"></i> ${slot.datetime}</h4>
                            </div>
                            <span class="text-xs font-semibold px-2.5 py-1 rounded bg-purple-500/10 text-purple-300 border border-purple-500/20">
                                Team Schedule
                            </span>
                        </div>
                        <div class="text-xs text-slate-300 italic">
                            <i class="fa-solid fa-users text-purple-400 mr-1.5"></i> Scheduled Team Practice / Event
                        </div>
                    `;
                } else {
                    let bookedItems = [];
                    slot.players.forEach((p, idx) => {
                        if (p !== "") {
                            let arrivalNote = `P${idx+1}`;
                            if (slot.isYouthDuoGroup) {
                                if (idx === 0 || idx === 1) arrivalNote = `P${idx+1} (Arrive at Start)`;
                                if (idx === 2 || idx === 3) arrivalNote = `P${idx+1} (Arrive +1 Hr)`;
                            }
                            const phoneStr = slot.phones && slot.phones[idx] ? ` <span class="text-slate-400 text-[11px]">(${slot.phones[idx]})</span>` : '';
                            
                            bookedItems.push(`<span class="bg-slate-900 border border-slate-800 px-3 py-2 rounded text-xs text-slate-200 flex items-center gap-2"><i class="fa-solid fa-user text-blue-500"></i> <strong class="text-white">p</strong>{phoneStr} <span class="text-[10px] text-amber-400 font-semibold bg-amber-500/10 border border-amber-500/20 px-1.5 py-0.5 rounded">(${arrivalNote})</span></span>`);
                        }
                    });

                    let rosterList = bookedItems.length > 0 
                        ? bookedItems.join('')
                        : '<span class="text-xs text-slate-500 italic">No players booked yet (Open slots available)</span>';

                    const filledCount = slot.players.filter(p => p !== "").length;

                    card.innerHTML = `
                        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 border-b border-slate-800 pb-3">
                            <div>
                                <span class="text-xs font-semibold text-blue-400 bg-blue-500/10 border border-blue-500/20 px-2 py-0.5 rounded">${slot.type}</span>
                                <h4 class="text-base font-bold text-white mt-1"><i class="fa-regular fa-calendar text-slate-400 mr-2"></i> ${slot.datetime}</h4>
                            </div>
                            <span class="text-xs font-semibold px-2.5 py-1 rounded ${filledCount === slot.slotsNeeded ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'}">
                                filledCount/{slot.slotsNeeded} Slots Filled
                            </span>
                        </div>
                        <div class="space-y-1">
                            <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Booked Roster & Arrival Times:</p>
                            <div class="flex flex-wrap gap-2 pt-1">
                                ${rosterList}
                            </div>
                        </div>
                    `;
                }
                container.appendChild(card);
            });
        }

        function renderCamps() {
            const container = document.getElementById('camps-container');
            if (!container) return;
            container.innerHTML = '';

            if (!camps || camps.length === 0) {
                container.innerHTML = '<p class="text-sm text-slate-500 col-span-2 text-center py-8">No camps or clinics currently advertised.</p>';
                return;
            }

            camps.forEach(camp => {
                const card = document.createElement('div');
                card.className = "bg-slate-950 border border-slate-800 rounded-xl p-6 flex flex-col justify-between shadow-xl space-y-4";

                card.innerHTML = `
                    <div class="space-y-2">
                        <span class="bg-blue-500/10 text-blue-400 text-xs font-bold px-2.5 py-1 rounded border border-blue-500/20"><i class="fa-solid fa-campground mr-1"></i> Featured Camp</span>
                        <h4 class="text-xl font-bold text-white">${camp.title}</h4>
                        <p class="text-xs font-semibold text-slate-400"><i class="fa-regular fa-calendar text-blue-400 mr-1.5"></i> ${camp.date}</p>
                        <p class="text-sm text-slate-300 leading-relaxed pt-1">${camp.desc}</p>
                    </div>

                    <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center gap-3">
                        <a href="${camp.flyer}" target="_blank" class="w-full text-center bg-slate-900 hover:bg-slate-800 text-blue-400 border border-blue-500/30 text-xs font-semibold py-2.5 px-4 rounded-lg transition shadow">
                            <i class="fa-solid fa-file-pdf mr-1.5"></i> View Google Drive Flyer
                        </a>
                        <a href="${camp.form}" target="_blank" class="w-full text-center bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold py-2.5 px-4 rounded-lg transition shadow">
                            <i class="fa-solid fa-clipboard-list mr-1.5"></i> Google Form Sign-Up
                        </a>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        function changeMonth(direction) {
            currentCalendarDate.setMonth(currentCalendarDate.getMonth() + direction);
            renderCalendar();
        }

        function renderCalendar() {
            const grid = document.getElementById('calendar-grid');
            const monthYearLabel = document.getElementById('calendar-month-year');
            if (!grid || !monthYearLabel) return;

            const year = currentCalendarDate.getFullYear();
            const month = currentCalendarDate.getMonth();

            monthYearLabel.innerText = currentCalendarDate.toLocaleString('default', { month: 'long', year: 'numeric' });
            grid.innerHTML = '';

            const firstDayIndex = new Date(year, month, 1).getDay();
            const totalDays = new Date(year, month + 1, 0).getDate();

            // Blank spaces for previous month offset
            for (let i = 0; i < firstDayIndex; i++) {
                const emptyCell = document.createElement('div');
                emptyCell.className = "min-h-[110px] bg-slate-900/30 rounded-xl border border-slate-800/40 opacity-30";
                grid.appendChild(emptyCell);
            }

            // Days of current month
            for (let day = 1; day <= totalDays; day++) {
                const cell = document.createElement('div');
                cell.className = "min-h-[125px] bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex flex-col justify-between shadow";

                const dateHeader = document.createElement('div');
                dateHeader.className = "text-xs font-bold text-slate-300 pb-1 border-b border-slate-800 mb-1.5 flex justify-between items-center";
                dateHeader.innerHTML = `<span>${day}</span>`;
                cell.appendChild(dateHeader);

                const eventsContainer = document.createElement('div');
                eventsContainer.className = "space-y-1.5 flex-grow overflow-y-auto";

                slots.forEach(slot => {
                    const slotDate = new Date(slot.datetime.replace(' |', ','));
                    if (
                        slotDate.getFullYear() === year &&
                        slotDate.getMonth() === month &&
                        slotDate.getDate() === day
                    ) {
                        const timeStr = slot.datetime.split('|')[1]?.trim() || '';
                        const shortType = slot.type.split('(')[0].trim();
                        const eventCard = document.createElement('div');

                        if (slot.isTeamEvent) {
                            eventCard.className = `p-1.5 rounded-lg border text-[11px] shadow-sm space-y-0.5 bg-purple-950/40 border-purple-900/60 text-purple-200`;
                            eventCard.innerHTML = `
                                <div class="font-bold flex items-center justify-between text-white">
                                    <span><i class="fa-solid fa-users text-purple-400 mr-1 text-[10px]"></i>${timeStr}</span>
                                </div>
                                <div class="text-[10px] text-purple-300 font-semibold truncate">${shortType}</div>
                            `;
                        } else {
                            const filledPlayers = slot.players.filter(p => p !== "").join(', ') || 'Open Slots';
                            const isFull = slot.players.every(p => p !== "");
                            eventCard.className = `p-1.5 rounded-lg border text-[11px] shadow-sm space-y-0.5 ${isFull ? 'bg-rose-950/40 border-rose-900/60 text-rose-200' : 'bg-blue-950/40 border-blue-900/60 text-blue-200'}`;
                            eventCard.innerHTML = `
                                <div class="font-bold flex items-center justify-between text-white">
                                    <span><i class="fa-regular fa-clock text-slate-400 mr-1 text-[10px]"></i>${timeStr}</span>
                                </div>
                                <div class="text-[10px] text-slate-300 font-semibold truncate">${shortType}</div>
                                <div class="text-[10px] text-amber-400 truncate"><i class="fa-solid fa-user mr-1 text-[9px]"></i>${filledPlayers}</div>
                            `;
                        }
                        eventsContainer.appendChild(eventCard);
                    }
                });

                cell.appendChild(eventsContainer);
                grid.appendChild(cell);
            }
        }

        function openBookingModal(slotId, positionIndex) {
            const slot = slots.find(s => s.id === slotId);
            document.getElementById('modal-slot-id').value = slot.id;
            document.getElementById('modal-position-index').value = positionIndex;
            document.getElementById('modal-slot-info').innerText = `${slot.type} — ${slot.datetime}`;
            document.getElementById('player-lastname').value = '';
            document.getElementById('player-lastname-2').value = '';
            document.getElementById('parent-venmo').value = '';
            document.getElementById('parent-phone').value = '';

            const hitter2Container = document.getElementById('hitter-2-container');
            const labelHitter1 = document.getElementById('label-hitter-1');

            if (slot.type.includes("2-on-1 Lesson") && positionIndex === 0) {
                hitter2Container.classList.remove('hidden');
                labelHitter1.innerText = "First Hitter's Last Name";
                document.getElementById('player-lastname-2').required = true;
            } else {
                hitter2Container.classList.add('hidden');
                labelHitter1.innerText = "Player's Last Name";
                document.getElementById('player-lastname-2').required = false;
            }

            document.getElementById('booking-modal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('booking-modal').classList.add('hidden');
        }

        async function confirmBooking(event) {
            event.preventDefault();
            const slotId = parseInt(document.getElementById('modal-slot-id').value);
            const positionIndex = parseInt(document.getElementById('modal-position-index').value);
            const player1 = document.getElementById('player-lastname').value.trim();
            const player2 = document.getElementById('player-lastname-2').value.trim();
            const venmo = document.getElementById('parent-venmo').value.trim();
            const phone = document.getElementById('parent-phone').value.trim();

            const slot = slots.find(s => s.id === slotId);
            if (slot) {
                if (!slot.phones) slot.phones = new Array(slot.slotsNeeded).fill("");
                
                slot.players[positionIndex] = player1;
                slot.phones[positionIndex] = phone;
                
                if (slot.type.includes("2-on-1 Lesson") && positionIndex === 0 && player2 && slot.players.length > 1) {
                    slot.players[1] = player2;
                    slot.phones[1] = phone;
                }

                closeModal();
                await saveSlots(); // Syncs to cloud bin immediately

                // --- EMAILJS NOTIFICATION TRIGGER ---
                const templateParams = {
                    session_type: slot.type,
                    session_datetime: slot.datetime,
                    player_name: player1 + (player2 ? ` & ${player2}` : ''),
                    parent_venmo: venmo,
                    parent_phone: phone
                };

                emailjs.send('service_uwpsp0v', 'template_l7bpk0i', templateParams, 'NBBKHwkytX5n5eJJy')
                    .then(function(response) {
                        alert(`Successfully booked for player(s)! Email notification sent to Coach Matt Pierce.`);
                    }, function(error) {
                        alert(`Successfully booked for player(s), but email notification failed.`);
                    });
            }
        }

        async function addNewSlot(event) {
            event.preventDefault();
            const type = document.getElementById('admin-type').value;
            const rawDatetime = document.getElementById('admin-datetime').value;
            const recurrenceMode = document.getElementById('admin-recurrence').value;

            if (!rawDatetime) return;

            const isTeamEvent = type.includes("Team");
            const baseDate = new Date(rawDatetime);

            let eventDates = [];

            if (isTeamEvent && recurrenceMode !== "none") {
                if (recurrenceMode.startsWith("weekly_")) {
                    const weeks = parseInt(recurrenceMode.split("_")[1]);
                    for (let i = 0; i < weeks; i++) {
                        let d = new Date(baseDate);
                        d.setDate(d.getDate() + (i * 7));
                        eventDates.push(d);
                    }
                } else if (recurrenceMode.startsWith("weekday_")) {
                    const weeks = parseInt(recurrenceMode.split("_")[1]);
                    const totalDays = weeks * 5;
                    let currentDate = new Date(baseDate);
                    
                    let addedCount = 0;
                    while (addedCount < totalDays) {
                        const dayOfWeek = currentDate.getDay();
                        if (dayOfWeek >= 1 && dayOfWeek <= 5) {
                            eventDates.push(new Date(currentDate));
                            addedCount++;
                        }
                        currentDate.setDate(currentDate.getDate() + 1);
                    }
                }
            } else {
                eventDates.push(new Date(baseDate));
            }

            eventDates.forEach((eventDate, i) => {
                const datetimeFormatted = eventDate.toLocaleString('en-US', { 
                    weekday: 'short', 
                    month: 'short', 
                    day: 'numeric', 
                    year: 'numeric', 
                    hour: 'numeric', 
                    minute: '2-digit', 
                    hour12: true 
                }).replace(',', ' |');

                let slotsNeeded = 1;
                let isYouthDuoGroup = false;

                if (type.includes("2-on-1 Lesson")) slotsNeeded = 2;
                if (type.includes("Youth Duo")) {
                    slotsNeeded = 4;
                    isYouthDuoGroup = true;
                }

                const newSlot = {
                    id: Date.now() + i,
                    type: type,
                    datetime: datetimeFormatted,
                    slotsNeeded: slotsNeeded,
                    players: new Array(slotsNeeded).fill(""),
                    phones: new Array(slotsNeeded).fill(""),
                    isYouthDuoGroup: isYouthDuoGroup,
                    isTeamEvent: isTeamEvent
                };

                slots.push(newSlot);
            });

            await saveSlots();
            document.getElementById('admin-datetime').value = '';
            document.getElementById('admin-recurrence').value = 'none';
            alert('New schedule event(s) published live across all devices!');
            renderAdminBookings();
        }

        async function addNewCamp(event) {
            event.preventDefault();
            const title = document.getElementById('camp-title').value.trim();
            const date = document.getElementById('camp-date').value.trim();
            const flyer = document.getElementById('camp-flyer').value.trim();
            const form = document.getElementById('camp-form').value.trim();
            const desc = document.getElementById('camp-desc').value.trim();

            const newCamp = {
                id: Date.now(),
                title,
                date,
                flyer,
                form,
                desc
            };

            camps.push(newCamp);
            await saveSlots();

            document.getElementById('camp-title').value = '';
            document.getElementById('camp-date').value = '';
            document.getElementById('camp-flyer').value = '';
            document.getElementById('camp-form').value = '';
            document.getElementById('camp-desc').value = '';

            alert('Camp flyer successfully published to the app!');
            renderAdminCamps();
        }

        function renderAdminBookings() {
            const list = document.getElementById('admin-bookings-list');
            if (!list) return;
            list.innerHTML = '';

            if (slots.length === 0) {
                list.innerHTML = '<p class="text-xs text-slate-500">No events or training slots created yet.</p>';
                return;
            }

            slots.forEach(slot => {
                const item = document.createElement('div');
                item.className = 'bg-slate-900 border border-slate-800 p-3 rounded-lg flex flex-col md:flex-row justify-between items-start md:items-center gap-2 text-xs shadow';
                
                if (slot.isTeamEvent) {
                    item.innerHTML = `
                        <div>
                            <span class="text-purple-400 font-bold uppercase tracking-wider text-[10px]">Team Event</span><br>
                            <strong class="text-white">slot.datetime</strong>({slot.type})
                        </div>
                        <div class="flex gap-2">
                            <button onclick="deleteSlot(${slot.id})" class="bg-rose-600/20 text-rose-400 hover:bg-rose-600/30 px-2.5 py-1 rounded transition">Delete</button>
                        </div>
                    `;
                } else {
                    const filledCount = slot.players.filter(p => p !== "").length;
                    let playerSummary = slot.players.map((p, i) => `P${i+1}: ${p || 'Open'}`).join(' | ');

                    item.innerHTML = `
                        <div>
                            <strong class="text-white">slot.datetime</strong>({slot.type})<br>
                            <span class="text-slate-300">Slots Filled: filledCount/{slot.slotsNeeded} [ ${playerSummary} ]</span>
                        </div>
                        <div class="flex gap-2">
                            <button onclick="resetSlot(${slot.id})" class="bg-amber-600/20 text-amber-400 hover:bg-amber-600/30 px-2.5 py-1 rounded transition">Reset Slots</button>
                            <button onclick="deleteSlot(${slot.id})" class="bg-rose-600/20 text-rose-400 hover:bg-rose-600/30 px-2.5 py-1 rounded transition">Delete</button>
                        </div>
                    `;
                }
                list.appendChild(item);
            });
        }

        function renderAdminCamps() {
            const list = document.getElementById('admin-camps-list');
            if (!list) return;
            list.innerHTML = '';

            if (!camps || camps.length === 0) {
                list.innerHTML = '<p class="text-xs text-slate-500">No camps created yet.</p>';
                return;
            }

            camps.forEach(camp => {
                const item = document.createElement('div');
                item.className = 'bg-slate-900 border border-slate-800 p-3 rounded-lg flex justify-between items-center text-xs shadow';
                item.innerHTML = `
                    <div>
                        <strong class="text-white">camp.title</strong>({camp.date})<br>
                        <span class="text-slate-400">Flyer: ${camp.flyer} | Form: ${camp.form}</span>
                    </div>
                    <button onclick="deleteCamp(${camp.id})" class="bg-rose-600/20 text-rose-400 hover:bg-rose-600/30 px-2.5 py-1 rounded transition">Delete</button>
                `;
                list.appendChild(item);
            });
        }

        async function resetSlot(id) {
            const slot = slots.find(s => s.id === id);
            if (slot) {
                slot.players = new Array(slot.slotsNeeded).fill("");
                slot.phones = new Array(slot.slotsNeeded).fill("");
                await saveSlots();
                renderAdminBookings();
            }
        }

        async function deleteSlot(id) {
            slots = slots.filter(s => s.id !== id);
            await saveSlots();
            renderAdminBookings();
        }

        async function deleteCamp(id) {
            camps = camps.filter(c => c.id !== id);
            await saveSlots();
            renderAdminCamps();
        }

        window.onload = function() {
            fetchSlots();
            setInterval(() => {
                fetchSlots(true);
            }, 4000);
        };
    </script>
</body>
</html>


