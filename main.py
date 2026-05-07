#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════════╗
# ║  🔥🔥🔥  HYPE ENGINE v4.2.0  🔥🔥🔥                ║
# ║                                                                  ║
# ║  STATUS .......... FULLY OPERATIONAL                             ║
# ║  MODE ............ BEAST                                         ║
# ║  PLATFORMS ....... KICK / TWITCH / REDDIT                        ║
# ║  INSTANCES ....... MULTI-SPAWN                                   ║
# ║  STEALTH ......... RANDOMIZED 450-800s                           ║
# ║  LOOP ............ ♾️  INFINITE                                  ║
# ╚══════════════════════════════════════════════════════════════════╝

import requests
import base64
import random
from seleniumbase import SB


# ═══════════════════════════════════════════════════════════════════
#  PHASE 0 — 🌍 GEO-LOCK: ACQUIRING TARGET COORDINATES
# ═══════════════════════════════════════════════════════════════════

print("🌍 [GEO-LOCK] Acquiring coordinates...")
geo_data      = requests.get("http://ip-api.com/json/").json()
proxy_str     = False
latitude      = geo_data["lat"]
longitude     = geo_data["lon"]
timezone_id   = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()   # e.g., 'us'
print(f"   ├── Lat/Lon   : {latitude}, {longitude}")
print(f"   ├── Timezone  : {timezone_id}")
print(f"   └── Country   : {language_code.upper()}")
print()


# ═══════════════════════════════════════════════════════════════════
#  PHASE 1 — 🔐 ENCRYPTED PAYLOAD DECODE
# ═══════════════════════════════════════════════════════════════════

name   = "YnJ1dGFsbGVz"
name_d = base64.b64decode(name)
fulln  = name_d.decode("utf-8")

print(f"🔐 [DECRYPT] Payload decoded → {fulln}")
print()


# ═══════════════════════════════════════════════════════════════════
#  PHASE 2 — 🎯 TARGET ACQUISITION
# ═══════════════════════════════════════════════════════════════════

URL_KICK   = f"https://kick.com/{fulln}"
URL_TWITCH = f"https://www.twitch.tv/{fulln}"
URL_CLIP   = (
    f"https://www.twitch.tv/{fulln}/clip/"
    "HumbleStrangeKuduJonCarnage-xTG7nQKnhrSA-BZk"
)
URL_REDDIT = f"https://www.reddit.com/r/{fulln}"

print("🎯 [TARGETS]")
print(f"   ├── KICK   : {URL_KICK}")
print(f"   ├── TWITCH : {URL_TWITCH}")
print(f"   ├── CLIP   : {URL_CLIP}")
print(f"   └── REDDIT : {URL_REDDIT}")
print()


# ═══════════════════════════════════════════════════════════════════
#  🧰 HELPER — Cookie / Consent Wall Bypass
# ═══════════════════════════════════════════════════════════════════

def _smash_accept(driver, label="driver"):
    """Destroy every cookie/consent wall in sight."""
    if driver.is_element_present('button:contains("Accept")'):
        driver.cdp.click('button:contains("Accept")', timeout=4)
        print(f"   🛡️  [{label}] Cookie wall OBLITERATED")


def _smash_start_watching(driver, label="driver"):
    """Auto-click 'Start Watching' if Twitch demands it."""
    if driver.is_element_present('button:contains("Start Watching")'):
        driver.cdp.click('button:contains("Start Watching")', timeout=4)
        driver.sleep(10)
        print(f"   🎬 [{label}] 'Start Watching' → ENGAGED")


# ═══════════════════════════════════════════════════════════════════
#  🚀 MAIN LOOP — INFINITE ENGAGEMENT ENGINE
# ═══════════════════════════════════════════════════════════════════

cycle = 0

print("🚀 [ENGINE] Entering infinite loop...")
print("=" * 60)
print()

while True:
    cycle += 1
    stealth_hold = random.randint(450, 800)

    print(f"┌──────────────────────────────────────────────────────┐")
    print(f"│  ♻️  CYCLE #{cycle:<6}  │  ⏱️  Stealth hold: {stealth_hold}s      │")
    print(f"└──────────────────────────────────────────────────────┘")

    with SB(
        uc=True,
        locale="en",
        ad_block=True,
        chromium_arg="--disable-webgl",
        proxy=proxy_str,
    ) as bot:

        # ── PHASE 3A — KICK.COM WARM-UP ─────────────────────────
        print("   🟢 PHASE 3A — KICK warm-up")
        bot.activate_cdp_mode(
            URL_KICK,
            tzone=f"{timezone_id}",
            geoloc=(latitude, longitude),
        )
        bot.sleep(2)
        bot.cdp.open(URL_KICK)
        bot.sleep(10)
        print("   ✅ KICK warm-up complete")

        # ── PHASE 3B — CLIP ENGAGEMENT ──────────────────────────
        print("   🟢 PHASE 3B — Clip engagement")
        bot.cdp.open(URL_CLIP)
        bot.sleep(10)
        print("   ✅ Clip viewed")

        # ── PHASE 3C — TWITCH PRIMARY DEPLOY ────────────────────
        print("   🟢 PHASE 3C — Twitch PRIMARY deploy")
        bot.cdp.open(URL_TWITCH)
        bot.sleep(2)

        _smash_accept(bot, "PRIMARY")
        bot.sleep(2)
        bot.sleep(12)

        _smash_start_watching(bot, "PRIMARY")
        _smash_accept(bot, "PRIMARY")

        # ── PHASE 4 — MULTI-INSTANCE DEPLOYMENT ─────────────────
        is_live = bot.is_element_present("#live-channel-stream-information")

        if is_live:
            print("   🔴 STREAM IS LIVE — deploying multi-instance!")
            _smash_accept(bot, "PRIMARY")

            # 🔥 SPAWN SECOND VIEWER INSTANCE 🔥
            print("   🔥 Spawning SECONDARY instance...")
            bot2 = bot.get_new_driver(undetectable=True)
            bot2.activate_cdp_mode(
                URL_TWITCH,
                tzone=f"{timezone_id}",
                geoloc=(latitude, longitude),
            )
            bot2.sleep(10)

            _smash_start_watching(bot2, "SECONDARY")
            _smash_accept(bot2, "SECONDARY")

            # ── COMMENTED: REDDIT INSTANCE (ready to deploy) ────
            # print("   🔥 Spawning REDDIT instance...")
            # bot3 = bot.get_new_driver(undetectable=True)
            # bot3.activate_cdp_mode(
            #     URL_REDDIT,
            #     tzone=f"{timezone_id}",
            #     geoloc=(latitude, longitude),
            # )
            # bot3.sleep(10)
            # _smash_accept(bot3, "REDDIT")
            # bot3.sleep(10)
            # bot3.cdp.gui_press_key("K")

            # ── STEALTH HOLD ────────────────────────────────────
            print(f"   ⏳ Stealth hold: chilling for {stealth_hold}s...")
            bot.sleep(stealth_hold)
            print("   ✅ Cycle complete")
        else:
            print("   💀 Stream is OFFLINE — aborting engine.")
            break

    print()

# ╔══════════════════════════════════════════════════════════════════╗
# ║  🏁  ENGINE TERMINATED — Total cycles: {cycle}                 ║
# ╚══════════════════════════════════════════════════════════════════╝
print()
print(f"🏁 ENGINE TERMINATED after {cycle} cycle(s). GG.")
